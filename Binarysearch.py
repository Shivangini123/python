import array as ar
def BinarySearch(arr,n,item):
    low=0;
    up=n-1;
    while(low<=up):
        mid=int((low+up)/2);
        if(item>arr[mid]):
            low=mid+1;
        elif(item<arr[mid]):
            up=mid-1;
        else:
            return mid;
    return -1;
arr=ar.array('i',[]);
n=int(input("Enter the number of elements"));
print("Enter the numbers in sorted order");
for i in range(n):
    y=int(input("Enter the number "));
    arr.append(y);
item=int(input("Enter the number to be searched"));
index=BinarySearch(arr,n,item);
if(index==-1):
    print("item is not in the array");
else:
    print("item found at position :",index+1);
