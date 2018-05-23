
"""
广度优先BFS：
"""
def procedure(v):
    pass

def BFS(G,v0):
    """ 广度优先搜索 """
    q, s = [], set()
    q.extend(v0)
    s.add(v0)
    while q:    # 当队列q非空
        v = q.pop(0)
        procedure(v)
        for w in G[v]:     # 对图G中顶点v的所有邻近点w 
            if w not in s: # 如果顶点 w 没被发现
                q.extend(w)
                s.add(w)    # 记录w已被发现