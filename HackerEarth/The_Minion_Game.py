s=input().rstrip()
stu=0
kev=0
v=['A','I','E','O','U']
n=len(s)
for i in range(n):
	if(s[i] in v):
		kev+=(n-i)
	else:
		stu+=(n-i)
if(stu==kev):
	print('Draw')
elif(stu>kev):
	print('Stuart',stu)
else:
	print('Kevin',kev)