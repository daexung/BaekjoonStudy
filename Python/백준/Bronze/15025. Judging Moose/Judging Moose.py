a,b= map(int,input().split(' '))
if a==b and a!=0 :
  print("Even %d"%(a+b))
elif a!=b :
  n=max(a,b)*2
  print("Odd %d"%(n))
elif a==b==0:
  print("Not a moose")