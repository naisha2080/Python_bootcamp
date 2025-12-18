"""
Daily Learning Journal Logger

Buold a python script thst sllows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a tiemstamp.

What it does?
-Ask the user what they learned today.
-Add the enrty to a file
-Each entry should include the date and time it was written.
-The journal should append new entries instead of overwriting.

Show a confirmation msg after saving the entry.

"""
import datetime

task = input("What did you learn today ? ").strip()
rating = input("⭐ rate your productivity (1-5, optional  )").strip()

now = datetime.datetime.now() #datetime module has datetime class has now() func
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n 🗓️ {date_str}\n{task}"
if rating:
    journal_entry += f"\nProductivity Rating: {rating}\n"
journal_entry += "\n" + "-" * 70

with open("learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print(f"\n your journal entry has been saved to 'learning_journal.txt' file. ")
