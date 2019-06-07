def fact(n):
	s=[0 for i in range(250)]
	s[0]=1
	k=0
	for i in range(2,n+1):
		add=0
		for j in range(0,250):
			te=s[j]*i+add
			add=te//10
			s[j]=te%10
			if(j>=k):
				if(add==0):
					k=j
					break
	nu=''
	for i in range(k+1):
		nu=str(s[i])+nu
	print(nu)
n=int(input())
fact(n)
