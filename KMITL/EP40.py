"""This is DocString"""

import re

def main():
    """This is DocString"""
    txt = str(input())
    if txt.find('"') != -1:
        txt = txt.replace('"', "")
        remu = re.compile('[A-z]')
        num = remu.sub('', txt)
        num = int(num)
        new_txt = chr(num)
        txt = txt.replace(str(num), str(new_txt))
        print(txt)
    else:
        print("No error")
main()
