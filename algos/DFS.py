from algos import pathFinder
class DFSPathFinder(pathFinder.AbstractPathFinder):
    path = []
    visited = []
    def __init__(self, starting: tuple, ending: tuple, *obstacles: list):
        self.starting = starting
        self.ending = ending
        self.obstacles = obstacles

    # This method finds the optimal path
    def findPath(self) -> list:
        self.dfs(self.starting)
        return self.path
        
    #This method performs the Depth First Search 
    def dfs(self, node:tuple):
        self.addNode(node,self.path)
        self.addNode(node,self.visited)
        if node != self.ending:
            validAdjNodes = self.validAdjacents(node)
            if len(validAdjNodes) != 0:
                self.moveToAdjacentNodes(validAdjNodes)
            else: 
                self.backTrack(node)
        return
    
    # This method adds the given node,if it is not in the given list
    def addNode(self,node:tuple, nodesList:list):  
        if node not in nodesList:
            nodesList.append(node)
    
    # This method will gives the valid adjacent nodes of the given node
    def validAdjacents(self,node: tuple) -> list:
        validAdjList = []
        adjNodes = self.AdjacentNodes(node)
        for n in adjNodes:
            if self.isValid(n):
                validAdjList.append(n)
        return validAdjList
    
    # This method will traverse the given nodes
    def moveToAdjacentNodes(self,nodes:list):
        for n in nodes:
            self.dfs(n)
            
    # This method will backtrack from the current node
    def backTrack(self,node: tuple): 
        path.remove(node)
        
    # This method returns the list of adjacent nodes for the given node
    def AdjacentNodes(self,node:tuple)->list:
        x,y = node[0],node[1]
        rNode = (x+1,y)
        lNode = (x-1,y)
        bNode = (x,y+1)
        tNode = (x,y-1)
        return [rNode,lNode,bNode,tNode]
    
    # This method checks whether the given node is a valid node
    def isValid(self,node:tuple) -> bool:
        if (self.inGrid(node) and not (self.inObstacle(node)) and (node not in self.visited)):
            return True
        return False
    
    # This method returns whether given node is present within the grid range 
    def inGrid(self,node:tuple)->bool:
        return (1 <= node[0] <= 8) and (1 <= node[1] <= 8)

    # This method returns whether given node is present in obstacles 
    def inObstacle(self,node:tuple)->bool:
        for obstacle in self.obstacles:
            if node in obstacle:
                return True
        return False
