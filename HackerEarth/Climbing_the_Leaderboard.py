def finr(x,n):
	if(x>=a[0]):
		return 1
	elif(x<a[n-1]):
		return n+1
	elif(x==a[n-1]):
		return n
	else:
		l=0
		u=n
		i=(l+n)//2
		while(not(x>=a[i] and x<a[i-1])):
			if(x>a[i]):
				u=i
			elif(x<a[i]):
				l=i
			i=(l+u)//2
		return i+1
n=int(input().rstrip())
a=list(map(int,input().rstrip().split()))
for i in range(n-1,0,-1):
	if(a[i]==a[i-1]):
		del a[i]
		n=n-1
m=int(input())
b=list(map(int,input().rstrip().split()))
for i in range(m):
	te=finr(b[i],n)
	print(te)
