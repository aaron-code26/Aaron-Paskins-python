#section 1

name = "Aaron"
age = 20
height= 6.00
is_student=True

print(name,type(name))
print(age,type(age))
print (height, type(height))
print (is_student, type(is_student))

#Section 2
name= input("what your name:")
User= eval(input("what is your birthyear:"))
year=2026
print("Hello:",name)
print(f"your age:{year-User}",)

#Section 3
Num= input("enter a number:")
Num2=input("enter the second number:")
print(f"your answer is:{float(Num)*float(Num2)}")

#Section 4
print("-------------------")
print("-------------------")
print("RECEIPT")
Book = "Calculus Super Review"
Price = float(30)
quantity= 1
Sum=Price * quantity
print('item:',Book)
print("price:",Price)
print('quantity',quantity)
print("Total is:",Sum)
print("-------------------")

#Section 5
name=(input("Enter your name:"))
Hometown= input("Enter where lived City,State:")
Hobby= input("Named something that like doing:")
Funfact= input ('Say something about you that most people dont know:')
birthyear=int(input('Date of Birth:'))
currentyear=2026


print("Profile:",name)
print("Hometown:",Hometown)
print("Funfact:",Funfact)
print(f"Age:{currentyear-birthyear}",)
