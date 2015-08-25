a=[] // fill it up with numbers

for i in range(1,len(a)):
  j=i
  while(j>0 and a[j-1]>a[j]):
    a[j],a[j-1]=a[j-1],a[j]
    
