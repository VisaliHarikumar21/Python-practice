# quiz game

print("==============================================")
print("                 QUIZ GAME                   ")
print("==============================================")

questions = (
"How many elements are there in the periodic table?",
"Which animal lays the largest eggs?",
"What is the most abundant gas in earth's atmosphere?",
"How many bones are there in the human body?",
"Which planet in the solar system is the hottest"
)

options = (
("A: 116", "B: 117", "C: 118", "D: 119"),
("A: Whale", "B: Crocodile", "C: Elephant", "D: Ostrich"),
("A: Nitrogen", "B: Oxygen", "C: CO2", "D: Hydrogen"),
("A: 206", "B: 207", "C: 208", "D: 209"),
("A: Mercury", "B: Venus", "C: Earth", "D: Mars"),
)

answers = ("C", "D", "A", "A", "B")

total = 0
qn_number = 0
guesses = []

for question in questions:
    print(f"{qn_number+1}. {question}")
    for option in options[qn_number]:
        print(option)
    guess = input("Enter your guess: ").upper()
    if guess == answers[qn_number]:
        print("CORRECT 🎊")
        total += 1
    else:
        print(f"Incorrect ☹️. The correct answer is {answers[qn_number]}")
    guesses.append(guess)
    print()
    qn_number += 1

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Your guess: ", end="")
for guess in guesses:
    print(guess, end =" ")
print()

print("Correct answers: ", end="")
for answer in answers:
    print(answer, end =" ")
print()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print()
print(f"You got {total} right!")
print(f"Your total score is {int((total / len(questions)) * 100)}%")