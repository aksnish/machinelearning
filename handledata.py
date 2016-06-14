import csv
import os
import random

def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

filename = "C:\\Users\\hm7xnk\\Documents\\GitHub\\machinelearning\\data\\pima-indians-diabetes.pima-indians-diabetes.data.csv"
# print(filename)
dataset = loadCsv(filename)

print("Loaded data file {0} with {1} rows".format(filename, len(dataset)));



def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


dataset = [[1], [2], [3], [4], [5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
print("Split {0} rows into train with {1} and test with {2}".format(len(dataset), train, test));

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


dataset = [[1,20,1], [2,21,0], [3,22,1]]
separated = separateByClass(dataset)
print("Separated instances: {0}".format(separated));





