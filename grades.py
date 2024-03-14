print("Enter your obtained marks of following subjects: ")
SAD=int(input("SAD: "))
DSA=int(input("DSA: "))
WEB=int(input("WEB: "))
OOP=int(input("OOP: "))

total= SAD+DSA+WEB+OOP
percentage= total/4
print("Percentage =", percentage,"%")

if percentage>80:
    print("Grade: A+")
elif percentage>=70 and percentage<=79:
    print("Grade: A")
elif percentage>=60 and percentage<=69:
    print("Grade: A-")
elif percentage>=50 and percentage<=59:
    print("Grade: B")
elif percentage>=40 and percentage<=49:
    print("Grade: B-")
else:
    print("Fail")