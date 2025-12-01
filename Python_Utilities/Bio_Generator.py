import textwrap

name = input("What is your name: ").strip()
profession = input("What is your profession ? ").strip()
passion = input("What is your passion or goal in one line ? ").strip()
emoji = input("What is your favourite emoji ? ").strip()
website = input("Your website or handle ? ").strip()

print("\nChoose your style: ")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style = input("Enter 1, 2 or 3: ")

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession}\n{emoji} {passion}\n{website}" 
    elif style == "2":
        return f"{emoji} {name}\n{profession}\n{passion}\n{website}"
    elif style == "3":
        return f"{emoji*3}\n{name} {profession}\n{passion}\n{website}\n{emoji*3}"
    
bio = generate_bio(style)

print("*" * 50)
print("Your stylish Bio: ")
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file ? (y/n): ").lower()

if save == 'y':
    filename = f"{name.lower().replace(" ","_")}_bio_txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File saved")
