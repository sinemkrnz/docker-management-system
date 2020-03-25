from flask import Flask
from flask import request, jsonify
import json
from algorithms import algorithms

sortedBy = algorithms()

app = Flask(__name__)


@app.route('/deneme', methods=['POST'])
def bubble2():
    data = request.get_json()
    return jsonify(data['content'])

@app.route('/bubble', methods=['POST'])
def bubble():
    data = request.get_json()
    unorderedArray = data['content']
    orderedArray = sortedBy.bubble_sort(unorderedArray)
    return createResponse("Bubble Sort", orderedArray)


@app.route('/selection', methods=['POST'])
def selection():
    data = request.get_json()
    unorderedArray = data['content']
    orderedArray = sortedBy.selection_sort(unorderedArray)
    return createResponse("Selection Sort", orderedArray)


@app.route('/insertion', methods=['POST'])
def insertion():
    data = request.get_json()
    unorderedArray = data['content']
    orderedArray = sortedBy.insertion_sort(unorderedArray)
    return createResponse("Insertion Sort", orderedArray)


def createResponse(algorithmName, orderedArray):
    response = {
        "Algorithm_Name": algorithmName,
        "Result": orderedArray
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="localhost", port=int("5001"), debug=True)

# docker build --tag sorted_algorithm .
# docker run -d --rm -ti --name python-app -p 5000:5000 sorted_algorithm

"""
    # url       =>      http://0.0.0.0:5000/bubble    
    # type      =>      POST
    # headers   =>      Content-Type:application/json
    # body      =>      {"content":[2,4,1,8,6,23,24,67,23,8,3,5]}
    # response  =>      {"Algorithm_Name": "Insertion Sort","Result": [1,2,3,4,5,6,8,8,23,23,24,67]} 
"""
