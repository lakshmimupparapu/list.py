a=[50,40,23,70,56,12,5,10,7]
i=0
max=0
smax=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]>smax and a[i]<max:
        smax=a[i]
    i=i+1
print(smax)