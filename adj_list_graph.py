# adj_list_graph.py

# ------------------------------------------------
"""Provides a class for Graph using an Adjacency
List Graph, and a class for Vertex. 

Adjacency List keeps a dictionary (self.vertList)
of all vertices in the Graph object.

Each Vertex object in the graph maintains a
dictonary (self.connectedTo) of the other vertices
or neighbors it is connected to.

Vertex class supports use of distance,
predecessors, discovery and finish."""
# ------------------------------------------------
import sys # used by Vertex to set maxsize

# ------------------------------------------------
class Graph:
    
    #--------class constructor--------------------    
    def __init__(self):
        # dictionary that maps vertex names to
        # vertex objects; initialize
        self.vertList = {}
        self.numVertices = 0
    #--------class accessors----------------------
    def get_numVertices(self):
        return self.numVertices
    
    def __contains__(self,n):
        return n in self.vertList
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None        
    
    # return names of all vertices in graph.
    # Together with iter, allows you to iterate
    # over vertices in graph by name, or by the
    # objects themselves.
    def getVertices(self):
        return list(self.vertList.keys())
    
    # makes it easy to iterate over all vertex
    # objects in graph
    def __iter__(self):
        return iter(self.vertList.values())
                
    #--------class methods------------------------
    # add vertices to graph and connecting one  
    # vertex to another.
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        
        # list of vertices
        self.vertList[key] = newVertex 
        return newVertex
    
    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],weight)

# ------------------------------------------------    
class Vertex:
    """Extended Vertex Class, adds instance
    Variables: distance, predecessor and color and
    full set of getter and setter methods."""
    
    #--------class constructor--------------------    
    def __init__(self,key):
        self.id = key # initialize id with key
        
        # dictionary to track vertex is connectedTo 
        # what vertices
        self.connectedTo = {} # initialize dictionary
        self.color = 'white'    # color
        self.dist = sys.maxsize # distance
        self.pred = None        # predecessor
        
        # Discovery Time; tracks number of steps
        # in algorithm before a vertex is first
        # encountered, supports parenthesis property.
        self.disc = 0
        
        # Finish Time: tracks number of steps in
        # algorithm before a vertex is colored
        # black, support parenthesis property.
        self.fin = 0
    
    #--------class accessors----------------------
    def getID(self,):
        return self.id
    
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    # returns all vertices in the adjacency list, connectedTo
    def getConnections(self):
        return self.connectedTo.keys()
        
    # returns the weight of edge from this vertex to
    # the vertex passed as a parameter
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo]) 
        
    #--------class methods------------------------
    # add a connection from this vertex to another
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime

# ------------------------------------------------
