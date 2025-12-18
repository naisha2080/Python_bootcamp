"""
Friendship Compatibility Calculator
Build a python script that calculates a fun "compatibility score" between two friends based on their names.

"""
def friendship_score(name1, name2):
    name1,name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2) #common letters
    vowels = set('aieou') #Set is best for fast checking and uniqueness, if it has a vowel or not

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score,100)

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator")
    name1 = input("Enter first friend's name: ")
    name2 = input("Enter first friend's name: ")

    score = friendship_score(name1, name2)

    print(f"\n{score}")

run_friendship_calculator()