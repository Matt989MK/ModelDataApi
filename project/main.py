# # import flask microframework library
# from flask import Flask, jsonify
#
# # initialize the flask application
# app = Flask(__name__)
#
# # endpoint api_1() with post method
#
# @app.route("/api/v1.0/csharp_python_restfulapi_json", methods=["POST"])
# def csharp_python_restfulapi_json():
#     """
#     simple c# test to call python restful api web service
#     """
#     try:
# #         get request json object
#         request_json = request.get_json()
# #         convert to response json object
#         response = jsonify(request_json)
#         response.status_code = 200
#     except:
#         exception_message = sys.exc_info()[1]
#         response = json.dumps({"content":exception_message})
#         response.status_code = 400
#     return response
#
#
#
#
# if __name__ == "__main__":
#     #     run flask application in debug mode
# app.run(debug=True)

# Apriori

# Run the following command in the terminal to install the apyori package: pip install apyori

# Importing the libraries
import csv
from dataOperations import DataOperations
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('../csvData.csv', header=None, error_bad_lines=False, quoting=csv.QUOTE_NONE, na_filter=False)
movies = []
#print(dataset)
for i in range(0,45):

    movies.append([str(dataset.values[i, j]) for j in range(0,20)])
#print(movies)
# Training the Apriori model on the dataset
from apyori import apriori

rules = apriori(transactions=movies, min_support=0.06, min_confidence=0.5, min_lift=5, min_length=2,
                max_length=4)

print("----------------------")

#print(rules)
# Visualising the results

## Displaying the first results coming directly from the output of the apriori function
results = list(rules)
#print(results[0])

## Putting the results well organised into a Pandas DataFrame
def inspect(results):

    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]

    return list(zip(lhs, rhs, supports, confidences, lifts))
    #DataOperations.insert(lhs, rhs, supports, confidences, lifts)

resultsinDataFrame = pd.DataFrame(inspect(results),
                                  columns=['Book1', 'Book2', 'Support', 'Confidence', 'Lift'])

## Displaying the results non sorted
#resultsinDataFrame


## Displaying the results sorted by descending lifts
resultsinDataFrame.nlargest(n=20, columns='Lift')
print(resultsinDataFrame)
for ind in resultsinDataFrame.index:
    DataOperations.insert(resultsinDataFrame['Book1'][ind],resultsinDataFrame['Book2'][ind],round(resultsinDataFrame['Support'][ind],2), round(resultsinDataFrame['Confidence'][ind],2), round(resultsinDataFrame['Lift'][ind],2))
