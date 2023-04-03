"""LS19-Dictionaries practice."""

#Empty dict
ice_cream: dict[str, int] = dict()

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#Adding elements
ice_cream["mint"] = 3

#Removing elements
ice_cream.pop("chocolate")

print(ice_cream)

#Accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Modifying
ice_cream["vanilla"] += 1 
print(f"After adding 1 vanilla: {ice_cream}")
print(f"Updated number of vanilla orders: {ice_cream['vanilla']}")

#Length of ice_cream dict
len(ice_cream)

#Check if key in dictionary (returns bool)
print("chocolate" in ice_cream)
print("mint" in ice_cream)



#DICTS IN MEMORY + FOR LOOPS

grades: dict[str, str] = {"Alyssa": "A", "Aksana": "A", "Regis": "B"}

for student in grades:
    print(grades[student])