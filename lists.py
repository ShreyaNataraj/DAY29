#accesssing the list
shoppinglist = ['milk','cheese','butter']
print(shoppinglist[0])
#Using Boolean values
print('milk' in shoppinglist)
#inserting property
shoppinglist.insert(0,'eggs')
print(shoppinglist)
#appending property
shoppinglist.append('ghee')
print(shoppinglist)
#extend property
newlist = [11,12,13,14,15]
shoppinglist.extend(newlist)
print(shoppinglist)
#slicing/deleting elements from the list
print(shoppinglist[:])
shoppinglist.pop()
print(shoppinglist)
#DELETING AN ELEMENT
del shoppinglist[2:4]
print(shoppinglist)
#linearsearch
def linear_search(p_list,p_target):
  for i, value in enumerate(p_list):
    if value == p_target:
      return i
  return -1
linear_search(shoppinglist,13) 
a =[1,2,3,4,5]
 #max.min,len functions
print(max(a))
print(min(a))
print(len(a))
#conversting strings into list
a ='spam'
b = list(a)
print(b)

