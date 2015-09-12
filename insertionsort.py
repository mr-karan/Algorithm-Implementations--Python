a=[1,4,3,5,6,2]
for i in range(1,len(a)):
	j=i-1
	key=a[i]
	while(j>=0) and (a[j]>key):
		a[j+1]=a[j]
		j=j-1
	a[j+1]=key
	print (a)
