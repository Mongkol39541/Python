ans = input()
if ans.isnumeric():
    ans = int(ans) * 3
else:
    if ans.islower():
        ans = (ans + " ") * 3
    else:
        ans = float(ans)/3
print(ans)