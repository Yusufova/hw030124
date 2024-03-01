d = ["hApPy"]

def ins(str1):
    for x in d:
        if x.capitalize():
            r = x.lower()
            e = x.replace(x,r)
            return e

ins(str1=str)