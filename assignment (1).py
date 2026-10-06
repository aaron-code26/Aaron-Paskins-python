# Section 1

Name="aaron"
age = 27
height = 6.0
is_student = True

print(Name,type(Name))
print(age,type(age))
print(height,type(height))
print(is_student,type(is_student))

# Section2
User_name=input("Enter your Name:")
User_age=int(input("Enter your current Age:"))
print(f"Hi,{User_name}!,You are approximately {User_age} old")
# f-strings are some favorite way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. This makes it easy to create dynamic strings that include variable values.
#Section3 Type Conversion and f-strings
num1=float(input("Enter your first Number:"))
num2=float(input("Enter your Second Number:"))
sum=float(num1*num2)
print("Sum equals to:",sum)

           
#Section 4 Type conversion and f-strings

Num1=float(input('Enter your first number:'))
Num2=float(input('Enter your second number'))
print(f"{Num1}*{Num2}")

#Section 4 Formatted format
Item = 'Python textbook'
price=float(29.99)
Quantity=2

print("===========================\n")
print("===========================")
print('             Recipt')
print('---------------------------\n')
print(f"Total:,${Quantity*price}\n")
print('---------------------------\n')
print('===========================')


#Section 5 Mini project
profile=input('Enter your Name:')
Hometown=input("Enter your Hometown:")
Hobby=input("Enter a Hobby you like doing:")
Funfact=input("Enter something interesting about you:")
birthyear=int(input("Enter your birthyear:"))
year=2026

print("╔══════════════════════════════╗")
print(f"Profile:{profile}")
print("╚══════════════════════════════╝")
print(f"Hobby:{Hobby}\n")
print(f"Fun Fact:{FunFact}\n")
print(f'Age:{year-birthyear}')
