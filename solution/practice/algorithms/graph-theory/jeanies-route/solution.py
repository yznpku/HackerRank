# Welp. I had tried my best, but this challenge needs so many steps 
# and thus is quite verbose to write. I will try to make myself clear.
#
# First we notice that the edges used are always the same no matter
# where we start or finish. These paths form a subtree of the original
# graph (which is the smallest subtree containing all the delivery cities).
#
# When we start and finish at the same city, the total distance is always
# twice of the sum of all paths in the said subtree. And when we start
# and finish in different cities, the distance should subtract the path
# between these two cities. Thus we must maximize the distance between
# the starting city and the finishing city.
#
# Using Dfs will greatly simplify the code. But the N seems too huge to
# do the recursion properly. Maybe next time.
#
# So here's what to do:
# 1. Find the said subtree
# 2. Find the longest path in it
# 3. Do the subtraction
#
# Time complexity: O(N)

from collections import deque
N, K = map(int, input().split())
paths = [[] for i in range(N)]
delivery = set(map(lambda x: int(x) - 1, input().split()))
for i in range(N - 1):
  frm, to, d = map(int, input().split())
  paths[frm - 1].append((to - 1, d))
  paths[to - 1].append((frm - 1, d))
# pick one delivery city as the root and construct a tree
parent = [-1] * N
root = next(iter(delivery))
q = deque([root])
while q:
  x = q.popleft()
  for path in paths[x]:
    if path[0] != parent[x]:
      q.append(path[0])
      parent[path[0]] = x
# find unused cities and discard them, getting the subtree
keep = [False] * N
for i in delivery:
  x = i
  while x != -1 and not keep[x]:
    keep[x] = True
    x = parent[x]
paths = [[path for path in paths[i] if keep[path[0]] and keep[i]] for i in range(N)]
# now we find the longest path in the tree
def furthest_vertex(start):  # return a tuple contains the vertex index and the path length
  result = (start, 0)
  visited = [False] * N
  q = deque([result])
  while q:  # run a Bfs from 'start' and count the path length from it
    x = q.popleft()
    if x[1] > result[1]:  # keep track of the furthest vertex
      result = x
    visited[x[0]] = True
    for path in paths[x[0]]:
      if not visited[path[0]]:
        q.append((path[0], x[1] + path[1]))
  return result
start = next(i for i, x in enumerate(paths) if len(x))  # get the first city in list
longest_path = furthest_vertex(furthest_vertex(start)[0])[1]
# all paths exist in both connected cities, so no need to multiply by 2 here
print(sum(sum(x[1] for x in l) for l in paths) - longest_path)
