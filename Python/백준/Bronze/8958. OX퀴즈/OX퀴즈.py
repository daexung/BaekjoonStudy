n=int(input())

for i in range(0,n):
  q=input()
  s=0
  a=[]
  list=q.split('X')
  for j in list :
    if j != '' :
      a.append(j)
  
  for k in a :
    b=0
    for l in range(0,len(k)):
      b+=1
      s+=b
  print(s)
  