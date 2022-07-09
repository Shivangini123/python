import array as ar
def FindPivot(arr,low,up):
    pivot=arr[low];
    i=low+1;
    j=up;

    while i<=j:
        while ((pivot > arr[i]) and (i < up)):
            i=i+1;
        while (arr[j] > pivot):
            j=j-1;
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i];
            i=i+1;
            j=j-1;
        else:
            i=i+1;
    arr[low] = arr[j];
    arr[j] = pivot;
    return j;
def QuickSort(arr,low,up):
    if(low>=up):
        return;
    pivloc=FindPivot(arr,low,up);
    QuickSort(arr,low,pivloc-1);
    QuickSort(arr,pivloc+1,up);

def main():
    arr=ar.array('i',[]);
    n=int(input("Enter the number of elements"));
    for i in range(0,n):
        x=int(input("Enter the number"));
        arr.append(x);
    QuickSort(arr,0,n-1);
    print("Sorted array is:", end=" ")
    for i in range(n):
        print(arr[i], " ", end=" ");
if __name__=="__main__":
    main()
