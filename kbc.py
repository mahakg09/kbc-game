questions=[
    "what is the capital of india??",
    "who wrote the national anthem?",
    "which planet is known as the red planet?",
    "who is known as the father of computer science?"
    ]
options=[
    ["A.Mumbai","B.Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Subhash Chandra Bose", "D. Jawaharlal Nehru"],
    ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
    ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"]
    ]
answers=["B", "A", "C", "B"]
prize_money=[1000,3000,5000,7000]
total=0
print("Welcome to KBC!!")

for i in range(len(questions)):
    print(f"Question No. :{i+1}->:{questions[i]}")
    for option in options[i]:
        print(option)
        
    user_answer=input("what is your answer (a/b/c/d)").strip().upper()
    if user_answer == answers[i]:
        total=total+prize_money[i]
        print(f"correct!! you won Rs.{prize_money[i]}.Total Prize: Rs.{total}")
    else:
        print(f"wrong answer!!.The correct answer is{answers[i]}.")
        break
print(f"Game over!!You Won a Total of Rs.{total}")