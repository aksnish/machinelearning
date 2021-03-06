import csv
import os
import random
import math

def loadCsv(filename):
    lines = csv.reader(open(filename,"rt"))
    dataset = list(lines)
    for i in range(len(dataset)):

        dataset[i] = [float(x) for x in dataset[i]]

    return dataset


filename = 'pima-indians-diabetes.pima-indians-diabetes.data.csv'
dataset = loadCsv(filename)
# print("Loaded data file {0} with {1} rows".format(filename, len(dataset)));


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
# print("Separated instances: {0}".format(separated));


def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

numbers = [1,2,3,4,5]
# print("Summary of {0}: mean={1}, stdev={2}".format(numbers, mean(numbers), stdev(numbers)));


def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries


dataset = [[1,20,0], [2,21,1], [3,22,0]]
summary = summarize(dataset)
# print("Attribute summaries: {0}".format(summary));


def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.iteritems():
		summaries[classValue] = summarize(instances)
	return summaries


dataset = [[1,20,1], [2,21,0], [3,22,1], [4,22,0]]
summary = summarizeByClass(dataset)
print("Summary by class value: {0}".format(summary));