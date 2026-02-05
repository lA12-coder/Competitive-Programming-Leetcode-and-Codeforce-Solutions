n,m = map(int,input().strip().split( ))
arr1 = list(map(int,input().strip().split( )))
arr2 = list(map(int,input().strip().split( )))

left = 0
result = []
for right in range(len(arr2)):
    while left<len(arr1) and arr1[left] < arr2[right]:
        left+=1
    result.append(left)
    
print(*result)