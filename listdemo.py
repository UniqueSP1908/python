
##

"""l1=[]
l2=[55,20]
l3=[66,85,44.4]
l4=[5,30,5,3.02]
print(type(l1))
print(type(l2))
print(type(l3))
print(type(l4))"""


#
"""l1=[55,41,65]
l2=[4,5,6,1]
l2=l1+l2
print(l2)"""

"""l1=[65,20]
l2=l1*3
print(l2)"""


#wap creating list of five employees. find the entered employee is present in list or not


"""l1=["hp","apple","dell","asus","lenovo"]
name=input("enter employee name")
if name in l1:
    print("present")
else:
    print("not present")"""


#wap to find entered character is vowel or not

"""ch=str(input("enter the alphabet"))
l1=["a","e","i","o","u"]
if ch in l1:
    print("it is vowel")
else:
    print("not vowel")"""

#
"""marks=[70,68,65,66,52,77,70,32]
print(marks.count(70))
print(marks.index(32))
print(len(marks))
print(sum(marks))
print(min(marks))
print(max(marks))

marks.reverse()
print(marks)

marks.sort()
print(marks)"""


"""marks=[70,68,65,66,52,77,70,32]
l=[500,1000]
print(marks)
#marks[3]=100
#arks[5:8]=[200,300,400]
#marks.append(500)
#marks.insert(0,500)
marks.extend(l)
print(marks)"""

"""marks=[70,68,65,66,52,77,70,32]
print(marks)
#marks.pop(3)
#marks.remove(68)
#del marks[2]
marks.clear()
print(marks)"""


#
"""l=[]
print("enter 5 values")
for t in range(5):
    i=int(input())
    l.append(i)
for t in l:
    print(t)"""

#
"""l=[]
print("enter 5 values")
for t in range(5):
    i=int(input())
    l.append(i)
count=0
while count<len(l):
    print(l[count])
    count=count+1"""


# wap to create a list & take five marks from user & find the largest marks & find the smallest marks
# &find the average of marks

"""l=[]
print("enter marks of 5 subjects")
for t in range(5):
    i=int(input())
    l.append(i)

print(max(l))
print(min(l))
i=sum(l)/5
print("average=",i)"""



# 8/08/2023

"""list=[1,2,3,4,5]
print(list)
list.reverse()
print(list)"""

"""l=[]
print("enter 5 values")
for t in range(5):
    i=int(input())
    l.append(i)
m=[]
count=len(l)-1
while count>=0:
    m.append(l[count])
    count=count-1
print(l)
print(m)
"""


