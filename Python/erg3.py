def function(FPA, l):
    y = 0
    f = 0
    for v in l:
        f = float(v)
        y = f + (f * (FPA/100))
        print(y)


FPA = int(input("εισαγεται τον ΦΠΑ: "))
d = {}
n = int(input("εισαγεται τον αριθμο των αγορων: "))



for i in range(n):
	k = input("εισαγεται (αντικειμενο) key: ")
	v = input("εισαγεται (ευρω) value: ")
	d.update({k:v})
print(d)
l = list(d.values())
print(l)
function(FPA, l)