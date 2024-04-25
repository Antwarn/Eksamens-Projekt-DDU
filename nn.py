import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

class StockPricePredictor:
    def __init__(self, data_file):
        self.data_file = data_file
        self.dataset = None
        self.dataset_train = None
        self.training_set = None
        self.sc = None
        self.X_train = None
        self.y_train = None
        self.model = None

    def load_data(self):
        self.dataset = pd.read_csv(self.data_file)
        self.dataset_train = self.dataset.drop(columns=['company'])
        self.training_set = self.dataset_train.iloc[:, 1:2].values

    def scale_data(self):
        self.sc = MinMaxScaler(feature_range=(0, 1))
        self.training_set_scaled = self.sc.fit_transform(self.training_set)

    def prepare_training_data(self):
        X_train = []
        y_train = []
        for i in range(60, len(self.training_set)):
            X_train.append(self.training_set_scaled[i - 60:i, 0])
            y_train.append(self.training_set_scaled[i, 0])
        self.X_train, self.y_train = np.array(X_train), np.array(y_train)
        self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))

    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.X_train.shape[1], 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(units=1))

    def compile_model(self):
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train_model(self, epochs=100, batch_size=32):
        self.model.fit(self.X_train, self.y_train, epochs=epochs, batch_size=batch_size)

    def prepare_test_data(self):
        dataset_total = pd.concat((self.dataset_train['Open'], self.dataset['Open']), axis=0)
        inputs = dataset_total[len(dataset_total) - len(self.dataset) - 60:].values.reshape(-1, 1)
        inputs = self.sc.transform(inputs)
        X_test = []
        for i in range(60, len(inputs)):
            X_test.append(inputs[i - 60:i, 0])
        self.X_test = np.array(X_test)
        self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1], 1))

    def predict_stock_price(self):
        predicted_stock_price = self.model.predict(self.X_test)
        return self.sc.inverse_transform(predicted_stock_price)

    def visualize_results(self, predicted_stock_price):
        plt.plot(self.dataset['Open'].values, color='black', label='Rigtige aktie pris')
        plt.plot(predicted_stock_price, color='green', label='Forudsagte aktie pris')
        plt.title('Forusigelse')
        plt.xlabel('Tid')
        plt.ylabel('pris')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    data_file = 'google_filtered_dataset.csv'
    predictor = StockPricePredictor(data_file)
    predictor.load_data()
    predictor.scale_data()
    predictor.prepare_training_data()
    predictor.build_model()
    predictor.compile_model()
    predictor.train_model()
    predictor.prepare_test_data()
    predicted_stock_price = predictor.predict_stock_price()
    predictor.visualize_results(predicted_stock_price)
