# Importerer nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

# Definerer en klasse til aktieprisforudsigelse
class StockPricePredictor:
    def __init__(self, data_file):
        self.data_file = data_file  # Sti til datafilen
        self.dataset = None
        self.dataset_train = None
        self.training_set = None
        self.sc = None
        self.X_train = None
        self.y_train = None
        self.model = None

    # Funktion til indlæsning af data
    def load_data(self):
        self.dataset = pd.read_csv(self.data_file)  # Læs datafilen
        self.dataset_train = self.dataset.drop(columns=['company'])  # Fjern 'company' kolonnen
        self.training_set = self.dataset_train.iloc[:, 1:2].values  # Vælg 'Last' kolonnen

    # Funktion til skalering af data
    def scale_data(self):
        self.sc = MinMaxScaler(feature_range=(0, 1))  # Initialiser MinMaxScaler
        self.training_set_scaled = self.sc.fit_transform(self.training_set)  # Skaler dataen

    # Funktion til at forberede træningsdata
    def prepare_training_data(self):
        X_train = []
        y_train = []
        for i in range(60, len(self.training_set)):
            X_train.append(self.training_set_scaled[i - 60:i, 0])  # Skab input sekvenser
            y_train.append(self.training_set_scaled[i, 0])  # Skab mål sekvenser
        self.X_train, self.y_train = np.array(X_train), np.array(y_train)  # Konverter til numpy arrays
        self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))  # Reshape input til LSTM

    # Funktion til at bygge LSTM modellen
    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.X_train.shape[1], 1)))  # Første LSTM lag
        self.model.add(Dropout(0.2))  # Dropout lag for at undgå overfitting
        self.model.add(LSTM(units=50, return_sequences=True))  # Andet LSTM lag
        self.model.add(Dropout(0.2))  # Dropout lag
        self.model.add(LSTM(units=50, return_sequences=True))  # Tredje LSTM lag
        self.model.add(Dropout(0.2))  # Dropout lag
        self.model.add(LSTM(units=50))  # Fjerde LSTM lag uden return_sequences
        self.model.add(Dropout(0.2))  # Dropout lag
        self.model.add(Dense(units=1))  # Output lag

    # Funktion til at kompilere modellen
    def compile_model(self):
        self.model.compile(optimizer='adam', loss='mean_squared_error')  # Brug Adam optimizer og mean_squared_error som tab

    # Funktion til at træne modellen
    def train_model(self, epochs=10, batch_size=32):
        self.model.fit(self.X_train, self.y_train, epochs=epochs, batch_size=batch_size)  # Træn modellen

    # Funktion til at forberede testdata
    def prepare_test_data(self):
        dataset_total = pd.concat((self.dataset_train['Last'], self.dataset['Last']), axis=0)  # Kombiner trænings- og testdata
        inputs = dataset_total[len(dataset_total) - len(self.dataset) - 60:].values.reshape(-1, 1)  # Forbered input
        inputs = self.sc.transform(inputs)  # Skaler input
        X_test = []
        for i in range(60, len(inputs)):
            X_test.append(inputs[i - 60:i, 0])  # Skab input sekvenser til test
        self.X_test = np.array(X_test)  # Konverter til numpy array
        self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1], 1))  # Reshape input til LSTM

    # Funktion til at forudsige aktiepriser
    def predict_stock_price(self):
        predicted_stock_price = self.model.predict(self.X_test)  # Forudsige aktiepriser
        return self.sc.inverse_transform(predicted_stock_price)  # Invers transformer forudsigelserne

    # Funktion til at visualisere resultaterne
    def visualize_results(self, predicted_stock_price):
        plt.plot(self.dataset['Last'].values, color='black', label='Rigtige aktie pris')  # Plot de rigtige aktiepriser
        plt.plot(predicted_stock_price, color='green', label='Forudsagte aktie pris')  # Plot de forudsagte aktiepriser
        plt.title('Forudsigelse')  # Titel på grafen
        plt.xlabel('Tid')  # X-akse label
        plt.ylabel('Pris')  # Y-akse label
        plt.savefig('nvida09')  # Gem grafen som billede
        plt.legend()  # Vis legend
        plt.show()  # Vis grafen

# Hovedprogram til at køre hele processen
if __name__ == "__main__":
    data_file = 'nvida09.csv'  # Filnavn med data
    predictor = StockPricePredictor(data_file)  # Opret en StockPricePredictor instans
    predictor.load_data()  # Indlæs data
    predictor.scale_data()  # Skaler data
    predictor.prepare_training_data()  # Forbered træningsdata
    predictor.build_model()  # Byg modellen
    predictor.compile_model()  # Kompilér modellen
    predictor.train_model()  # Træn modellen
    predictor.prepare_test_data()  # Forbered testdata
    predicted_stock_price = predictor.predict_stock_price()  # Forudsig aktiepriser
    predictor.visualize_results(predicted_stock_price)  # Visualisér resultaterne
