#3. Write a menu driven program with the following options:
#a. Check whether a given set of three numbers are lengths of an isosceles triangle or not.
#b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not.
#c. Check whether a given set of three numbers are equilateral triangle or not
#d. Exit.

print('1.right angled triangle')
print('2.isosceles triangle')
print('3.equilateral triangle')
print('4.exit')
print('enter your choice')
choice=int(input())
match choice:
    case 1:
        a=int(input('enter first length of triangle:-'))
        b=int(input('enter second length of triangle:-'))
        c=int(input('enter third length of triangle:-'))
        if (a*a+b*b==c*c)or (c*c+b*b==a*a)or (a*a+c*c==b*b):
            print('right angled triangled')
        else:
            print('not a right angled triangled')
         
           
    case 2:
        a=int(input('enter first length of triangle:-'))
        b=int(input('enter second length of triangle:-'))
        c=int(input('enter third length of triangle:-'))
        if (a==b)or (b==c) or (a==c):
            print('isosceles triangle')
        else:
            print('not a isosceles triangle')
          
    case 3:
        a=int(input('enter first length of triangle:-'))
        b=int(input('enter second length of triangle:-'))
        c=int(input('enter third length of triangle:-'))
        if (a==b==c):
            print('Equilateral triangle')
        else:
            print('not a equilateral triangle')
          
    case 4:
        exit()
        
