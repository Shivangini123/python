
import array as ar;
def CountSort():
    Min=min(arr);
    Max=max(arr);

    Range=Max-Min+1;

    frq=[0]*(Range);
    arrlen = len(arr);

    for i in range(arrlen):
        index=arr[i]-Min;
        frq[index]=frq[index]+1;
    frqlen=len(frq);

    for i in range(1,frqlen):
        frq[i]=frq[i]+frq[i-1];

    ans=[0]*arrlen;

    for i in range((arrlen-1),-1,-1):
        val=arr[i];
        pos=frq[(val-Min)];
        idx=pos-1;
        ans[idx]=val;
        frq[(val-Min)]=frq[(val-Min)]-1;

    anslen=len(ans);

    for i in range(anslen):
        arr[i]=ans[i];

global arr;
arr=ar.array('i',[]);
n=int(input("Enter the number of elements"));

for i in range(n):
    x=int(input("Enter the number"));
    arr.append(x);
print(arr);
CountSort();
print("Sorted array is:");
print(arr);
