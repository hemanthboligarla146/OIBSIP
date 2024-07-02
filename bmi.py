def calculate_bmi(weight, height):
    bmi= weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight",bmi
    elif 18.5 <= bmi < 25:
        return "Normal weight",bmi
    elif 25 <= bmi < 30:
        return "Overweight",bmi
    else:
        return "Obesity",bmi



def main():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    category,bmi = calculate_bmi(weight, height)


    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
