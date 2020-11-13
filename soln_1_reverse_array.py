arr = [1, 2, 3, 4, 5]
arr=arr[::-1]  # method 1
# arr.reverse()  method 2
"""l=len(arr)
for i in range(l):
    arr[i]=arr[l-1-i]""" # method 3
"""def reverse_arr(A,start,end):
    if start>=end:
        return A
    A[start],A[end]=A[end],A[start]
    reverse_arr(A,start+1,end-1)


arr = [1, 2, 3, 4, 5]
reverse_arr(arr,0,len(arr)-1)""" # method 4
"""start=0
end=len(arr)-1
while(start<end):
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1""" # method 5
print(arr)
