'''MergeSort

Complexity : O(n logn)

'''

def mergesort(numlist):
	if (len(numlist)>1):
		middle=len(numlist)//2
		leftHalf=numlist[:middle]
		rightHalf=numlist[middle:]

		mergesort(leftHalf)
		mergesort(rightHalf)

		i=0
		k=0
		j=0

		while(i<len(leftHalf) and j<len(rightHalf)):
			if leftHalf[i]<rightHalf[j]:
				numlist[k]=leftHalf[i]
				i=i+1
			else:
				numlist[k]=rightHalf[j]
				j=j+1
			k=k+1
		while(i<len(leftHalf)):
			numlist[k]=leftHalf[i]
			i=i+1
			k=k+1
		while(j<len(rightHalf)):
			numlist[k]=rightHalf[j]
			j=j+1
			k=k+1
	


alist = [54,26,93,45,37,14,28,10,157,98,6475,45,74]
mergesort(alist)
print(alist)
