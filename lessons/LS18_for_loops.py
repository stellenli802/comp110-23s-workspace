"""for loop examples and practices"""

#Example 2
pets: list[str] = ["Louie", "Bo", "Bear"]
for i in pets:
    print(f"Good boy, { i }!")

#Using range() in a for loop
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
#the i in this for loop is now the index of the list
#rather than element in the for loop above
for i in range(0,3):
    print(f"{ i }: { names[i] }")

