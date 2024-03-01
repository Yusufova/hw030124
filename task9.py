edmund = ["anime", "meme", "vines", "roasts", "Danny DeVito"]
w = input("What do u wanna watch?")
for x in edmund:
    if x in w:
        print("NO!")
    elif x not in edmund:
        print("Safe watching!")