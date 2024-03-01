r = ["I have never seen a thin person drinking Diet Coke."]
d = ["a,e,u,i,o"]
def vowel():
    for x in r:
        for y in d:
          if x == y:
             x.remove(x,y)
             return x

vowel()