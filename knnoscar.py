import numpy as np


data = [58, 59, 67, 53, 266, 0, 2004, 180, 66,
        53, 56, 61, 50, 252, 0, 2004, 182, 76,
        55, 56, 75, 51, 275, 0, 2004, 192, 90,
        55, 56, 60, 50, 254, 0, 1998, 189, 84,
        54, 59, 66, 50, 286, 0, 2001, 176, 72,
        58, 55, 69, 54, 284, 0, 1999, 187, 73,
        60, 59, 96, 55, 288, 0, 2005, 191, 97,
        64, 63, 76, 54, 307, 0, 2006, 178, 76]



# Konverter listen til et NumPy-array
numpy_array = np.array(data)


# Udskriv NumPy-arrayet
print(numpy_array)


# Define the number of features (excluding labels)
num_features = 8


# Reshape the data into a 2D array with multiple labels
reshaped_data = numpy_array.reshape(-1, num_features + 1)  # +1 for the label


# Split into X (features) and y (labels)
X = reshaped_data[:, :-1]  # Features (all columns except the last)
y = reshaped_data[:, -1]   # Labels (the last column)


# Print X and y
print("X (features):")
print(X)
print("y (labels):")
print(y)



# run knn on the data

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)





# divide data into training and testing

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)



# train the model

knn.fit(X_train, y_train)



# test the model

y_pred = knn.predict(X_test)



# print the accuracy

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, y_pred))



# draw accuracy vs k



import matplotlib.pyplot as plt


k_range = range(1, 20)

scores = []

for k in k_range:

    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    scores.append(accuracy_score(y_test, y_pred))



plt.plot(k_range, scores)

plt.xlabel('k')

plt.ylabel('accuracy')

plt.show()