"""This is DocString"""

def temperature_cf(num):
    """This is DocString"""
    num = (num * (9 / 5)) + 32
    return "Fahrenheit = " + str('%.2f' %num)

def temperature_ck(num):
    """This is DocString"""
    num = num + 273.15
    return "Kelvin = " + str('%.2f' %num)

def temperature_cr(num):
    """This is DocString"""
    num = (num + 273.15) * (9 / 5)
    return "Rankine = " + str('%.2f' %num)

def temperature_fc(num):
    """This is DocString"""
    num = (num - 32) * (5  / 9)
    return "Celsius = " + str('%.2f' %num)

def temperature_fk(num):
    """This is DocString"""
    num = (num + 459.67) * (5  / 9)
    return "Kelvin = " + str('%.2f' %num)

def temperature_fr(num):
    """This is DocString"""
    num = num + 459.67
    return "Rankine = " + str('%.2f' %num)

def temperature_kc(num):
    """This is DocString"""
    num = num - 273.15
    return "Celsius = " + str('%.2f' %num)

def temperature_kf(num):
    """This is DocString"""
    num = (num * (9 / 5)) - 459.67
    return "Fahrenheit = " + str('%.2f' %num)

def temperature_kr(num):
    """This is DocString"""
    num = num * (9 / 5)
    return "Rankine = " + str('%.2f' %num)

def temperature_rc(num):
    """This is DocString"""
    num = (num - 491.67) * (5 / 9)
    return "Celsius = " + str('%.2f' %num)

def temperature_rf(num):
    """This is DocString"""
    num = num - 459.67
    return "Fahrenheit = " + str('%.2f' %num)

def temperature_rk(num):
    """This is DocString"""
    num = num * (5 / 9)
    return "Kelvin = " + str('%.2f' %num)

def temperature(txt, num):
    """This is DocString"""
    ans = num
    if txt == "C→C":
        ans = "Celsius = " + str('%.2f' %num)
    elif txt == "F→F":
        ans = "Fahrenheit = " + str('%.2f' %num)
    elif txt == "K→K":
        ans = "Kelvin = " + str('%.2f' %num)
    elif txt == "R→R":
        ans = "Rankine = " + str('%.2f' %num)
    return ans

def main():
    """This is DocString"""
    num = float(input())
    txt = str(input())
    ans = num
    if txt == "C→F":
        ans = temperature_cf(num)
    elif txt == "C→K":
        ans = temperature_ck(num)
    elif txt == "C→R":
        ans = temperature_cr(num)
    elif txt == "F→C":
        ans = temperature_fc(num)
    elif txt == "F→K":
        ans = temperature_fk(num)
    elif txt == "F→R":
        ans = temperature_fr(num)
    elif txt == "K→C":
        ans = temperature_kc(num)
    elif txt == "K→F":
        ans = temperature_kf(num)
    elif txt == "K→R":
        ans = temperature_kr(num)
    elif txt == "R→C":
        ans = temperature_rc(num)
    elif txt == "R→F":
        ans = temperature_rf(num)
    elif txt == "R→K":
        ans = temperature_rk(num)
    ans = temperature(txt, ans)
    print(ans)
main()
