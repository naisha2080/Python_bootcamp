"""
Created a python script that takes a message and adds emojis after specific keywords to make it more expressive.


"""
# get a dictionary
emoji_map = {
    "love": "❤️",
    "happy": "😊",
    "sad": "😔",
    "code": "💻",
    "music":"🎵",
    "sunny": "🌞", 
}

# get a user message
message = input("Enter your message: ")

updated_word = []

# process each word
for word in message.split(): #Return a list of the substrings in the string.
    cleaned_word = word.lower().strip(".,!?")
    emoji = emoji_map.get(cleaned_word, "")
    if emoji:
        updated_word.append(f"{word} {emoji} ")
    else:
        updated_word.append(word)

updated_message = " ".join(updated_word) #the list (updated_message) is now a string
print("\n Enhanced message: ")
print(updated_message)
