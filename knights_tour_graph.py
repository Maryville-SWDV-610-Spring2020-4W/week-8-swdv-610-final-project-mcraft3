#knights_tour_graph.py
"""
SWDV-610-4W 20/SP2 DATA STRUCTURES WK 8
Module 8 Final Project.

WK 8 Final: knights_tour_graph.py

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft"""
# ------------------------------------------------
"""Specified Requirements from Canvas:

Assignment Requirements

At this point in time, you are familiar with all
of the data types and data structures in Python
and can implement them in a variety of ways.  For
your final project, you must make a choice of
which algorithms and data structures can best be
utilized to solve a problem and implement them in
a program. 

You must develop an algorithm and/or data
structure and implement it to solve a problem of
your choosing. For example, you may want to
address the classic Knight's Tour
(https://en.wikipedia.org/wiki/Knight%27s_tour)
problem by implementing a graph utilizing a depth
first search algorithm. In your program, you must
also provide a test case for the algorithm. This
is a fairly open-ended challenge but should
showcase the skills and knowledge you have
acquired over your coursework so far. 

You will be submitting your code as a .py file as
well as a brief video of you explaining what your
program should do and  so it functioning.  You may
reference the rubric to further understand the
parameters for grading.

P.S.  Here is a solution to the Knight's Tour
Problem being run out.  It is not coded since that
could be a legitimate project.  However, you
should see the completion of it and the
algorithmic construction of the solution.
"""
# ------------------------------------------------
"""GitHub Submission Instructions:
Once you complete these exercises, be sure you
have committed your solutions locally and pushed
them up to the remote repository. If you are
unsure how to clone the repository for this
assignment, please review Pull and Push for
Assignments. 

Note: If you are utilizing any additional
packages, these need to be submitted as well.

GitHub Link:
https://classroom.github.com/a/tCOU_nlT"""
# ------------------------------------------------
"""Canvas Submission Instructions:

When you have completed this assignment and pushed
your work to the remote GitHub repository, please
upload your video file to Canvas."""
# ------------------------------------------------
"""Final Project Rubric

1. Functionality - Program completes its set
   purpose.
2. Video Walthrough - Clearly explains code and
   demonstrates its functionality.
3. Readability - Code is readable and clearly
   commented and organized.
4. Problem Set - Problem chose for program to
   solve fits under the submission guidelines.
5. Data Structure Implementation - Data Structures
   are clearly references and articulated what
   they are and how they will be utilized.
"""
# ------------------------------------------------

from adj_list_graph import Graph
import time

# ------------------------------------------------
"""This program will demonstrate completion of the
Knight's Tour using a Depth First Search (DFS)
General Search algorithm. This will initially run
a single search from a selected start vertex, and
can then be set to run multiple searches from a
consective group of vertices or the entire list of
64 including from 0 to 63 vertices. Searches can
then be expanded for additional search end
vertices by using alternative moveOffset lists
for the 2 to 8 moves from any position on the
board.

Main calls buildKnightGraph function (utilizes
DFSGraph sub class and base class Graph from
adjacency list graph) to build the graph for an
n-by-n board, in this scenario an 8 x 8 is
used. BuildKnightGraph calls two helper functions:
posToNodeId and genLegalMoves (genLegalMoves is
further helped by legalCoord).

Main then calls dfs to initiate and schedule the
start of the dfs search by calling dfsvisit that
actually executes the search, and further
recursions of the search are to dfsvisit."""
# ------------------------------------------------
def buildKnightGraph(bdSize):
    ktGraph = DFSGraph()                                  # use for knightGraph with DFS
    for row in range(bdSize):                             # 8 total, row of 0 to 7
        for col in range(bdSize):                         # 8 total, column of 0 to 7
            nodeId = posToNodeId(row,col,bdSize)          # vertex ID, coord
            newPositions = genLegalMoves(row,col,bdSize)  # vertex connected/neighbors list
            for e in newPositions:                        # loop for connected in connected list
                nid = posToNodeId(e[0],e[1],bdSize)       # gen ID
                ktGraph.addEdge(nodeId,nid)               # add vertex, add edge
    return ktGraph                                        # returns built graph with vertices and edges to main
                                                          # so you can then run the search from main
