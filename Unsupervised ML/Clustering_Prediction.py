#!/usr/bin/env python
# coding: utf-8

import pickle


# Load from file if needed
pkl_filename = "KMeans.pkl"
with open(pkl_filename, 'rb') as file:
    clustering_model = pickle.load(file)


print("Enter the following details to make the predictions:- n")

Avg_Credit_Limit = int(intput("Enter The Average Credit Limit:- "))
Total_Credit_Cards = int(intput("Enter Total # of Credit Cards:- "))
Total_visits_bank = int(intput("Enter Total Visits to Bank:- "))
Total_visits_online = int(intput("Enter Total Visits Online:- "))
Total_calls_made = int(intput("Enter Total Calls Made:- "))

customer_prediction = clustering_model.predict([[Avg_Credit_Limit,Total_Credit_Cards,Total_visits_bank,Total_visits_online,Total_calls_made]])

print(customer_prediction)

