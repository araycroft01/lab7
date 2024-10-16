#the authors are Anna Raycroft and Victoria Garcia
#1
def too_long (x):
    if len(x)<=140:
        print("send")
    else:
        print("text is too long")
too_long('hii')

#2
import unicodedata
print(unicodedata.lookup("sun"))
print(unicodedata.lookup("cat"))
print (unicodedata.lookup("two hearts"))

def text_one ():
    print("I", unicodedata.lookup("two hearts"),"you")
text_one()
def text_two():
    print("I need", unicodedata.lookup("sun"),"asap")
text_two()
def text_three():
    print("I love", unicodedata.lookup("cat"))
text_three()
def text_four():
    print("my", unicodedata.lookup("dog"), "is so cute")
text_four()
def text_five():
    print("my fav flower is", unicodedata.lookup("rose"))
text_five()

print(unicodedata.name("("))

#3
def number_of_o(word):
    total=0
    for x in word:
        if x=="o":
            total=total+1
    print(total)
            
number_of_o("hello")

#4
def first_letter(word):
    total=1
    for x in word:
        if x=="k":
            return("True")
        else:
            return ("False")
print(first_letter("kite"))
print(first_letter("love"))
print(first_letter("luck"))