# ------------------------------------------------
"""posToNodeId is a helper function to
buildKnightsGraph converts a location on the board
in terms of a row and a column into a linear
vertex number."""
def posToNodeId(row, column, board_size):                 # converts position to vertex coord
    return (row * board_size) + column

# ------------------------------------------------
"""genLegalMoves is a helper function called by
buildKnightGraph. At each square on the board,
buildKnightGraph calls genLegalMoves to create a
list of legal moves for that position on the
board. All legal moves are then converted into
edges in the graph."""
def genLegalMoves(x,y,bdSize):                            # generate 2 to 8 edges/moves
    newMoves = []                                         # edgelist
   
    # newX and newY define next move of Knight.  
    # newX is for next value of x coordinate; 2 is down, -2 is up 
    # newY is for next value of y coordinate; 1 is to right, -1 is to left   
    
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),         # original search order
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]      

    # Samples of alternative Search Patterns to acheive added searches with different Tours/End Vertices.
    
    #moveOffsets = [(2,1), (1,2), (-1,2), (-2,1),       # CW1      # if automated to 8 factorial, may provide
    #               (-2,-1), (-1,-2), (1,-2), (2,-1)]              # simple means for over 40,000 searches x 64 vertices
                                                                   # for over 2.5 Million searches.
    #moveOffsets = [(-2,-1), (-1,-2), (1,-2), (2,-1),   # CW2
    #               (2,1), (1,2), (-1,2), (-2,1)]       
    
    #moveOffsets = [(2,-1), (1,-2), (-1,-2), (-2,-1),   # CCW3
    #               (-2,1), (-1,2), (1,2), (2,1)]        
  
    #moveOffsets = [(-2,1), (-1,2), (1,2), (2,1),       # CCW4
    #               (2,-1), (1,-2), (-1,-2), (-2,-1)]   
    
    for i in moveOffsets:
        newX = x + i[0] 
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY))# add edge
    return newMoves # edgelist

# ------------------------------------------------
"""legalCoord is a helper function for
genLegalMoves, and makes sure that a particular
move generated is still on the board."""
def legalCoord(x,bdSize): # ensure still on board
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

# ------------------------------------------------
# Depth First Search (DFS) General Search.
# Searches as deep as possible.
# Extends Graph class adds time tracker, discovery 
# and finish. Adds methods dfs and dfsvisit.
class DFSGraph(Graph):
# ------subclass constructor----------------------
    def __init__(self):
        super().__init__()
        # tracks time across calls                
        self.time = 0
            
# ---------subclass methods-----------------------
    # dfs initiates, schedules DFS search.
    # Calls dfsvisit that executes the search
    # including recursions of dfsvisit.
    def dfs(self, pathDFS, start):
        # iterates over all vertices in the graph
        # ensures all nodes in graph are
        # considered and no vertices are left out
        # of the depth first forest.
        # iterave over DFSGraph or self.                
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':       # if vertice white, not visited, schedule visit, call dfsvisit  
                self.dfsvisit(start, pathDFS)       # provides different start vertex, passed from dfs from main                
        return pathDFS

# ------------------------------------------------
    # Executes search. Uses colors: White
    # unvisited, gray exploring, black complete.
    def dfsvisit(self,startVertex, pathDFS):
        
        # starts with single vertex and explores
        # all of the neighboring white vertices
        # as deeply as possible.
        startVertex.setColor('gray')                     # set gray, being explored
        self.time += 1                                   # increment time tracker
        startVertex.setDiscovery(self.time)              # start discovery tracker
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':         # if white explore, if black done
                nextVertex.setPred(startVertex)          # set predecessor
                self.dfsvisit(nextVertex, pathDFS)       # call next explore, recursive (uses implicit stack)
                                                         # backtracks/moves over to nextVertex in connectedTo/neighbors
        startVertex.setColor('black')                    # set/paint black, complete; backtrack and paint black as you come out.
        self.time += 1                                   # increment time for current vertex
        startVertex.setFinish(self.time)                 # sets finish for start vertex        
                                            
        # prints reverse order of predecessors (path back to start; reverse it)
        # prints path vertex and their connectedTo/neighbors list; can toggle/comment off
        print(startVertex, "\n     Discovery Time:", startVertex.getDiscovery(), "Finish Time:", startVertex.getFinish(), "\n")   
        
        # provides means to print path
        # will be in reverse order of predecessors
        # (path back to start; reverse it)
        # appends key to path        
        pathDFS.append(startVertex.getID()) # adds key or vertex to path list to return to main for print
        return pathDFS

