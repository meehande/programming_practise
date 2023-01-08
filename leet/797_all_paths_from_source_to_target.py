from typing import List



def find_paths(index, target, graph, visited, path, results):
    visited[index] = True
    path.append(index)

    if index == target:
        results.append([el for el in path])
    else:
        for adjacent_index in graph[index]:
            if visited[adjacent_index] == False:
                find_paths(adjacent_index, target, graph, visited, path, results)
    path.pop()
    visited[index] = False


def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    visited = [False for _ in range(target)]
    path = []
    results = []
    find_paths(0, target, graph, visited, path, results)
    return results


