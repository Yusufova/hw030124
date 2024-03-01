#Modul
import time
import random




dmy = "25.02.2024"



# lst = [1, 2, 3, 4, 5, 6, 7]
# for x in lst:
#     print(x)
#     time.sleep(1)
#
# times = time.strftime("%H:%M:%S")
# t1 = time.strftime("%d.%m.%y")
# print(times, t1)
# result = 0
# for x in range(1, 101):
#     if x == 81:
#         break
#     result += x
# print(x)



#dublikatlarni ochirish
# lst = [1, 27, 2, 9, 2, 3, 6, 3]
# lst1 = []
# for x in lst:
#     if x not in lst1:
#         lst1.append(x)
# print(lst1)


# lst = [1, 27, 2, 9, 2, 3, 6, 3]
# lst1 = []
# for x in lst:
#     if x in lst1:
#         print("yes")
#     if x not in lst1:
#         lst1.append(x)
# print(lst1)

def are_anagrams(string1, string2):
    if len(string1) != len(string2):
        return False


    return sorted(string1) == sorted(string2)

print(are_anagrams("cristian", "cristina"))
print(are_anagrams("dave barry", "ray adverb"))
print(are_anagrams("nope", "note"))




