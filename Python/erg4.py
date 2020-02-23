string = input("please wright something: ")
def function(string):
    s = 0
    for c in string:
        s = s + ord(c)
        print(s)
    if (s % 2) == 1 :
        print("o arithmos einai prwtos")
    else:
        print("o arithmos den einai prwtos")
function(string)