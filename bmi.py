def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)

    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("You are underweight")

    elif bmi <= 25.0:
        print("You are normal weight")

    elif bmi > 25.0:
        print("You are overweight")


calculate_bmi(1.8, 80)
