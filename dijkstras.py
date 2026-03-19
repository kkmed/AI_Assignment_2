import pandas as pd
import heapq

def add_edge(adj,origin,destination,distance):
    if adj == {} or origin not in adj:
        adj[origin] = [[destination,distance]]
    else:
        adj[origin].append([destination,distance])

path = []
def backtracking(prev,start):
    path.append(start)
    if prev[start] == 'NULL':
        return
    backtracking(prev,prev[start])


def dijkstra(adj,start,dest):
    distances = {node: float('inf') for node in adj}
    prev = {node: float('inf') for node in adj}
    distances[start] = 0
    prev = {start:'NULL'}
    minheap = [(0,start)]
    while minheap:
          curr_dist,curr_node = heapq.heappop(minheap)
          if curr_dist > distances[curr_node]:
              continue
          for neighbour,weight in adj[curr_node]:
              distance = curr_dist + weight
              if distance < distances[neighbour]:
                  distances[neighbour] = distance
                  prev[neighbour] = curr_node
                  heapq.heappush(minheap,(distance,neighbour))
    backtracking(prev,dest)
    return distances

data = pd.read_csv('indian-cities-dataset.csv')
#print(data.shape) (85,3)
cities = set(list(data['Origin']) + list(data['Destination']))
adj = {}
for city in cities:
    destinations = list(data[data['Origin'] == city]['Destination'])
    distances = list(data[data['Origin'] == city]['Distance'])
    for i in range(len(destinations)):
        add_edge(adj,city,destinations[i],distances[i])

start = input('Enter Start Location:').lower().capitalize()
dest = input('Enter Destination:').lower().capitalize()
distances = dijkstra(adj,start,dest)
print(f'{start} to {dest} : {distances[dest]} kms')
for i in range(len(path) - 1, -1, -1):
    if i == 0:
        print(f'{path[i]}',end='')
    else:
        print(f'{path[i]}->',end='')