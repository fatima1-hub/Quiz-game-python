from questions import questions

user = input("Enter your name: ")
print(f"Hello {user}, welcome to the Knowledge Quiz!")

score = 0
for q in questions:
    print("\n" + q["question"])
    for idx, opt in enumerate(q["options"], start=1):
        print(f"{idx}. {opt}")
    try:
        choice = int(input("Select your option (1-4): "))
        if q["options"][choice - 1] == q["answer"]:
            score += 1
    except (ValueError, IndexError):
        print("Invalid input. Skipping question.")

print(f"\n{user}, your total score is {score}/{len(questions)}")

with open("results.txt", "a") as file:
    file.write(f"{user}: {score}/{len(questions)}\n")
