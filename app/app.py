from flask import Flask, request
import circuit as c
import json
import pprint

Circuit = c.Circuit
solutionCircuitsByLevel = c.allCircuits

app = Flask(__name__)


@app.route('/getCircuits')
def getCircuits():
    return ''

@app.route('/getQTP')
def getQTP():
    return 'QTP'

@app.route('/checkCircuit', methods = ['POST'])
def checkCircuit():
    circuit = Circuit.from_json(request.get_json())
    solutionsCircuits = solutionCircuitsByLevel[circuit.level]
    if circuit in solutionsCircuits:
        return 'SUCCESS'
    else:
        return 'FAILURE'

@app.route('/runOnQiskit', methods = ['POST'])
def runOnQiskit():
    print(request.get_json())
    return 'QISKIT'
