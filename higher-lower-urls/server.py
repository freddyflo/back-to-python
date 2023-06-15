from flask import Flask
import random
app = Flask(__name__)


def random_number():
    return random.randint(0, 9)
    pass

random_guess = random_number()
print(f"Random number: {random_guess}")

@app.route("/")
def guess_number():
    return \
        "<h1>Guess a number between 0 and 9</h1>" \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' 
    pass


@app.route("/guess/<int:user_guess>")
def user_guess(user_guess):
    if user_guess > random_guess:
        return f"<h1>{user_guess} too high. Please again</h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>" 
    elif user_guess < random_guess:
        return f"<h1>{user_guess} too low. Please again</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1>{user_guess} is right</h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    pass





if __name__ == "__main__":
    app.run(debug=True)