# ------------------------------------------------
def main():
    # Build the Graph
# ------------------------------------------------
    pathDFSkt = []                               # initialize DFS path to empty list
    x = 8                                        # initialize local variable to x for boardsize/graph row/column size
    ktGraph = buildKnightGraph(x)                # Calls knightGraph to build graph(size x) (8 for 8 * 8 chessboard)
                                                 # knightsGraph will use DFSGraph sub class and base class Graph.
                                                 # This builds the graph, with vertices and connections/neighbors
    
    print("Nodes/Vertices in order prior to search, with connections:\n") # Pre-Order Traverse of vertices and edges.
    for i in range(ktGraph.get_numVertices()):                            # loops through size of graph / number of vertices
        print(ktGraph.getVertex(i))              # prints DFS Graph vertices using vertex __str__ with connections/neighbors
    print()
    
# ------------------------------------------------
    # Run the Search and get Results
    
    t0=time.time()                               # clock look to start time of search
    
    ######## This print line used for single search to print the vertex path out with connectedTo/neighbors list########
    ######## Toggle single search on 270,286,235 all on ######## while 272,273,274 all off (used to print all 64 searches)########
    ######## Set line 276 to range (0,1) to search vertice 0; set to (1,2) to search vertice 1, or (0,64) to search all 64.
    
    ######## Toggle multi search on 272,273,274, and toggle/comment out 270,286,235 ########
    
    print("DFS Path Results (reverse to start) with neighbors/connections, Discovery and Finish Times:\n")
    
    #print("--------------------------------------------------")
    #print("\nKnight's Tour search results using DFS General Search for multiples vertices between 0 to 63:\n")
    #print("--------------------------------------------------")
    
    for vertex in range(0, 1): # set to 0,64 to see all 64 outputs; 0,1 to see with start 0; 1,2 to see with start 1.
        pathDFSkt = []
        
        # Call to DFS with parameters: Path, and Start Vertex.
        pathDFSoutkt = ktGraph.dfs(pathDFSkt, ktGraph.getVertex(vertex))
        
        print("Using start vertex:", vertex)                                      # Display start vertex for search
        print()
        print("Length of DFS Path:", len(pathDFSkt))                              # computes and prints length of returned path
        
        print("\nDFS returned path from finish to start:", pathDFSoutkt)          ######## can toggle off to print list of 64 runs

        pathDFSoutReversedkt = []                                                 # initializes emtpy list to reverse
        for i in range(len(pathDFSkt)-1, -1, -1):                                 # loops through returned list in reverse order
            pathDFSoutReversedkt.append(pathDFSkt[i])                             # saves to reverse list
        print("\nDFS returned path from start to finish:", pathDFSoutReversedkt)  # prints reversed list
        
        t1 = time.time()                                                          # Clock look to stop search time
        print("\ntotal: {:0.6f} seconds".format(t1-t0))                           # Calculate search time
        print("--------------------------------------------------")
    
# ------------------------------------------------
    """Note: Additional DFS path end points can be achieved by going up to knightsGraph, and toggling to
    use of a different moveOffsets group, that will change the order of look for the 2 to 8 neighbor moves
    for each position. It does not change the neighbor list, but does alter the order that they are looked
    at and provides a different end point that are complete tours, open or closed."""
# ------------------------------------------------
    
main()