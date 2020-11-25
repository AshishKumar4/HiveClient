import pickle 
import os
import secrets
from hivelib_internal import resources

DEFAULT_CONFIG_LOC = '~/.hiveConfig'

def getConfig():
    try:
        f = pickle.loads(open(DEFAULT_CONFIG_LOC, 'r').read())
    except Exception as e:
        print("Error while loading config: \n\t=>", e)
        traceback.print_tb(e.__traceback__)
        return None
    return f

def authenticateApiKey(ip, port, apiKey):
    return True

def createConfig():
    ip = input("Provide the IP address of the Central Hive Server: ")
    port = int(input("Provide the port of the Central Hive Server (80 for default): "))
    apiKey = input("Provide a valid API key: ")
    auth = authenticateApiKey(ip=ip, port=port, apiKey=apiKey)
    if auth == True:
        print("Authenticated! ")
        identifier = input("Provide a Unique name/id for this client or leave blank: ")
        if identifier == '':
            identifier = secrets.token_hex(8)
            print("\tAssigning the id ", identifier)
        resourceCount = int(input("Max. Number of parallel runs allowed on this client: "))
        resourceType = input("Type of Resource (tpu, gpu, cpu): ")
        assert resourceType in ['tpu', 'gpu', 'cpu']
        resource = resources.makeResource(resourceType=resourceType, resourceCount=resourceCount)
        if resource == None:
            print("Error in making Resource of type ", resourceType, "Try again later")
            return None
        config = {
            'ip' : ip,
            'port' : port,
            'apiKey' : apiKey,
            'resources' : resource,
            'identifier' : identifier
        }
        f = open(DEFAULT_CONFIG_LOC, 'w')
        f.write(pickle.dumps(config))
        f.close()
        return config 
    return None