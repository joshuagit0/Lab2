import statistics


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    numlist = input().split(",")
    numlist = [float(string) for string in numlist]
    return numlist


def find_min_max(templist):
    print("find_min_max")
    minmaxTemp = [min(templist), max(templist)]
    return minmaxTemp


def sort_temperature(templist):
    print("sort_temperature")
    templist = sorted(templist)
    return templist


def calc_average_temperature(templist):
    print("calc_average_temperature")
    total = 0
    for x in templist:
        total += x

    average = total/len(templist)
    return average


def calc_median_temperature(templist):
    print("calculate_median_temperature")
    return statistics.median(sorted(templist))

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(calc_average_temperature(num_list))
    print(find_min_max(num_list))
    print(sort_temperature(num_list))
    print(calc_median_temperature(num_list))


if __name__ == "__main__":
    main()
