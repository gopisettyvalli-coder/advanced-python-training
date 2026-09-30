print("========== Simple Calaculator ==============")

num_01=int(input("Enter  first number:"))
num_02=int(input("Enter second number:"))
operator=input("Enter the operator(+,-,*,/):")

if operator=="+":
    result= num_01+num_02
    print("Result:", result)

elif operator=="-":
    result=num_01-num_02
    print("Result:", result)

elif operator=="*":
    result=num_01*num_02
    print("Result:", result)

elif operator=="/":
    result=num_01/num_02
    print("Result:", result)

else:
    print("Perform valid operation")