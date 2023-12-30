"""c="hello world"
print(c[3])
print(c[-5];2)
print(c[6])
print(c[-1])
print(c[-6])"""


"""c="hello saurabh"
print(c[2:5])
print(c[1:7])
print(c[-5:-1])
print(c[2:8:2])
print(c[::-2])"""


#string operators

# +  concatenation

"""name1="saurabh"
name2="petkar"
i=name1+name2
print(i)"""


#   * -  repetation
"""c="unique"
print(c*4)"""


"""c="unique"
d=c*4
print(d)"""

# in and not in


"""l="i just came to pune"
if "pune" in l:
    print("present")
else:
    print("not present")"""

"""l="i just came to pune"
print("just" in l)

l="i just came to pune"
print("just" not in l)"""


#wap user will enter first name and last name- print the full name

"""name1="saurabh"
name2="petkar"
fullname=name1+name2
print(fullname)
"""




#wap first characterof  entered char is P or not
"""i=str(input("enter character"))
if "P" in i:
    print("true")
else:
    print("false")
"""




#user will enter address and check the address contains pune or not

"""l=str(input("address"))
if "pune" in l:
    print("correct")
else:
    print("incorrect")"""







#


"""l= "saurabh petkar"

print(l.upper())
print(l.lower())
print(l.islower())
print(l.capitalize())"""



"""l= "saurabh petkar"

print(l.find('tk'))
print(l.count('e'))
print(l.index('u'))"""









# string functions
#case related

"""l="hello world"
for i in l:
    print(i)
"""


"""l="hello world"
count=0
while count<len(l):
    print(l[count])
    count=count+1"""


#print every alternate character
#reverse

l=input("enter the character")
count=0
while count<len(l):
    print(l[count])
    count=count+2


#reverese
"""l="python assignment"
count=len(l)-1
while count>=0:
      print(l[count])
      count=count-1"""

##
"""data="saurabh19082000"
print(data.isalnum())
print(data.isalpha())
print(data.isdigit())
print(data.isspace())"""


#

"""address=input("enter your address")
dcount=0
for i in address:
    if i.isdigit():
         dcount=dcount+1
print(dcount)
"""




#wap to find the number of lowercase letters and uppercase letters if entered full name

"""name=input("enter fullname")
lcount=0
ucount=0
for i in name:
    if i.islower():
        lcount=lcount+1
    elif i.isupper():
        ucount=ucount+1
print("uppercase=",ucount)
print("lowercase=",lcount)"""



#user will enter full address
#1) count number of alphabets
#2) count number of digits
#3) count number of spaces
#4) count number of special characters


"""address=input("enter full address")
acount=0
dcount=0
scount=0
ccount=0
for i in address:
    if i.isalpha():
        acount=acount+1
    elif i.isdigit():
        dcount=scount+1
    elif i.isspace():
        scount=scount+1
    else:
        ccount=ccount+1
print("alphabets=",acount)
print("digits=",dcount)
print("space=",scount)
print("special characters=",ccount)
"""

#wap to find entered character is present in string or not? and if preserent prints its position
"""ch=input("enter the character")
i="saurabh"
if ch in i:
    print("present",i.index(ch))
else:
    print("not")
"""









# replace function

"""lan="python is an easy programming language"
lan2=lan.replace("an easy","a good")
print(lan2)"""

#split function
"""lan="pyt.hon is a.n easy pro.gramming l.anguage"
k=lan.split(".")
print(k)"""



#
















