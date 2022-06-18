class Graph:
    graph={};

    def Addedge(self,node,nbr):
        if node not in self.graph:
            self.graph[node]=[nbr];
        else:
            self.graph[node].append(nbr);
    def ShowEdges(self):
        for node in self.graph:
            for nbr in self.graph[node]:
                print("(",node,", ",nbr,")");
    def DFS(self,src):
        visit={};
        for i in self.graph:
            visit[i]=False;
        stack=[src];
        visit[src]=True;
        while stack:
            a=stack.pop(len(stack)-1);
            for i in self.graph[n]:
                if not visit[i]:
                    stack.append(i);
                    visit[i]=True;
            print(a,end=" ");
    def BFS(self,src):
        visit={};
        for i in self.graph:
            visit[i]=False;
        queue=[];
        queue.append(src);
        visit[src]=True;

        while(len(queue)!=0):
            src=queue.pop(0);
            for node in self.graph[src]:
                if visit[node]!=True:
                    visit[node]=True;
                    queue.append(node);
            print(src,end=" ");
        print("");
if __name__=="__main__":
    g=Graph();
    g.Addedge(1,2);
    g.Addedge(1,3);
    g.Addedge(2,3);
    g.Addedge(2,1);
    g.Addedge(3,1);
    g.Addedge(3,2);
    g.Addedge(3,4);
    g.Addedge(4,3);

    g.ShowEdges();
    print("BFS: ",end=" ");g.BFS(1);
    print("DFS: ",end=" "); g.DFS(1);
