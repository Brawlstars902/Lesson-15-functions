def add(x,y):
    return(x,'+',y,'=',float(x)+float(y))
def subtract(x,y):
    return (x,'-',y,'=',float(x)-float(y))
def divide(x,y):
    return (x,'/',y,'=',float(x)/float(y))
def multiply(x,y):
    return (x,'x',y,'=',float(x)*float(y))

print('Welcome to the calculator')
z=input('Do you want to Add, Subtract, Divide or Multiply?\n')
if str(z)=="Add":
    x=input('Enter the first number you would like to add.  :  ')
    y=input('Enter the second number you would like to add.  :  ')
    print(add(x,y))
if str(z)=="Subtract":
    x=input('Enter the first number you would like to subtract by.  :  ')
    y=input('Enter the second number you would like to subtract from the previous number.  :  ')
    print(subtract(x,y))
if str(z)=="Divide":
    x=input('Enter the first number you would like to divide by.  :  ')
    y=input('Enter the second number you would like to divide from the previous number.  :  ')
    print(divide(x,y))
if str(z)=="Multiply":
    x=input('Enter the first number you would like to multiply.  :  ')
    y=input('Enter the second number you would like to multiply.  :  ')
    print(multiply(x,y))