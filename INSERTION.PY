def insertionsort(arr):
    for i in range (1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
arr=[7,3,10,5,6,12,5]
print("SAKSHAM JAIN-1716510094")
insertionsort(arr)
print("Sorted array is")
for i in range(len(arr)):
    print(arr[i]) 