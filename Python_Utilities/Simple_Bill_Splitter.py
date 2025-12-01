"""Write a python script thatbhelps split a bill evenly between friends"""

members = int(input("How many people are in the group? "))
names = []
for member in range(1, members+1):
    name = input(f"What is the name of member {member}? ").split()
    names.append(name)

total_bill = int(input("What is the total bill? "))
split_bill = total_bill/members
rounded_split_value = format(split_bill,".2f")

print("\n"+"*"*40)
print(f"Each member will pay - {rounded_split_value}")
print("Final output: ")
for name in names:
    print(f"  {name[0]} owes {rounded_split_value}")
print("*"*40)

