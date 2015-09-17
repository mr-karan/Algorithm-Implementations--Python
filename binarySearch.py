"""
    binary_search.py
    Implementation of binary search on an already sorted list.
    Recursively partitions the list until the key is found.
    Time Complexity:  O(lg n)
  
"""



def binarySearch(a,key):
	imin=0
	imax=len(a)
	while(imin<=imax):
		imid=(imax+imin)//2
		if a[imid]==key:
			return imid
		elif a[imid]<key:
			imin=imid+1
		else:
			imax=imid-1
	return False

numlist=[1,4,32,74,5,18,8,9,24,25,30,26,85]

ans = binarySearch(numlist,8)

print(ans)
