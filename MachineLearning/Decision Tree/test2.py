import car_dataset
from ID3 import ID3
import numpy as np

X, Y, F = car_dataset.load(return_attr_names=True)
Xtrain, Ytrain, Xtest, Ytest = car_dataset.load(split_train_test=0.8)
tree = ID3(Xtrain, Ytrain, F)
print(tree.parent)
print(tree.node)
print(tree.attr_id)
print(tree.branch)

Ztest = tree.predict(Xtest)
rate = np.sum(Ytest == Ztest) / len(Ytest) * 100
#print(Ztest)
print('Accuracy rate (evaluate by training set) = ', rate, '%')

#Xnew = [['vhigh', 'low', '4', 'more', 'big', 'high']]
#Znew = tree.predict(Xnew)
#print(Znew)

#tree.show()