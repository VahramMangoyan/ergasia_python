f = open("ask.txt","r")
s = 0
x = 2
keno = " "
teleytaio = "y"
proteleytaio = "a"
for line in f:
    for word in line.split():
        
        if len(word) > x:
            print(word[1:]+"ay")
            
            