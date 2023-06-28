def swap(l,i,j):
    l[i],l[j] = l[j],l[i]
def checkparent(i):
    if (i-1) // 2 >= 0:
        return True
    else:
        return False
def parent(i):
    return (i-1) // 2
def heapify(l,i):
    max = i
    left = 2*i + 1
    right =  2*i + 2
    if (left < len(l)) and (l[max][1] < l[left][1]):
        max = left
    if (right < len(l)) and (l[max][1] < l[right][1]):
        max = right
    if max != i:
        swap(l,i,max)
        heapify(l,max)
    return l     
def heap(l):
    for i in range(len(l),-1,-1):
        heapify(l,i)
    return l
def heapup(l,i):
    if checkparent(i):
        if l[i][1] > l[parent(i)][1]:
            swap(l,i,parent(i))
            return heapup(l,parent(i))
def extractmax(l):
    x = l[0]
    swap(l,0,-1)
    l.pop()
    heapify(l,0)
    return x
def enqueue(l,data):
    l.append(data)
    heapup(l,len(l)-1)
def graph(l,n):
    g = []
    for i in range(n):
        g.append([])
    for i in range(len(l)):
        k = l[i][0]
        m = l[i][1]
        o = l[i][2]
        g[k].append((m,o))
        g[m].append((k,o)) 
    return g
def findMaxCapacity(n,links,s,t):
    res = [float('inf'),[]]#this stores the result
    gr = graph(links,n)
    cap = []#this stores the max capacity to the router at the ith index
    previous = []#this stores the previous router
    reached = []#this ensures to not visit the same router
    for i in range(n):
        cap.append(-1)
        previous.append(None)
        reached.append(False)
    cap[s] = float('inf')
    l = [(s,0)]
    while (len(l) != 0):
        x = extractmax(l)
        if x[1] >= cap[x[0]]:
            cap[x[0]] = x[1]
        reached[x[0]] = True
        for i in range(len(gr[x[0]])):
                k = gr[x[0]][i][0]
                m = gr[x[0]][i][1]
                if reached[k] == False:
                    if min(cap[x[0]],m) > cap[k]:
                        cap[k] = min(cap[x[0]],m)#updating the capacity
                        previous[k] = x[0]
                        enqueue(l,(k,min(cap[x[0]],m)))
    i = t
    while i != s:
        if cap[i]<=res[0]:
            res[0] = cap[i]
        res[1].append(i)
        i = previous[i]
    res[1].append(s)
    res[1].reverse()
    return res
