name="Sneha"
print("name",name,type(name))
rollno=207
print("rollno",rollno,type(rollno))
percentage=90.80
print("percentage",percentage,type(percentage))

#Read a number and if a multiple of 3 print multiple of 3 of 5 then print of 5 and if of both 3 and 5 then print of 3 and 5 else print invalid

n=int(input("Enter a number:"))
if(n%3==0 and n%5==0):
    print("The number is multiple of both 3 and 5.")
elif(n%3==0):
    print("The number is multiple of 3.")
elif(n%5==0 ):
    print("The number is multiple of 5.")
else:
    print("Invalid number.")


#print 1 to 100 then all odd and even numbers between 1 to 100.

for i in range(1,101):
    print(i,end=' ')
print()

for i in range(1,101,2):
    print(i,end=' ')
print()

for i in range(0,101,2):
    print(i,end=' ')
print()


#print 100 to 1

for i in range(100,0,-1):
    print(i,end=' ')
print()

for i in range(100,0,-2):
    print(i,end=' ')
print()

for i in range(99,0,-2):
    print(i,end=' ')
print()

for i in range(100,1,-2):
    print(i,end=' ')
print()

#Write a program useing for loop to print 1 to 100 but break at 50

for i in range(1,101):
    if(i==50):
        break
        print(i,end=' ')
    else:
        print(i,end=' ')

for i in range(1,101):
    if(i==50):
        continue
    print(i,end=' ')


#Pass is like a null statement.
for i in range(1,101):
    if(i==50):
        pass
    print(i,end=' ')




        


   
    
