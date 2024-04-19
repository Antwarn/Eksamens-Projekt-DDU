import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset from the CSV file
data = pd.read_csv('stockinfo.csv')

# Perform data preprocessing and feature engineering
data['date'] = pd.to_datetime(data['date'])
data['timestamp'] = data['date'].apply(lambda x: x.timestamp())
data['days_since_prev'] = (data['date'] - data['date'].shift()).fillna(0).dt.days
data['price_change'] = data['price'].pct_change()
data['price_change'].fillna(0, inplace=True)

# Select relevant features for predicting stock price changes
X = data[['days_since_prev', 'volume', 'market_cap']].values
y = np.where(data['price_change'] > 0, 1, 0)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the KNN model and number of neighbors to consider
model = KNeighborsClassifier(n_neighbors=3)

# Train the KNN model using the training data
model.fit(X_train, y_train)

# Make predictions using the trained model
predictions = model.predict(X_test)

# Evaluate the model's performance
print('Confusion Matrix:')
print(confusion_matrix(y_test, predictions))
print('Classification Report:')
print(classification_report(y_test, predictions))