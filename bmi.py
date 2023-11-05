def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)

    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("You are underweight")
        return -1

    elif bmi <= 25.0:
        print("You are normal weight")
        return 0

    elif bmi > 25.0:
        print("You are overweight")
        return 1


calculate_bmi(1.65, 80)
