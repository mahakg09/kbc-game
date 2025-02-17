from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    "What is the capital of India?",
    "Who wrote the national anthem?",
    "Which planet is known as the Red Planet?",
    "Who is known as the Father of Computer Science?",
    "Which is the largest ocean on Earth?",
    "Which is the smallest country in the world?"
]

options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Subhash Chandra Bose", "D. Jawaharlal Nehru"],
    ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
    ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"],
    ["A. Atlantic Ocean","B. Indian Ocean","C. Arctic Ocean","D. Pacific Ocean"],
    ["A. Monaco", "B. Vatican City", "C. San Marino", "D. Liechtenstein"]
]

answers = ["B", "A", "C", "B","D","B"] 
prize_money = [1000, 3000, 5000, 7000,9000,11000]  

@app.route("/")
def home():
    return redirect(url_for("play", question_num=0, total_prize=0))

@app.route("/play/<int:question_num>/<int:total_prize>", methods=["GET", "POST"])
def play(question_num, total_prize):
    if question_num >= len(questions):  # If all questions are answered
        return render_template("game_over.html", total_prize=total_prize)

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = answers[question_num]

        if user_answer == correct_answer:
            total_prize += prize_money[question_num]
            feedback = f"Correct! You won ₹{prize_money[question_num]}."
        else:
            feedback = f"Oops! Incorrect. The correct answer is {correct_answer}."

        return render_template("game.html", question_num=question_num, total_prize=total_prize,
                               question=questions[question_num], options=options[question_num],
                               feedback=feedback)

    return render_template("game.html", question_num=question_num, total_prize=total_prize,
                           question=questions[question_num], options=options[question_num],
                           feedback="")

if __name__ == "__main__":
    app.run(debug=True)
