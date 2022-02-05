rivers = {
    "Nile":"Egypt",
    "Amazon":"Brazil",
    "Yangtze":"China"
}
for i, g in rivers.items():
    print(f"The {i} runs throung {g}")
for i in rivers.keys():
    print(f"River: {i}")
for i in rivers.values():
    print(f"Countries: {i}")