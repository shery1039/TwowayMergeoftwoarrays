a=[-34,-8,-5,0,3,5,7]
b=[9,34,65,90,22]


# First step is to compare elments of both list one by one and store it into a new list
c = []
i=0
j=0
k=0
# to store you have to use loop
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
        # one way to add remaining elment 
# If there are remaining elements in `a`, append them to `c`
while i < len(a):
    c.append(a[i])
    i += 1

# If there are remaining elements in `b`, append them to `c`
while j < len(b):
    c.append(b[j])
    j += 1
    
    
# Second way of add remaining elements
    
# c.extend(a[i:])
# c.extend(b[j:])


print(c)