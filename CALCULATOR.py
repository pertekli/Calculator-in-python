
user = input("enter your number: ")
op = input("select any operator\n1.for addition\n2.for subtraction\n"
"3.for multiply\n4.for divide\n5.for exponantial\n6.for floor division\n7.for modulus: ")
user2 = input("now enter your second number: ")
if op == "1":
    print("your answer is",int(user)+int(user2))
elif op == "2":
    print("your answer is",int(user)-int(user2))
elif op == "3":
    print("your answer is",int(user)*int(user2))
elif op == "4":
    print("your answer is",int(user)/int(user2))
elif op == "5":
    print("your answer is",int(user)**int(user2))
elif op == "6":
    print("your answer is",int(user)//int(user2))
elif op == "7":
    print("your answer is",int(user)%int(user2))
else:
    print("enter valid operator")

