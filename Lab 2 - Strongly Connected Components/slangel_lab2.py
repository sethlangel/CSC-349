import sys

class node:

	def __init__(self,name,out_edges,in_edges,previsit, postvisit,component):
		self.name = name
		self.out_edges = out_edges
		self.in_edges = in_edges
		self.previsit = previsit
		self.postvisit = postvisit
		self.component = component

def strong_connectivity(G):
	def dfs(vertex, visited, stack):
		visited.add(vertex)

		for neighbor in G[vertex].out_edges:
			if neighbor not in visited:
				dfs(neighbor, visited, stack)
		stack.append(vertex)

	def fill_stack(G):
		visited = set()
		stack = []
		for vertex in G:
			if vertex.name not in visited:
				dfs(vertex.name, visited, stack)
		
		return stack

	def reverse_graph(G):
		new_graph = [node(n.name, [], [], -1, -1, None) for n in G]

		for vertex in G:
			for neighbor in vertex.out_edges:
				new_graph[neighbor].out_edges.append(vertex.name)
		
		return new_graph
	
	def find_comp(vertex, visited, comp):
		visited.add(vertex)
		comp.append(vertex)

		for neighbor in reversed_graph[vertex].out_edges:
			if neighbor not in visited:
				find_comp(neighbor, visited, comp)
			
	stack = fill_stack(G)
	reversed_graph = reverse_graph(G)
	visited = set()
	components = []

	while stack:
		vertex = stack.pop()

		if vertex not in visited:
			comp = []
			find_comp(vertex, visited, comp)
			components.append(comp)

	
	print(components)

	sort_component_list(components)
	return components

def sort_component_list(components):
	for c in components:
		c.sort()
	components.sort(key = lambda x: x[0])

def read_file(filename):
	with open(filename) as f:
		lines = f.readlines()
		v = int(lines[0])
		if  v == 0:
			raise ValueError("Graph must have one or more vertices")
		G = list(node(name = i, out_edges=[],in_edges=[],previsit= -1, postvisit=-1, component=None) for i in range(v))
		for l in lines[1:]:
			tokens = l.split(",")
			fromVertex,toVertex = (int(tokens[0]),int(tokens[1]))
			G[fromVertex].out_edges.append(toVertex)
			G[toVertex].in_edges.append(fromVertex)
		return G


def main():
	filename = sys.argv[1]
	G = read_file(filename)
	components = strong_connectivity(G)
	print(components)
		
		
if __name__ == '__main__':
	main()
