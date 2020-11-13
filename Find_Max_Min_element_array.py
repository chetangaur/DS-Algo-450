#arr = [1000, 11,233,534,4300,54]
"""mini=arr[0]    # method 1
maxi=arr[0]
l=len(arr)
for i in range(l):
    if mini>arr[i]:
        mini=arr[i]
    if maxi<arr[i]:
        maxi=arr[i]
print(mini)
print(maxi)"""
# method 2
def min_max(arr):

    l=len(arr)
    if l%2==0:
        if arr[0]<arr[1]:
            mini=arr[0]
            maxi=arr[1]
        else:
            mini=arr[1]
            maxi=arr[0]
        i=2
    else:
        mini=arr[0]
        maxi=arr[0]
        i=1
    if l==1:
        return(mini,maxi)
    elif l==2:
        return(mini,maxi)
    else:
        while(i<l-1):
            if arr[i]<arr[i+1]:
                mini=min(mini,arr[i])
                maxi=max(maxi,arr[i+1])
            else:
                mini = min(mini, arr[i+1])
                maxi = max(maxi, arr[i])
            i=i+2
        return(mini,maxi)


arr = [1000, 11, 233, 534, 4300, 54]
mini,maxi=min_max(arr)
print(mini)
print(maxi)





