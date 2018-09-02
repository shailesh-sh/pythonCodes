from sklearn.datasets import load_digits
from sklearn import svm
import matplotlib.pyplot as plt
import random

digits=load_digits(random.randint(0,10))
plt.gray()
plt.matshow(digits.images[20])
plt.show()
#print (digits.images[20])

clf=svm.SVC()
clf.fit(digits.data[:-1],digits.target[:-1])
prediction = clf.predict(digits.data[20:21])
print ("it's ", *prediction)
