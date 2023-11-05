import Lab2

def test_find_min_max():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 90]

    result = Lab2.find_min_max(input_arr)

    assert (result == test_arr)


def test_calc_average_temperature():
    result = []
    input_arr = [7, 10, 20, 30, 33]
    test_arr = 20.0

    result = Lab2.calc_average_temperature(input_arr)

    assert (result == test_arr)


def test_calc_median_temperature():
    result = []
    input_arr = [7, 10, 20, 30, 33]
    test_arr = 20.0

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test_arr)