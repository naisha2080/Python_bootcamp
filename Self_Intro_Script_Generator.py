import datetime

name = input("What is your name ? ")
age = input("What is your age ? ")
city = input("Where do you live ? ")
profession = input("What is your profession ? ")
hobby = input("What is your hobby ? ")

print(f"\nA warm welcome to everyone! My name is {name} and I'm {age} years old. I reside in {city}, and work as a {profession}. I love {hobby} in my free time. Thank you!!")

logged_time = datetime.date.today()
print(f"Logged on: {logged_time} ")