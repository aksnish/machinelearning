# machinelearning

* Everything about machine learning from scratch in python


## Naive Bayes Classifier
* This is a supervised learning approach to classification
* It is an intuitive method that uses the probabilities of each attribute belonging to each class to make a prediction
* Naive Bayes simplifies the calculation of probabilities by assuming that the probability of each attribute belonging to a given class value is independent of all the other attributes
* This is a strong assumption but results in a fast and effective method.
* The probability of a class value given a value of an attribute is called the conditional probability. 
* By multiplying the conditional probabilities together for each attribute for a given class value, we have a probability of a data instance belonging to that class.
* To make a prediction we can calculate probabilities of the instance belonging to each class and select the class value with the highest probability.

## Steps for computation
* Handle Data: Load the data from CSV file and split it into training and test datasets.
* Summarize Data: summarize the properties in the training dataset so that we can calculate probabilities and make predictions.
* Make a Prediction: Use the summaries of the dataset to generate a single prediction.
* Make Predictions: Generate predictions given a test dataset and a summarized training dataset.
* Evaluate Accuracy: Evaluate the accuracy of predictions made for a test dataset as the percentage correct out of all predictions made.
* Tie it Together: Use all of the code elements to present a complete and standalone implementation of the Naive Bayes algorithm.

