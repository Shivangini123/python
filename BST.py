class node:
    def __init__(self,val):
        self.data=val;
        self.left=self.right=None;

def Insert(root,val):
    if root==None:
        return node(val);
    elif(val<=root.data):
        root.left=Insert(root.left,val);
    elif(val>=root.data):
        root.right=Insert(root.right,val);
    else:
        print("Duplicate key");
    return root;

def Findmaxad(root):
    while(root.right!=None):
        root=root.right;
    return root;

def Deletion(root,val):
    if(root==None):
        return None;
    elif(val>root.data):
        root.right=Deletion(root.right,val);
    elif(val<root.data):
        root.left=Deletion(root.left,val);

    else:
        if(root.right and root.left):
            temp=Findmaxad(root.left);
            root.data=temp.data;
            root.left=Deletion(root.left,root.data);

        elif(root.left==None):
            temp=root;
            root=root.right;
            del temp;

        elif(root.right==None):
            temp=root;
            root=root.left;
            del temp;

        else:
            del root;
            root=None;

    return root;

def Search(root,val):
    if(root==None):
        print("Not found");
        return None;
    elif(val<root.left.data):
        return Search(root.left,val);
    elif(val>root.right.data):
        return Search(root.right,val);
    else:
        return root;




def main():
    root=node(10);

    root=Insert(root,60);
    root = Insert(root, 45);
    root = Insert(root, 25);
    root = Insert(root, 12);

    root=Deletion(root,60);
    



if __name__=="__main__":
    main();
