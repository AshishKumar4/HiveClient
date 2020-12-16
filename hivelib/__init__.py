import os
import json
import xmlrpc.client

global rpc 
rpc = None

global experimentId
experimentId = ''

def init(expId = None):
    global experimentId
    if expId == None:
        global rpc
        rpc = xmlrpc.client.ServerProxy('http://localhost:8447')
        data, status = rpc.getExperiment()
        (config, resource) = data
        if status == -2:
            print("No experiments left, terminating...")
            exit(0)
        experimentId = config['experimentId']
    else:
        experimentId = expId
    return config, resource

def setWandb(wandbId):
    global rpc 
    global experimentId 
    status = rpc.setWandb(experimentId, wandbId)
    if status == True:
        print("Wandb ID set Successfully!")

def concludeExperiment(results, status):
    global rpc 
    global experimentId

    if type(status) == str:
        status = status.lower()
        assert status in ['success', 'error']
    elif type(status) == int:
        if status == 0:
            status = 'success' 
        else:
            status = 'error'
    
    status = rpc.concludeExperiment(experimentId, results, status)
    if status == True:
        print("Experiment ", experimentId, "Concluded successfully!")


