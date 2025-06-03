from mdit_py_plugins.myst_role.index import myst_role
from sklearn.conftest import print_changed_only_false

txt="   abc     def     ghi"
print(txt)
print(txt.lstrip())
print(txt.rstrip())

'''Escape Charactor'''
systr = "My favourite TV Series is \"Game of Thrones\""
print(systr)

'''List'''
list1=[]
print(type(list1))
list1=[10,30,60]
print(list1)
list1.append([10,10])
list1.append(10+10j)
list1.append('Diamond')
list1.append(97.68)
print(list1)
'''Nested Index'''
print(list1[3][0])
print(list1[3][1])

'''Function in List'''

print(len(list1))
list7 = ['Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'}]
print(list7[0][1])

'''List Slicing'''
mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
print(mylist[:])
print(mylist[1:])
print(mylist[1:-1])
print(mylist[1:-1])

print(mylist[-1:])
print(mylist[-5:])

'''Add/Remove/Change'''
print(mylist)
mylist.append(1000)

mylist.pop()
print(mylist)

mylist.append('nine')
mylist.insert(0,'zero')
print(mylist)

mylist.remove('zero')
print(mylist)

mylist.pop(len(mylist)-1)
print(mylist)

mylist.remove('eight')
print(mylist)

'''Copy List'''
mylist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print(mylist)
mylist1=mylist
print(mylist1)
print(id(mylist))
print(id(mylist1))

'''Cooy'''
mylist2=mylist.copy()
print(mylist2)

'''Join list '''
print(mylist1+mylist2)
L1=[1,2,3,4,6]
L2=[5,6,7,8]
L1.extend(L2)
print(L1)


'''Membership'''
if 1 in L1:
    print("yes")
else:
    print("No")


'''Reverse and Sort'''

L1.reverse()
print(L1)
L1.sort()
print(L1)
L1.sort(reverse=True)
print(L1)


'''Loop throught List'''
for i in L1:
    print(i)

'''Count'''
print(f"Count of 6= {L1.count(6)}")


'''All/Any'''
L5=[True,True,False]
print(all(L5))
print(any(L5))
L3 = [1,2,3,True,145]
print(all(L3))



























