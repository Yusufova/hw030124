r = ["aBFDc"]

def func(str1):
    res = 0
    for x in str1:
        if x.islower():
            res += x
            print(res)
            return res

func(str1=str)