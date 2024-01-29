# extend a list without append

l1=[12345]
l2=[87564]
l1.append(l2)
print(l1)

l1=[12345]
l2=[87564]
l1.extend(l2)
print(l1)

l1=[1,2,3,4,5]
l2=[8,7,5,6,4]
l1[:0]=l2
print(l1)