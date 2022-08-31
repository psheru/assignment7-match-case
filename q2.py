#2. Write a menu driven program to perform following operations - Addition, Subtraction,
#Multiplication, Division.

print('1.Addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')
print('enter your choice')
choice=int(input())
match choice:
    case 1:
        a=int(input('enter first number:-'))
        b=int(input('enter second number:-'))
        c=a+b
        print("sum of two number is:-",c)
    case 2:
        a=int(input('enter first number:-'))
        b=int(input('enter second number:-'))
        c=a-b
        print("difference of two number is:-",c)
    case 3:
        a=int(input('enter first number:-'))
        b=int(input('enter second number:-'))
        c=a*b
        print("multiplication of two number is:-",c)
    case 4:
         a=int(input('enter first number:-'))
         b=int(input('enter second number:-'))
         c=a/b
         print("division of  number is:-",c)
