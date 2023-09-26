cha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
txt = "cqn lduyarc rb hxda knbc oarnwm".upper()
for k in range(1, 10):
    ans = ""
    for i in txt:
        if i == " ":
            ans += " "
        else:
            index = (cha.index(i) - k) % 26
            ans += cha[index]
    print("k = {0} : {1}".format(k, ans.lower()))