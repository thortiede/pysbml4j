class Network(object):
    # this class is the main object the user is working with
    # it gets initialized after a call to sbml4j.getNetwork()
    # a network should hold all the metadata that is available in the networkInventoryItem
    # also it should hold a reference to a parent network (if applicable)
    # all endpoints in the networks category of sbml4j should be available on this class
    # everytime a new network is created due to a REST call (i.e. addCsvData) it should update the current object
    # and keep a reference to the parent network somehow.
    # How exactly this can be done I have to see.
    uuid: str
    name: str
    organismCode: str
    numberOfNodes: int
    numberOfRelations: int
    numberOfReactions: int
    nodeTypes: list
    relationTypes: list
    networkMappingType: str

    sbml4jApi = None
        
    def __init__(self, dict_from_api, api):
        # keep a reference to the api to route calls through
        self.sbml4jApi = api
        #print("Initializing Network instance")
        #print(dict_from_api)
        self.updateInfo(dict_from_api)

    def updateInfo(self, dict_with_info):
        #print("Updating network with info from :\n{}".format(dict_with_info))
        #for key, value in dict_with_info.items():
        self.uuid = dict_with_info['uuid']
        self.name = dict_with_info['name']
        self.organism_code = dict_with_info['organismCode']
        self.numberOfNodes = dict_with_info['numberOfNodes'] if dict_with_info['numberOfNodes'] != None else 0
        try:
            self.numberOfRelations = dict_with_info['numberOfRelations']
        except:
            self.numberOfRelations = 0
        try:
            self.numberOfReactions = dict_with_info['numberOfReactions']
        except:
            self.numberOfReactions = 0

        self.nodeTypes = dict_with_info['nodeTypes']
        self.relationTypes = dict_with_info['relationTypes']
        self.networkMappingType = dict_with_info['networkMappingType']
    
    def getInfoDict(self):
        dict_with_info = {
            'uuid' : self.uuid,
            'name' : self.name,
            'organismCode' : self.organism_code,
            'numberOfNodes' : self.numberOfNodes,
            'numberOfRelations' : self.numberOfRelations,
            'numberOfReactions' : self.numberOfReactions,
            'nodeTypes' : self.nodeTypes,
            'relationTypes' : self.relationTypes,
            'networkMappingType' : self.networkMappingType
        }
        return dict_with_info
    
    def __str__(self):
        return '{}-Network with {} nodes and {} relationships'.format(
            self.networkMappingType, self.numberOfNodes, self.numberOfRelations)
    
    
    ############
    # Retrieve the contents of the network in the GraphML format
    # decodes the output in utf-8 if not overwritten
    def graphML(self, directed=None, coding=None):
        # fire request
        try:
            resp = self.sbml4jApi.getNetworkGraphML(self, directed)
        except Exception as e:
            print(e)
            return None # Do we actually want to break here and terminate execution?
        else:
            if coding == None:
                return resp.decode('utf-8')
            else:
                return resp.decode(coding)
 
    ############
    # Create a copy of a network
    # The network will be identical to the given network
    # except getting a new name and a new uuid
    def copy(self, newNetworkName=None, doPrefixName=False, doSuffixName=None):
        dict_with_new_info = self.sbml4jApi.copyNetwork(self.uuid, newNetworkName, doPrefixName, doSuffixName)
        self.updateInfo(dict_with_new_info)
    
    ############
    # Add Data from a csv file to the network
    # The csv file needs have the gene symbol in the first column
    # all additional columns get added as annotations to the nodes
    # The given dataName will be added as Label to the gene-node and can be used in context searches
    # A name can be given to the resulting network, if ommited the old network name will prefixed with "Added_{dataName}_to_"
    def addCsvData(self, csvFile, dataName, newNetworkName=None, doPrefixName=None, doDerive=None):
        dict_with_new_info = self.sbml4jApi.addCsvDataToNetwork(self.uuid, csvFile, dataName, newNetworkName, doPrefixName, doDerive)
        self.updateInfo(dict_with_new_info)
        
    ############
    # Context
    # POST's a context for a network
    #     Searches the context, persists it as a new network
    #     and updates this Network instance to reflect the new network
    def createContext(self, 
                      geneList, 
                      terminateAt=None, 
                      direction=None, 
                      minSize=None, 
                      maxSize=None, 
                      newNetworkName=None,
                      doPrefixName=None):
        dict_with_new_info = self.sbml4jApi.postContext(self.uuid, geneList, terminateAt, direction, minSize, maxSize, newNetworkName, doPrefixName)
        self.updateInfo(dict_with_new_info)
   
    ############
    # Context
    # There are two ways to generate a context
    # GET's a context from a network
    #     Searches the context and returns it as GraphML, leaving the network unchanged      
    def getContext(self, geneList, terminateAt=None, direction=None, minSize=None, maxSize=None, directed=None, coding=None):
        try:
            resp = self.sbml4jApi.getContext(self.uuid, geneList, terminateAt, direction, minSize, maxSize, directed)
        except Exception as e:
            print(e)
            return None # Do we actually want to break here and terminate execution?
        else:
            if coding == None:
                return resp.decode('utf-8')
            else:
                return resp.decode(coding)
    
    ############
    # Calcualte a shortest path between two given genes
    # This also uses the multi-gene context endpoint
    # which does calculate the shortest path for the two genes
    # and a neighborhood around the genes, whose size can be given.
    # With a size of zero, it results in only the shortest path between the two genes
    # TODO: ADD weight parameter
    def shortestPath(self, gene1, gene2, directed=None, coding=None):
        try:
            resp = self.sbml4jApi.getContext(uuid=self.uuid, geneList=[gene1, gene2], minSize=0, maxSize=0, directed=directed)
        except Exception as e:
            print(e)
            return None # Do we actually want to break here and terminate execution?
        else:
            if coding == None:
                return resp.decode('utf-8')
            else:
                return resp.decode(coding)
    
    def getOptions(self):
        resp = self.sbml4jApi.getNetworkOptions(self.uuid)
        return resp
