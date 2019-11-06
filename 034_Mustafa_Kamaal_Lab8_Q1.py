f = open("main.txt","r")
count1=0
count2=0
for i in f:
    i = f.readline() 
    if(i.isdigit() == True):
        count1=count1+1
    count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)
f.close()
