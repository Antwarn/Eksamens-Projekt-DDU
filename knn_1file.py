import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# fly ryg bryst crawl medley køn alder højde vægt
x = [   [58, 59, 67, 53, 266, 2004, 180, 66],
        [53, 56, 61, 50, 252, 2004, 182, 76],
        [55, 56, 75, 51, 275, 2004, 192, 90],
        [55, 56, 60, 50, 254, 1998, 189, 84],
        [54, 59, 66, 50, 286, 2001, 176, 72],
        [58, 55, 69, 54, 284, 1999, 187, 73],
        [60, 59, 96, 55, 288, 2005, 191, 97],
        [64, 63, 76, 54, 307, 2006, 178, 76],
        #kvinder
        [58, 63, 70, 59, 279, 1998, 182, 73],
        [63, 65, 73, 61, 280, 2003, 162, 55],
        [61, 67, 75, 60, 304, 2004, 165, 57],
        [62, 65, 76, 57, 294, 2004, 168, 64],
        [63, 60, 72, 58, 300, 2002, 170, 65]]


y = [0,0,0,0,0,0,0,0,1,1,1,1,1]

#printer vores features
print(x)

#printer vores labels
print(y)

#her splitter vi vores x og y og tester på det der svare til 20% af hele vores datasæt
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

#her bestemer vi vores nærmeste naboer
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

#her forudser vi ud fra vores data om det er en kvinde (1) eller en mand (0)
print(X_test)
print("vi forudser",y_pred)

#her tager vi vores vores labels og sammenligner dem med vores træningsdata
#for at se hvor arkurrat vores algorithme er
print("nøjaktigheden på vores forudsigelse er",accuracy_score(y_test,y_pred))