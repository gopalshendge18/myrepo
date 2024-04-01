def create_graph(adj_matrix, input_array):
    for edge in input_array:
        adj_matrix[edge[0]][edge[1]] = 1
        adj_matrix[edge[1]][edge[0]] = 1

def dfs(adj_matrix, visited, start_node):
    visited[start_node] = True
    print(start_node, end=" ")
    for i in range(len(adj_matrix) - 1, -1, -1):
        if adj_matrix[start_node][i] == 1 and not visited[i]:
            dfs(adj_matrix, visited, i)

if __name__ == "__main__":
    adj_matrix = [[0] * 10 for _ in range(10)]
    visited = [False] * 10
    input_array = [
        [1, 2],
        [1, 3],
        [8, 3],
        [4, 5],
        [4, 6],
        [6, 7]
    ]

    create_graph(adj_matrix, input_array)

    for i in range(10):
        if not visited[i]:
            print()
            dfs(adj_matrix, visited, i)
