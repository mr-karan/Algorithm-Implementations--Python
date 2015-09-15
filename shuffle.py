'''
To shuffle an array a of n elements (indices 0..n-1):
  for i from n − 1 downto 1 do
       j ← random integer such that 0 ≤ j ≤ i
       exchange a[j] and a[i]
'''

'''Fisher Yates Shuffle'''

import random

def shuffule(a):
  for i in reversed(range(len(a))):
      j=random.randint(0,i)
      a[j],a[i]=a[i],a[j]
  return a

ans=shuffle([3,4,8,1,7,6,9,0,2])

print(ans)
