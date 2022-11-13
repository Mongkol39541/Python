num1 = input("f(x) = ")
num2 = input("g(x) = ")
txt = input("operater = ")

if num1 == '0' and num2 == '0' and txt == '/':
    print("Indeterminate Form Type 0/0")
elif num1 == '1/0' and num2 == '1/0' and txt == '/':
    print("Indeterminate Form Type inf/inf")
elif num1 == '0' and num2 == '1/0' and txt == 'x':
    print("Indeterminate Form Type 0xinf")
elif num1 == '1/0' and num2 == '1/0' and txt == '-':
    print("Indeterminate Form Type inf-inf")
elif num1 == '0' and num2 == '0' and txt == '^':
    print("Indeterminate Form Type 0^0")
elif num1 == '1' and num2 == '1/0' and txt == '^':
    print("Indeterminate Form Type 1^inf")
elif num1 == '1/0' and num2 == '0' and txt == '^':
    print("Indeterminate Form Type inf^0")
else:
    print("No Indeterminate Form")