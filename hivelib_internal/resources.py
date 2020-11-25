from abc import ABC, abstractmethod 

class ResourceManager():
    resourceType = None
    resourceCount = None
    resources = []
    freeQueue = []

    def __init__(self, **kwargs):
        self.freeQueue = list(self.resources)

    def getAvailable(self):
        return self.freeQueue
    
    def allocate(self):
        res = self.freeQueue.pop()
        return res

    def free(self, resource):
        self.freeQueue.append(res)

    def checkVitals(self):
        pass 

    def to_dict(self):
        pass
    
    
class TPUResourceManager(ResourceManager):
    def __init__(self, resourceCount=5, **kwargs):
        print("Initializing TPU Resource Manager...")
        if resourceCount == None or resourceCount == 0:
            resourceCount = int(input("\tPlease enter the number of TPUs available to this client: "))
            assert resourceCount != 0
        self.resourceCount=resourceCount
        print("You would be required to Enter the names and zones of each TPU-->")
        tpus = []
        for r in range(resourceCount):
            name = input('\tName of TPU #'+r)
            zone = input('\tZone for the TPU (default: europe-west4-a)')
            if zone == '' or zone == '\n':
                zone = 'europe-west4-a'
            tpus.append({
                'name':name,
                'zone':zone,
            })
        self.resources = tpus 

        super(TPUResourceManager).__init__(**kwargs)

    def checkVitals(self):
        pass