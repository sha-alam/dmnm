def color_nodes(graph):
    color_map = {}
    # Consider nodes in descending degree 
    nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
    for node in nodes:
        neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next( color for color in range(len(graph)) if color not in neighbor_colors)
    return color_map
#Adjacent list
graph={'a':list('bcd'),'b': list('ac'),'c': list('abdef'),'d': list('ace'),'e': list('cdf'),'f': list('ce')}
print(color_nodes(graph))