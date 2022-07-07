import array as ar
def MaximumSumSubArray():
    MaxSum=0;
    CurrSum=0;

    for i in range(0,len(arr)):
        CurrSum=CurrSum+arr[i];
        if (CurrSum > MaxSum):
            MaxSum = CurrSum;
        if (CurrSum < 0):
            CurrSum = 0;
    return MaxSum;
def main():
    global arr,n;
    arr=ar.array('i',[]);
    n=int(input("Enter the number of elemnets"));
    for i in range(n):
        a=int(input("Enter the number:"));
        arr.append(a);
    print("Array is :",end=" ");
    for i in range(len(arr)):
         print(arr[i]," ",end=" ");
    MAx=MaximumSumSubArray();

    print("\nMaximum Sum is:",MAx);
if __name__=="__main__":
    main();
