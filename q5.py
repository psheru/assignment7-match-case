#5. Write a program which takes a number from user. Print Saurabh Shukla if the number
#is even, print Prateek Jain if the number is negative odd number and print Aditya
#Choudhary if number is positive odd number.

x=int(input('enter any number:-'))
match x:
   case x if x%2==0:
       print('saurabh shukla')
   case x if x<0 and x%2:
       print('Prateek Jain')
   case x if x>0 and x%2:
       print('Aditya choudhary')
