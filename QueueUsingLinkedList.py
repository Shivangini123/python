class node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
class Queue:
    def __init__(self):
        self.front=self.rear=None;

    def isEmpty(self):
        return self.front==None;

    def Push(self,data):
        temp=node(data);

        if self.rear==None:
            self.front=self.rear=temp;
            return;
        self.rear.next=temp;
        self.rear=temp;

    def Pop(self):
        if self.isEmpty():
            return ;

        temp=self.front
        self.front=temp.next;

        if(self.front==None):
            self.rear=None;

    def ViewQueue(self):
        temp=self.front;
        if self.isEmpty():
            print("Queue is empty");
        else:
            while (temp != None):
                print(temp.data, " ", end=" ");
                temp = temp.next;
            return ;

def main():
    q=Queue();
    q.Push(1);
    q.Push(2);
    q.Push(3);
    q.Push(4);
    q.Push(5);

    q.ViewQueue();
    print();
    q.Pop();
    q.Pop();

    q.ViewQueue();

    # print("Front is:",(q.front.data));
if __name__=="__main__":
    main();
