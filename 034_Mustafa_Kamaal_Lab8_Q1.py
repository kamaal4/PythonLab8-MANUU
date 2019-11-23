f = open("main.txt","r")
f = f.readline()
Digits=Alphabets=0
for c in f:
    if c.isdigit():
        Digits=Digits+1
    elif c.isalpha():
        Alphabets=Alphabets+1
    else:
        pass
print("Letters", Alphabets) 
print("Digits", Digits)
