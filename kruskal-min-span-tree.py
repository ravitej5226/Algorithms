class Graph(object):
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.edges=edges

class Solution(object):
    def kruskal(self,graph):
        self.parent={}
        self.rank={}

        # Intialize parent and rank
        # Set parent to self and rank to 0
        for v in graph.vertices:
            self.parent[v]=v
            self.rank[v]=0
        
        # Sort the edges based on the weights
        graph.edges=sorted(graph.edges,key=lambda x: x[2])
        result=[]
        # For each edge in graph
        # Check if they belong to same set
        # If not, add them to the same set
        for u,v,w in graph.edges:
            root1=self.find(u)
            root2=self.find(v)
            if(root1!=root2):
                result.append((u,v,w))
                self.union(root1,root2)
                #print(self.parent)

        return result
    
    def find(self,x):
        if(self.parent[x]==x):
            return x
        else:
            return self.find(self.parent[x])
    
    def union(self,u,v):
        if(self.rank[u]>self.rank[v]):
            self.parent[v]=u
        elif(self.rank[u]<self.rank[v]):
            self.parent[u]=v
        else:
            self.parent[v]=u
            self.rank[u]=self.rank[u]+1

s=Solution()
vertices=['A','B','C','D','E','F','G']
edges=[('A','B',7)]
edges.append(('B','C',8))
edges.append(('A','D',5))
edges.append(('B','D',9))
edges.append(('B','E',7))
edges.append(('C','E',5))
edges.append(('D','E',15))
edges.append(('D','F',6))
edges.append(('E','F',8))
edges.append(('E','G',9))
edges.append(('F','G',11))
graph=Graph(vertices,edges)
result=(s.kruskal(graph))
for item in result:
    print('{0} -> {1} = {2}'.format(item[0],item[1],item[2]))