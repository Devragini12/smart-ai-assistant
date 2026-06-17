from flask import Flask, render_template, request

app = Flask(__name__)

chat_history = []

def chatbot_response(user):

    user = user.lower()

    if "hello" in user or "hi" in user:
        return "Hello! 👋 How can I help you today?"

    elif "python" in user:
        return "Python is a powerful and beginner-friendly programming language."

    elif "motivate me" in user:
        return "Success is the sum of small efforts repeated every day."

    elif "sad" in user:
        return "Tough times don't last, but tough people do."

    elif "happy" in user:
        return "That's amazing! Keep smiling 😊"

    elif "who created you" in user:
        return "I was built by Rags as a Python project."

    elif "bye" in user:
        return "Goodbye! Have a productive day."

    return "Interesting. Tell me more."

@app.route("/", methods=["GET", "POST"])
def home():

    global chat_history

    if request.method == "POST":

        user_message = request.form["message"]

        bot_response = chatbot_response(user_message)

        chat_history.append(
            {"user": user_message,
             "bot": bot_response}
        )

    return render_template(
        "index.html",
        chats=chat_history
    )

        import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
