class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
class LinkedList:
    def __init__(self):
        self.start=None;

    def Insert(self,data):
        newNode = Node(data);
        if (self.start == None):
            self.start = newNode;
        else:
            temp = self.start;
            while temp.next != None:
                temp = temp.next;
            temp.next = newNode;

    def DetectLoop(self):
        slowpointer=self.start;
        fastpointer=self.start;

        while slowpointer != None and fastpointer != None and fastpointer.next != None:
            slowpointer=slowpointer.next;
            fastpointer=fastpointer.next.next;

            if(slowpointer==fastpointer):
                return True;
        return False;

def main():
    Mylist = LinkedList();
    Mylist.Insert(1);
    Mylist.Insert(2);
    Mylist.Insert(3);
    Mylist.Insert(4);

    temp=Mylist.start;

    while(temp.next!=None):
        temp=temp.next;
    temp.next=Mylist.start;

    if(Mylist.DetectLoop()):
        print("loop exists in the linked list");
    else:
        print("Loop does'nt exist in the linked list");



if __name__=="__main__":
    main();
