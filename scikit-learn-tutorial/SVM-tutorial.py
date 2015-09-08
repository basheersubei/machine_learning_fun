import matplotlib.pyplot as plt
import numpy as numpy
import cv2
from sklearn import datasets
from sklearn import svm

# SVM (support vector machines)
# basically divvies up points into categories

digits = datasets.load_digits()

original_length = digits.images[0].shape[0]
original_width = digits.images[0].shape[1]

# digit0_large = cv2.resize(digits.images[0], (240, 240), interpolation=cv2.INTER_NEAREST)
# cv2.imshow('digit0', digit0_large)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# classifier
clf = svm.SVC(gamma=0.001, C=100)

# use even numbers for training
x, y = digits.data[::2], digits.target[::2]
# print("length of x: " + str(len(x)) + " and length of y: " + str(len(y)))

clf.fit(x, y)

predictions = clf.predict(digits.data[1::2])
values = digits.target[1::2]
# print('Prediction: ', clf.predict(digits.data[1::2]))

mistakes = 0
for (p, v) in zip(predictions, values):
    if(p != v):
        mistakes += 1
#         print('p: ' + str(p) + ' is not v: ' + str(v))
# print mistakes
# print len(predictions)
print('accuracy: ' + str(100.0 * (len(predictions) - mistakes) / len(predictions)) + '%')

