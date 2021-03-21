#Author: Drew Rafferty

def fahr_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def cels_to_fahr(celsius):
    fahrenheit = celsius * 5/9 + 32
    return fahrenheit

def miles_to_kil(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilo_to_miles(kilo):
    miles = kilo * 0.621371
    return miles

print("Conversion Program")
command = int(input(f"""
Enter Type of Conversion: 
1. Fahrenheit to Celsius
2. Celsius to Farhenheit
3. Miles to Kilometers
4. Kilometers to Miles
"""))

value = float(input("Enter value: "))

if command < 1 or command > 4:
    print("Sorry.. Invalid Command")
elif command == 1:
    result = fahr_to_cels(value)
    print(f"{value}F = {round(result,2)}C")
elif command == 2:
    result = cels_to_fahr(value)
    print(f"{value}C = {round(result,2)}F")
elif command == 3:
    result = miles_to_kil(value)
    print(f"{value} Miles = {round(result,2)} Kilometers")
elif command == 4:
    result = kilo_to_miles(value)
    print(f"{value} Kilometers = {round(result,2)} Miles")