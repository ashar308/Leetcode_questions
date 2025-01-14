from collections import deque
#Lets do the nodes undirected 1 is connected to2 and 3 and 2 to 1 and 3 and 3 to 2 and 1
graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
}

#bfs -> marking the visited nodes
#1 the start node will be part of the queue
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)
    return result
print(bfs(graph, 1))



#bfs-2
def bfs2(graph,start):
    #declaring a queue
    visited = set()
    q = deque([start])
    result= []
    while q:
        stack = q.popleft()
        #if stack not in visited:
        print("Stack is: ")
        print(stack)
        if stack not in visited:
            visited.add(stack)
            result.append(stack)
            for neighbor in graph[stack]:
                if neighbor not in visited:
                    q.append(neighbor)
    return result
print("BFS-2: ")
print(bfs2(graph, 1))

def bfs_recursive(graph,start):
    q = deque([start])
    result = []
    if q ==None:
        return result
    visited = set()
    stack = q.popleft()
    if stack not in visited:
        visited.add(stack)
        result.append(stack)
        for neighbor in graph[stack]:
            if neighbor not in visited:
                q.append(neighbor)
            
    bfs_recursive(q,start)
print("BFS-3: ")
#print(bfs_recursive(graph, 1))


#breath for search -4
def bfs4(graph,start):
    visited = set()
    q = deque([start])
    print(q)
    result = []
    while q:
        stack = q.popleft()
        print("leftmost stack:", stack)
        
        print("Visited",visited)
        if stack not in visited:
            visited.add(stack)
            print("entered the stack not in visited")
            result.append(stack)
            print("result:",result)
            for child in graph[stack]:
                if child not in visited:
                    q.append(child)
    return result
print("BFS-4: ")
print(bfs4(graph, 1))

def dfs_iterative(graph,start):
    stack = [start]
    visited = set()
    result = []
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.add(tmp)
            result.append(tmp)
            for child in graph[tmp]:
                if child not in visited:
                    stack.append(child)
    return result
print("DFS-4: ")
print(dfs_iterative(graph, 1))
    
#Detecting cycles:
def hascycles(Graph,node,visited,parent):
    

        
    




