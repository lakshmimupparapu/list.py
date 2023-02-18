# a=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# s=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         s=s+a[i][j]
#         j+=1
#     i+=1
# print(s)


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    if b>c:
        print("b is second max")
    else:
        print("c is second max")
elif b>a and b>c:
    if a>c:
        print("a is second max")
    else:
        print("c is second max")
elif c>a and c>b:
    if a>b:
        print("a is second max")
    else:
        print("b is second max")
else:
    print("Invali data")