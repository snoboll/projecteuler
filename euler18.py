#euler 18
edgelist = sort(edgelist(lambda = x: int(x.weight))

N = 4
nodelist = list(range(N))

class Edge:
	def __init__(self,node_a, node_b, weight):
		self.node_a = node_a
		self.node_b = node_b
		self.weight = weight
	
e1 = Edge(1,2,1)
e2 = Edge(2,3,4)
e3 = Edge(1,3,3)
e4 = Edge(3,4,5)

edgelist = [e1,e2,e3,e4]
	
edgelist.sort(key=lambda x: int(x.weight))
