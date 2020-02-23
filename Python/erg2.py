f = open("ask.txt","r")
good = 0
bad = 0
for line in f:
    for word in line.split():
        print(word)
        for letters in word:
            print(letters)
            if letters == "a" or letters =="o" or letters =="e" or letters == "i":
                pass
            else:
                if letters == "f" or letters == "c" or letters == "k" or letters =="r":
                    bad += 1
                else:
                    good += 1
        if bad > good:
            print("kakkia")
        else:
            print("kalh")
        bad = 0
        good = 0
        