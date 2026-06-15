from colorama import init, Fore
from datetime import datetime
import random
import os

init(autoreset=True)

# Load user name
user_name = ""

if os.path.exists("user_data.txt"):
    with open("user_data.txt", "r") as file:
        user_name = file.read().strip()

greetings = [
    "Hello! 👋",
    "Hey there!",
    "Hi! Nice to see you.",
    "Greetings!"
]

motivation = [
    "Keep going, you're improving every day!",
    "Small progress is still progress.",
    "Every expert was once a beginner.",
    "Consistency beats talent when talent doesn't work."
]

fallbacks = [
    "Interesting. Tell me more.",
    "Can you explain that differently?",
    "I'm still learning. Could you elaborate?",
    "That's something I don't know yet."
]

print(Fore.CYAN + "=" * 50)
print(Fore.CYAN + "🤖 SMART AI ASSISTANT")
print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "Type 'help' to see commands.\n")

while True:

    user = input(Fore.YELLOW + "You: ").lower().strip()

    # Save chat history
    with open("chat_history.txt", "a") as history:
        history.write(f"You: {user}\n")

    if user in ["hello", "hi", "hey"]:

        response = random.choice(greetings)

    elif "my name is" in user:

        user_name = user.replace("my name is", "").strip()

        with open("user_data.txt", "w") as file:
            file.write(user_name)

        response = f"Nice to meet you, {user_name}!"

    elif "what is my name" in user:

        if user_name and user_name != "Unknown":
            response = f"Your name is {user_name}."
        else:
            response = "I don't know your name yet."

    elif user == "time":

        current_time = datetime.now().strftime("%H:%M:%S")
        response = f"Current time is {current_time}"

    elif "python" in user:

        response = "Python is a powerful and beginner-friendly programming language."

    elif "motivate me" in user:

        response = random.choice(motivation)

    elif "happy" in user:

        response = "That's great to hear! 😊"

    elif "sad" in user:

        response = "Don't give up. Tough times never last, but tough people do."

    elif "tired" in user:

        response = "Take a break, drink some water, and recharge."

    elif user == "help":

        response = """
Available Commands
------------------
hello
hi
hey
my name is <name>
what is my name
time
python
motivate me
happy
sad
tired
help
bye
"""

    elif user == "bye":

        response = "Goodbye! Keep coding 🚀"

        print(Fore.GREEN + "Bot: " + response)

        with open("chat_history.txt", "a") as history:
            history.write(f"Bot: {response}\n")

        break

    else:

        response = random.choice(fallbacks)

    print(Fore.GREEN + "Bot: " + response)

    with open("chat_history.txt", "a") as history:
        history.write(f"Bot: {response}\n")