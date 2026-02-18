calories =  {index:num for index,num in enumerate(map(int,input().strip().split(' ')))}
strips = input().strip()
sum  = 0


for str in strips:
    sum += calories[int(str)-1]

