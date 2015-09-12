'''
Quicksort, like merge sort, applies the divide-and-conquer paradigm introduced
function quicksort(array)
    less, equal, greater := three empty arrays
    if length(array) > 1  
        pivot := select any element of array
        for each x in array
            if x < pivot then add x to less
            if x = pivot then add x to equal
            if x > pivot then add x to greater
        quicksort(less)
        quicksort(greater)
        array := concatenate(less, equal, greater)

'''
def quicksort(a):
	less=[]
	greater=[]
	equal=[]
	result=[]
	if len(a)<=1:
		return a
	if len(a)>1:
		pivot=a[0]
		for i in a:
			if i<pivot:
				less.append(i)
			elif i==pivot:
				equal.append(i)
			else:
				greater.append(i)
		less=quicksort(less)
		greater=quicksort(greater)
		result=less+equal+greater
	return result


ans=quicksort([8,6,5,4,21,1])

print (ans)
