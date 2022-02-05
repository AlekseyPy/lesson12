# user = {
#     "u1": "human"
#     "u2": "superhero"
#     "u3": "wolf"
#     "u4": "Broccoli"
# }
# print (user)
# print (user["u3"])
# user["u5"] = "Programmer"
# print(user)

# user = {}
# user["u1"] = "superhero"
# user["u2"] = "human"
# user["u3"] = "broccoli"
# print(user)
# user["u2"] = "wolf"
# print(user)
# a = input("Enter your speed(medium/fastest/else):")
# info = {"x": 10, "y": 30, "player_speed":a}
# if  info["player_speed"] == "medium":
#     x_increment = 2
# elif info["player_speed"] == "fastest":
#     x_increment = 10
# else:
#     x_increment = 1
# info["x"] += x_increment
# print(f"Новая позиция игрока будет: {info["x"]})

# language = {
#     "aleksey":"python",
#     "ilya":"c++",
#     "xlebich":"js",
#     "vanya":"python(crutoy)",
#     "nikiton":"php"
#     }
# print(f"Я люблю программировать на {language['aleksey'].title()} языке программирования")
# for i, g in language.items():
#     print(f"Меня зовут {i.title()}.Я люблю программировать на {g} языке программирования")

# language = {
#     "aleksey":"python",
#     "ilya":"c++",
#     "xlebich":"js",
#     "vanya":"python(crutoy)",
#     "nikiton":"php"
#     }
# print(f"Я люблю программировать на {language['aleksey'].title()} языке программирования")
# for i in language.values():
#     print(f"Меня зовут {i.title()}.Я люблю программировать на языке программирования")


# info1 = {
#     "color":"red",
#     "points":"5"
# }
# info2 = {
#     "color":"yellow",
#     "points":"15"
# }
# info3 = {
#     "color":"green",
#     "points":"25"
# }

# list1 = [info1,info2,info3]

# for i in list1:
#     print(i)



list_huge = []
for i in range (30):
    info = {
    "color":"yellow",
    "points":"15"
    }
    list_huge.append(info)
    print(f"{list_huge}")
for x in list_huge:
    print(x)
    print(f"Количсетво игроков {len(list_huge)}")
for p in list_huge[0:3]:
    if p["color"] == "yellow":
        p["color"] = "blue"
        p["points"] = 100
for x in list_huge:
    print(x)
print(f"кол-во игроков {len(list_huge)}")