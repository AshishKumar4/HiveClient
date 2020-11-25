#!/usr/bin/python3

import os
import json
import traceback 
from sockets import sockets
import requests

from hivelib_internal.common import *
from hivelib_internal import hiveAPI
import trainer

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

global CONFIG
CONFIG = None

global api
api = None

def rpc_getExperiment():
    resource = CONFIG['resource'].allocate()
    global api
    config, status = api.fetchExperiment(resource)
    if status == -1:
        print("Error fetching experiments!")
        return None, -1
    elif status == -2:
        print("No experiments left in the queue, Terminating")
        return None, -2
    elif status == 0:
        print("Successfully fetched config and resource!")
        return (config, resource), status
    else:
        return None, None 

def rpc_setWandb(experimentId, wandbId):
    global api 
    status = api.setExperimentWandb(experimentId, wandbId)
    if status == 0:
        return True 
    elif status == -1:
        print("Experiment id ", experimentId, "Is Invalid!")
    elif status == -2:
        print("Wandb id ", wandbId, "Is Invalid!")
    print("Unable to set experiment's wandb id")
    return None

def rpc_concludeExperiment(experimentId, results, status):
    global api
    status = api.concludeExperiment(experimentId, results, status)
    if status == 0:
        return True 
    elif status == -1:
        print("Experiment id ", experimentId, "Is Invalid!")
    print("Some error while concluding experiment", experimentId)
    return None

if __name__ == '__main__':
    config = getConfig()
    if config == None:
        print("No config file found at ", DEFAULT_CONFIG_LOC, 
                ", Launching First run setup wizard...")
        config = createConfig()
        if config == None:
            print("Please try again...")
            exit(-1)
    
    global CONFIG
    CONFIG = config

    global api 
    api = hiveAPI.MindApi(ip=config['ip'], port=config['port'], 
                            apiKey=config['apiKey'], identifier=config['identifier']

    server = SimpleXMLRPCServer(('0.0.0.0', 8447),)
    server.register_introspection_functions()
    server.register_function(rpc_getExperiment, 'getExperiment')
    server.register_function(rpc_setWandb, 'setWandb')
    server.register_function(rpc_concludeExperiment, 'concludeExperiment')

    print("Initialization completed successfully, Launching RPC process")
    print("Entering infinite loop!")
    server.serve_forever()


