def bfs(tree, node, parent, visited=set()):
	child_nodes = tree[node]
	sum = 0
	if node in visited:
		return 0
	else:
		visited.add(node)

	for child_node in child_nodes:
		if (child_node == parent):
			sum += 1
		else:
			sum += bfs(tree, child_node, node, visited)
	
	return sum

def number_of_friends(A, B):
	tree = dict()
	for item in A:
		items = item.split(":")
		nodes = tree.get(items[0], None)
		if nodes is not None:
			nodes.append(items[1])
		else:
			tree[items[0]] = [items[1]]

		nodes = tree.get(items[1], None)
		if nodes is not None:
			nodes.append(items[0])
		else:
			tree[items[1]] = [items[0]]
	res = []
	for item in B:
		print(item + ": " + str(bfs(tree, item, None)), end=" ")
	print()

def main():
	A = ["Vanja:Sergio", "Sergio:Pedro", "Pedro:Martin", "Martin:Pablo", "Pablo:Sergio", "Jelena:Ivan", "Jelena:Alan", "Alan:Tomislav"]
	B = ["Tomislav", "Martin"]
	number_of_friends(A, B)


if __name__ == "__main__":
	main()
