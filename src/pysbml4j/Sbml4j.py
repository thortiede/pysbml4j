import os
import json

from .Configuration import Configuration
from .Network import Network

from urllib3 import PoolManager
from urllib3 import Timeout
from urllib3 import Retry
from urllib.parse import urlencode

class Sbml4j(object):
    _configuration : Configuration
    _networkList : [Network]
    _shortUuidToNetworkMap : {}
    _nameToNetworkMap: {}
    _pm : PoolManager
    
    def __init__(self, configuration=None):
        self._pm = PoolManager(
        timeout=Timeout(connect=1.0),
        retries=Retry(1, redirect=0))
        if configuration == None:
            self._configuration = Configuration()
        else:
            self._configuration = configuration
        self.refreshNetworkList()
        self._configuration.isInSync = True
        
        
    @property
    def configuration(self):
        return self._configuration
    @configuration.setter
    def configuration(self, configuration):
        self._configuration = configuration
    
    @property
    def user(self):
        return self._configuration.user
    @user.setter
    def user(self, value):
        print("Setting user to {}".format(value))
        self._configuration.user = value
    
    @property
    def networkMap(self):
        return self._shortUuidToNetworkMap
    
    @property
    def nameToNetworkMap(self):
        return self._nameToNetworkMap
    
    #@property
    #def networkList(self):
    #    return self._networkList
    
    def refreshNetworkList(self):
        self._networkList = self.generateNetworkList()
        self._shortUuidToNetworkMap = self.generateNetworkMap('uuid')
        self._nameToNetworkMap = self.generateNetworkMap('name')
    
    def checkSyncStatus(self):
        if not self._configuration.isInSync:
            #print("Configuration out of sync. Refreshing network list.")
            self.refreshNetworkList()
            self._configuration.isInSync = True
    
    ######################################## SBML methods #####################################################
    
    def uploadSBML(self, sbmlFiles, organism, datasource, datasourceVersion):
        self.checkSyncStatus()
        baseUrl = "{}{}/sbml?".format(
                    self._configuration.server, 
                    self._configuration.application_context)
        # required arguments
        args_dict = {'organism': organism, 'source': datasource, 'version': datasourceVersion}
       
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        print(urlString)
         
        if isinstance(sbmlFiles, list):
            files_dict = {}
            for file in sbmlFiles:
                with open(file) as sbml:
                    response = self._pm.request(
                        "POST",
                        urlString,
                        fields={
                            'files': (os.path.basename(sbml.name), sbml.read())
                        },
                        headers = self._configuration.headers
                    )
                    if response.status > 399:
                        if not 'reason' in response.headers.keys():
                            raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
                        else:
                            raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
                    else:
                        pathwayInventoryItemList = json.loads(response.data.decode('utf-8'))
                        print(pathwayInventoryItemList)
        return pathwayInventoryItemList
 

    ######################################## Pathway methods #####################################################

    def pathwayList(self, hideCollections=None):
        baseUrl = "{}{}/pathways".format(
                    self._configuration.server, 
                    self._configuration.application_context)
        if hideCollections != None and (hideCollections == True or hideCollections == False):
            urlString = baseUrl + "?hideCollections=" + hideCollections
        else:
            urlString = baseUrl
        
        response = self._pm.request("GET", urlString,
                                   headers=self._configuration.headers)
        
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data)

        
    def pathwayUUIDs(self, hideCollections=None):
        baseUrl = "{}{}/pathwayUUIDs".format(
                    self._configuration.server, 
                    self._configuration.application_context)
        
        if hideCollections != None:
            if hideCollections == True:
                urlString = baseUrl + "?hideCollections=True"
            elif hideCollections == False:
                urlString = baseUrl + "?hideCollections=False"
            else:
                raise Exception("Parameter hideCollections needs to be either True or False, or omitted. You provided:{}".format(hideCollections))
        else:
            urlString = baseUrl
        
        response = self._pm.request("GET", urlString,
                                   headers=self._configuration.headers)
        
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data)

    def createPathwayCollection(self, collectionName, collectionDesc, pathways):
        baseUrl = "{}{}/pathwayCollection".format(
                    self._configuration.server, 
                    self._configuration.application_context)
        if not isinstance(pathways, list):
            raise Exception("parameter pathways must be of type list (of pathwayUUID-Strings), found {}".format (type(pathways)))
        else:
            data = {'name': collectionName,
                    'description': collectionDesc,
                    'sourcePathwayUUIDs': pathways}
            encoded_data = json.dumps(data).encode('utf-8')
        
        headers_dict = self._configuration.headers
        # our content does not get recognized as json, so we set the header explicitly
        headers_dict['Content-Type'] = 'application/json'
        #print("Headers for postContext: {}".format(headers_dict))
        
        # send the request
        response = self._pm.request(
            "POST",
            baseUrl,
            body=encoded_data,
            headers=headers_dict
        )
        # reset the header as other requests cannot set it themselves otherwise
        del headers_dict['Content-Type']
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error while creating pathwayCollection resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not create pathwayCollection. Reason: {}".format(response.headers['reason']))
        else:
            return response.data.decode('utf-8')
        
    def mapPathway(self, pathwayUUID, mappingType, networkname=None, doPrefixName=None, doSuffixName=None):
        baseUrl = "{}{}/mapping/{}?".format(
            self._configuration.server,
            self._configuration.application_context,
            pathwayUUID)
            
        # required arguments
        args_dict = {'mappingType': mappingType}
        # optional arguments
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if doSuffixName != None:
            args_dict['suffixName'] = doSuffixName
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        # send the request
        response = self._pm.request(
            "POST",
            urlString,
            headers=self._configuration.headers
        )
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error mapping Pathway: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not map Pathway. Reason: {}".format(response.headers['reason']))
        else:
            self._configuration.isInSync=False
            return json.loads(response.data.decode('utf-8'))
            
    ######################################## Network methods #####################################################
    def addNetwork(self, value):
        if isinstance(value, Network):
            self._networkList.append(value)
            self._shortUuidToNetworkMap[value.uuid[:8]] = value
            self._nameToNetworkMap[value.name] = value
        elif isinstance(value, list):
            for elem in value:
                self.addNetwork(elem)
        elif isinstance(value, dict):
            newNetwork = Network(value, self)
            self.addNetwork(newNetwork)
        else:
            raise Exception("Cannot add {} to list of networks.\n Expected type Network or dict of a network or list of Network entities or list of dicts of networks, found {}".format(value, type(value)))
    
    def generateNetworkList(self):
        #print("Fetching available networks..")
        return [Network(netInvItem, self) for netInvItem in json.loads(self.retrieveNetworkList().data)]
    
    def generateNetworkMap(self, key):
        #print("Populating network map for {}".format(key))
        localMap = {}
        for netItem in self._networkList:
            if (key=="uuid"):
                localMap[netItem.uuid[:8]] = netItem 
            elif (key=="name"):
                localMap[netItem.name] = netItem
        return localMap
    
    def retrieveNetworkList(self):
        response = self._pm.request("GET", "{}{}/networks".format(
            self._configuration.server, 
            self._configuration.application_context), 
            headers = self._configuration.headers)
        return response
    
    def listNetworks(self):
        #for shortId, net in self._shortUuidToNetworkMap.items():
        #    print("{}: {}".format(shortId, net))
        self.checkSyncStatus()
        for name, net in self._nameToNetworkMap.items():
            print("{}: {}".format(name, net))
        
    def getNetwork(self, uuid):
        self.checkSyncStatus()
        print("Getting network with id {}".format(uuid))
        networkInfoDict = self._shortUuidToNetworkMap[uuid[:8]].getInfoDict()
        return Network(networkInfoDict, self)
    
    def getNetworkByName(self, name):
        self.checkSyncStatus()
        #print("Getting network with name {}".format(name))
        networkInfoDict = self._nameToNetworkMap[name].getInfoDict()
        return Network(networkInfoDict, self)   
    
    def copyNetwork(self, uuid, newNetworkName=None, doPrefixName=None, doSuffixName=None):
        self.checkSyncStatus()
        #print("Headers for copy Request: {}".format(self._configuration.headers))
        baseUrl = "{}{}/networks?".format(
                    self._configuration.server, 
                    self._configuration.application_context)
        
        # required arguments
        args_dict = {'parentUUID': uuid}
        # optional arguments
        if newNetworkName != None:
            args_dict['networkname'] = newNetworkName
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if doSuffixName != None:
            args_dict['suffixName'] = doSuffixName
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        
        response = self._pm.request("POST",
                                    urlString,
                                    headers = self._configuration.headers)
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
        else:
            #print (json.loads(response.data.decode("utf-8")))
            copiedNetworkDict = json.loads(response.data.decode("utf-8"))
            self.addNetwork(copiedNetworkDict)
            return copiedNetworkDict
       
    def addCsvDataToNetwork(self, uuid, csvFile, dataName, newNetworkName=None, doPrefixName=None, doDerive=None):
        self.checkSyncStatus()
        #prior_content_type = self._configuration.content_type
        #self._configuration.content_type = 'multipart/form-data'
        print("Request headers: {}".format(self._configuration.headers))
        # build the url
        baseUrl = "{}{}/networks/{}/csv?".format(
                    self._configuration.server, 
                    self._configuration.application_context,
                    uuid)
        # required arguments
        args_dict = {'type': dataName}
        # optional arguments
        if newNetworkName != None:
            args_dict['networkname'] = newNetworkName
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if doDerive != None:
            args_dict['derive'] = doDerive
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        print(urlString)
        with open(csvFile) as fp:
            file_data = fp.read()
           
        response = self._pm.request(
            "POST",
            urlString,
            fields={
                'data': (csvFile, file_data)
            },
            headers = self._configuration.headers
        )
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
        else:
            csvNetworkDict = json.loads(response.data.decode('utf-8'))
            self.addNetwork(csvNetworkDict)
            return csvNetworkDict

        
    # TODO: ADD weight parameter
    def getContext(self, 
                   uuid, 
                   geneList, 
                   terminateAt=None, 
                   direction=None, 
                   minSize=None, 
                   maxSize=None, 
                   directed=None):
        self.checkSyncStatus()
        prior_accept = self._configuration.accept
        self._configuration.accept = "application/octet-stream"
        #print("maxSize is: {}".format(maxSize))
        urlString = "{}{}/networks/{}/context".format(
                    self._configuration.server, 
                    self._configuration.application_context,
                    uuid)
        fieldsDict = {}
        
        # geneList must be list object
        if not isinstance(geneList, list):
            raise Exception("parameter geneList must be of type list, found {}".format (type(geneList)))
        else:
            fieldsDict['genes'] = ", ".join(geneList)
        if minSize != None:
            fieldsDict['minSize'] = minSize
        if maxSize != None:
            fieldsDict['maxSize'] = maxSize
        if terminateAt != None:
            fieldsDict['terminateAt'] = terminateAt
        if direction != None:
            fieldsDict['direction'] = direction
        if directed != None:
            fieldsDict['directed'] = directed
        
        response = self._pm.request(
            "GET",
            urlString,
            fields=fieldsDict,
            headers=self._configuration.headers
        )
        # reset the accept header to the state before this request
        self._configuration.accept = prior_accept
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return response.data
        
    # TODO: ADD weight parameter
    def postContext(self, 
                    uuid, 
                    geneList,  
                    terminateAt=None,  
                    direction=None,
                    minSize=None, 
                    maxSize=None, 
                    newNetworkName=None, 
                    doPrefixName=None):
        self.checkSyncStatus()
        baseUrl = "{}{}/networks/{}/context".format(
                    self._configuration.server, 
                    self._configuration.application_context,
                    uuid
                    )
        
        # no required arguments
        
        args_dict = {}
        # optional arguments
        if minSize != None:
            args_dict['minSize'] = minSize
        if maxSize != None:
            args_dict['maxSize'] = maxSize
        if terminateAt != None:
            args_dict['terminateAt'] = terminateAt
        if direction != None:
            args_dict['direction'] = direction
        if newNetworkName != None:
            args_dict['networkname'] = newNetworkName
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        
        if len(args_dict) > 0:
            baseUrl += "?"
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        print(urlString)
        # request body
        # geneList must be list object
        if not isinstance(geneList, list):
            raise Exception("parameter geneList must be of type list, found {}".format (type(geneList)))
        else:
            data = {'genes': geneList}
            encoded_data = json.dumps(data).encode('utf-8')
        
        headers_dict = self._configuration.headers
        # our content does not get recognized as json, so we set the header explicitly
        headers_dict['Content-Type'] = 'application/json'
        print("Headers for postContext: {}".format(headers_dict))
        
        # send the request
        response = self._pm.request(
            "POST",
            urlString,
            body=encoded_data,
            headers=headers_dict
        )
        # reset the header as other requests cannot set it themselves otherwise
        del headers_dict['Content-Type']
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            contextNetworkDict = json.loads(response.data.decode('utf-8'))
            self.addNetwork(contextNetworkDict)
            return contextNetworkDict  
            
            
    def getNetworkGraphML(self, network, directed=None):
        self.checkSyncStatus()
        baseUrl = "{}{}/networks/{}".format(
                    self._configuration.server, 
                    self._configuration.application_context,
                    network.uuid)
        if directed != None:
            urlString = baseUrl + "?directed={}".format(directed)
        else:
            urlString = baseUrl
        
        prior_accept = self._configuration.accept
        self._configuration.accept = "application/octet-stream"
                                    
        response = self._pm.request("GET", urlString,
                                    headers = self._configuration.headers)
        
        # reset the accept header to the state before this request
        print("Previous accept is: {}".format(prior_accept))
        self._configuration.accept = prior_accept
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return response.data
        
        
    def getNetworkOptions(self, uuid):
        self.checkSyncStatus()
        baseUrl = "{}{}/networks/{}/options".format(
                    self._configuration.server, 
                    self._configuration.application_context,
                    uuid)
        
        response = self._pm.request("GET", baseUrl,
                                   headers = self._configuration.headers)
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode("utf-8"))
    
    def filterNetwork(self, uuid, filterOptions):
        # TODO: implement
        return None
        
    def annotateNetwork(self, uuid, annotationObject):
        # TODO: implement
        return None
