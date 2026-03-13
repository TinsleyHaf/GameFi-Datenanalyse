# Machine Learning Models for Churn Prediction and Price Forecasting

## Random Forest Model

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Load your dataset
# dataset = pd.read_csv('path/to/dataset.csv')

# Preprocessing steps go here

# Example: Splitting data
# X = dataset.drop('target_column', axis=1)
# y = dataset['target_column']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
predictions = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f'Random Forest Model Accuracy: {accuracy}')


## LSTM Model for Price Forecasting

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Load your dataset
# dataset = pd.read_csv('path/to/price_data.csv')

# Preprocessing steps go here

# Example: Reshaping data for LSTM
# data = np.array(dataset['price_column'])
# data = data.reshape((data.shape[0], data.shape[1], 1))

# Create LSTM model
lstm_model = Sequential()
lstm_model.add(LSTM(50, return_sequences=True, input_shape=(data.shape[1], 1)))
lstm_model.add(Dropout(0.2))
lstm_model.add(LSTM(50))
lstm_model.add(Dropout(0.2))
lstm_model.add(Dense(1))

lstm_model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model
lstm_model.fit(data, epochs=100, batch_size=32)
