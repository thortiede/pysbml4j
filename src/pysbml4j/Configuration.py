class Configuration(object):
    #_server=None
    #_user=None
    
    def __init__(self, server=None, user=None):
        if server == None:
            self._server = "http://localhost:8080"
        else:
            self._server = server
        self._application_context="/sbml4j"
        #self._user = user
        self._headers = {'Accept':'application/json'}
        if user == None:
            self._headers['user'] = "sbml4j"
        else:
            self._headers["user"] = user
        self._isInSync = False
    @property
    def isInSync(self):
        return self._isInSync
    
    @isInSync.setter
    def isInSync(self, value):
        self._isInSync = value
    
    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server=value
        self._isInSync=False
    
    @property
    def application_context(self):
        return self._application_context
    @application_context.setter
    def application_context(self, value):
        self._application_context = value
        self._isInSync=False
    
    @property
    def user(self):
        return self._headers['user']
    @user.setter
    def user(self, value):
        self._headers['user'] = value
        self._isInSync=False
    
    @property
    def headers(self):
        return self._headers
    
    @property
    def accept(self):
        return self._headers['Accept']
    @accept.setter
    def accept(self, value):
        self._headers['Accept'] = value
        
    #@property
    #def content_type(self):
    #    return self._headers['Content-Type']
    #@content_type.setter
    #def content_type(self, value):
    #    self._headers['Content-Type'] = value
    
    
    def __str__(self):
        return "Server: {}{} with headers: {}".format(self._server, self._application_context, self._headers)
