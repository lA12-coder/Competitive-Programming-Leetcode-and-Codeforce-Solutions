left = 0
right = 0
s1  = input().strip().lower()
s2 = input().strip().lower()
equal = False



while left < len(s1) and right<len(s2):
    if ord(s1[left])<ord(s2[right]):
        print(-1)
        equal=False
        break
    if ord(s1[left])>ord(s2[right]):
        print(1)
        equal=False
        break
    else:
        equal=True
        left+=1
        right+=1
        
if equal==True:
    print(0)
        
    
    