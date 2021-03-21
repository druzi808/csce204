#Author: Drew Rafferty

def get_cut_cost(gender, lenght, density):
    basePrice = 0
    
    #price based on gender
    if gender == "m":
        basePrice = 20
    elif gender == "f":
        basePrice = 40
    
    #price based on length
    if length == "l":
        basePrice += 15

    #price based on thickness
    if desnisty == "t":
        basePrice += 15
    
    return basePrice

def get_color_cost(length, density, change):
    basePrice = 50

    if length == 'l':
        basePrice += 20
    if density == "t":
        basePrice += 20
    if change == "l":
        basePrice += 40

    return basePrice

print("Salon Service Calculator")
print("Please fill out the short survey so we can give you a price estimate")

gender = input("Gender (M)ale or (F)emale: ").strip().lower()
hairLength = input("Length (L)ong or (S)hort: ").strip().lower()
hairDensity = input("Density (F)ine or (T)hick: ").strip().lower()

hairCut = input("Do you want your hair cut (Y)es or (N)o: ").lower().strip()
hairColor = input("Do you want your hair colored (Y)es or (N)o: ").lower().strip()

cost = 0

if hairCut == "y":
    cost += get_cut_cost(gender, hairLength, hairDensity)

if hairColor == "y":
    colorChange = input("Will you be going (L)ighter or (D)arker: ").lower().strip()
    cost += get_color_cost(hairLength, hairDensity, colorChange)

#tax
cost *= 1.07

print(f"Your estimated total is ${round(cost,2)}")