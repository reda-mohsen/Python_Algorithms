# Tuples
# Tuples are immutable. we cannot change a value in a tuple using its index
# instead change the whole tuple!
def qr(x,y):
    """
    Function to get the quotient and the reminder of x/y
    Input: integer x and integer y
    Output: Tuple contain the quotient and the reminder
    """
    q = x//y
    r=x%y
    return (q, r)
x = qr(32, 16)
print(x)
print(x[0])
print(type(x[0]))

y = 5
z = 20
(y,z)=(z,y)
print(y)
print(z)
print('------------')
# List
# List are mutable, we can add items to the list using its index
# .append(): add an item to the end of the list (take just an item)
# .extend(): append all the items from a list (take a whole list of items)
# del(List[index]): delete element at a specific index V
# .remove(element): remove a specific element, if element occurs multiple times, removes first occurence. raises a ValueError if there is no such item.
# .pop(): removes and returns the last item in the list.
# .pop(x): remove and return an item at any position by including the index of the item
# list(s): returns a list with every character from string s.
# .split(): split a string on a character parameter to a list
# .join(List): turn a list of characters into a string (e.g. 'separator'.join(List))
# sorted(List): just returns a sorted list, does not mutate List
# List.sort(): mutates List, Sort the items of the list in place
# List.reverse(): reverse the elements of the list in place.
# list1 = list2: aliasing(they points on the same memory location, so if one change the other also changes)
#list1=list2[:]: cloning(copy list2 into list 1 on different memory locations)
# list1=sorted(list2): cloning a sorted version of list 2 into list 1
# when using a list in a loop and length of the list expected to be changed. Take a copy of the list at first and iterate on the copied one and change the original one.

List=[] # Empty list
List=[1,5,6,9,3]
print(type(List))
List.append(4)
print(List) # [1,5,6,9,3,4]
List.extend([1,2,3]) # [1,5,6,9,3,4,1,2,3]
del(List[6])
print(List) # [1,5,6,9,3,4,2,3]
List.remove(3) # [1,5,6,9,4,2,3]
print(List) # [1,5,6,9,4,2,3]
p = List.pop()
print(p) #3
print(List)# [1,5,6,9,4,2]

string = "Hello, i am reda"
stringList=list(string) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'i', ' ', 'a', 'm', ' ', 'r', 'e', 'd', 'a']
len(stringList) # 16
string.split(i) # ['Hello, ', ' am reda']
"".join(stringList) # 'Hello, i am reda'
sorted(stringList) # ASCII CODE
list=[1,2,3,423,543,63,-3,44]
sorted(list) # [-3, 1, 2, 3, 44, 63, 423, 543] but list remain same
list.sort() # now list is sorted in place
list.reverse() #[543, 423, 63, 44, 3, 2, 1, -3]
print('------------')
# Dictionaries
# Each element in dictionary consists of key:value pairs and is indexing by its key
# .keys(): get an iterable that acts like a tuple of all keys, return dict_keys([,,])
# .values(): get an iterable that acts like a tuple of all values, return dict_values([,,])
# .get(key,default): return value within key, return default if key not found, if no default it returns None
# .update(dictionary): add key-value pairs of dictionary into the original dictionary
dic={} # Empty dictionary
dic={'Reda':'A+', 'Mohy':'B', 'Peter':'C-'}
dic['Dina']='B-' # Add entry(key-value pair)
'Reda' in dic # True
'reda' in dic # False
d1 = {'A':10, 'B':25}
d1['A']=100
for key in d1:
    print(key+":"+d1[key]) # A:100 # B:25
