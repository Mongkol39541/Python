"""This is DocString"""

def function_f(num_x):
    """This is DocString"""
    ans = 2 * num_x
    return ans

def function_g(num_x):
    """This is DocString"""
    ans = (3 * (num_x ** 4)) - (num_x ** 3) + (2 * (num_x ** 2)) + 10
    return ans

def function_h(num_x, num_y, num_z):
    """This is DocString"""
    ans = ((num_z + num_x) ** 2) - (num_x * num_y) + (num_y ** 2)
    return ans

def function_i(num_a, num_b, num_c, num_d):
    """This is DocString"""
    ans_up = (num_a ** 2) + (num_b ** 2) - (num_c ** 2)
    ans_low = (num_d ** 2) - (2 * num_a * num_d) + (2 * num_a)
    ans = ans_up / ans_low
    return ans

def main():
    """This is DocString"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
    ans_1 = function_f(function_f(num_a))
    ans_2 = function_g(function_f(num_a - num_b))
    ans_3 = function_h(function_f(num_a + num_b), function_f(num_a + num_c), \
function_g(function_f(num_d ** 2)))
    ans_4 = function_i(function_h(function_f(num_a + num_b), function_f(num_a - num_c), \
function_g(function_f(num_d ** 2))), function_g(function_f(num_a - num_b)), \
function_f(function_f(function_f(function_f(function_f(num_c))))), num_d ** 8)
    print(ans_1)
    print(ans_2)
    print(ans_3)
    print(ans_4)
main()
