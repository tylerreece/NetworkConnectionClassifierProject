import numpy as numpy
import pandas as pandas
from sklearn import svm

input_file = "training1.csv"

data_array = numpy.loadtxt(input_file, delimiter=',', skiprows=1)
data = data_array[:, :-1]
target = data_array[:,-1:]
target= [y for x in target for y in x]

clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(data, target)