import requests
import os 
import json 

class MindApi():
    def __init__(self, ip, port, apiKey, identifier):
        self.ip = ip 
        self.port = port
        self.apiKey = apiKey 
        self.url = 'http://'+self.ip+':'+str(self.port)
        self.identifier = identifier
        pass 

    def fetchExperiment(self, resource=None):
        response = requests.post(url=self.url + '/api/fetchExperiment', data={
            'resource' : {
                'global':self.identifier,
                'local':resource
            },
            'apiKey' : self.apiKey
        })
        if response.status_code == 200:
            result = json.loads(response.text)
            return result['experiment'], result['status']
        return None, -1

    def setExperimentWandb(experimentId, wandbId):
        response = requests.post(url=self.url + '/api/setExperimentWandb', data={
            'apiKey' : self.apiKey,
            'experimentId' : experimentId,
            'wandbId' : wandbId 
        })

        if response.status_code == 200:
            result = json.loads(response.text)
            return result['status']
        return None
    
    def concludeExperiment(experimentId, results, status):
        response = requests.post(url=self.url + '/api/concludeExperiment', data={
            'apiKey' : self.apiKey,
            'experimentalId' : experimentId,
            'results' : results,
            'status' : status,
        })
        if response.status_code == 200:
            result = json.loads(response.text)
            return result['status']
        return None
