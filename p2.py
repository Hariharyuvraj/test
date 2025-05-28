l=[10,20,30,'yuvraj','anuja','pune','tushar']
print(l)

#:In list data type we can add any values like int,str,etc.

#: Append() 
#: by using append we can add value in list 
l.append(230)
print(l)
l.append('bunty')
print(l)

# remove: by using this operater we can remove item from the list

l.remove(230)
print(l)
l.remove('bunty')
print(l)

#:if i want to replace the item by another item in list then i can use following

l[1]=1991
print(l)

l[-1]="dada"
print(l)

#: in list we can use slice operater

s1=l[1:3]
print(s1)

s2=l[1:0]
print(s2)

s3=l[1:-1]
print(s3)

# reverse() and reversed()

l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)

l1=[12,34,55,67,8,88]
l1.reverse()
print(l1)

l2=['megha','nava','yuvraj','usha','bharat','malan','laxman']
l2.reverse()
print(l2)

# now reversed()

l=[1,2,3,4,5,6,7,8,9]
r=reversed(l)
l1=list(r)
print(l1)

l='yuvraj'
r=reversed(l)
for x in r:
    print(x)

l1=['harihar','bharat','yuvraj']
r=reversed(l1)
for x in r:
    print(x)

## 'sort()' funtion using for assending order of number & str alphabetically
    
l=[3,5,7,5,7,9,10,0]
l.sort()
print(l)

l=['ball','fox','dog','sheep','apple','light']
l.sort()
print(l)

# list
# list.sort()
l=[1,2,3,4,5,6,7,8,9]
l.sort()

l=[[1, 2, 3],[4, 5, 6],[7, 8,9]]
print(l)

print('element in matrix style:')
for x in l:
    for y in x:
        print(y,end=' ')
    print()
    
l=[[1, 2, 3],[4, 5, 6],[7, 8,9]]
print(l)

print('element in row wise:')
for x in l:
    print(x)