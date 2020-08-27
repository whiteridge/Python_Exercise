# Wap to create a faulty calculator of specific input such as..
# 5*5 = 555 , 56+9 =64, 56/9=4
print("Enter first number")
num1=int(input())
print("Enter second number")
num2=int(input())
print("Select any one of it:(+,-,*,/,%,**)")
print("enter your operator")
op=input()
if op=='+' and num1==59 and num2==9 :
    print("64")
elif op=='*' and num1==5 and num2==5 :
    print("55")
elif op == '/' and num1 == 56 and num2 ==6:
    print("4")
elif op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/' :
    print(num1/num2)
elif op=='%' :
    print(num1%num2)
elif op=='**':
    print(num1**num2)
else:
    print("Invalid Input")