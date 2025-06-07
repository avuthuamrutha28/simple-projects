def load_questions(filename):
    questions = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        if lines[i].startswith('#'):
            question_text = lines[i + 1]
            options = lines[i + 2:i + 6]
            answer_line = lines[i + 6]
            if answer_line.startswith('Ans:'):
                correct_answer = int(answer_line.split(':')[1].strip())
                questions.append({
                    'question': question_text,
                    'options': options,
                    'answer': correct_answer
                })
            i += 7
        else:
            i += 1
    return questions


def run_quiz(questions):
    correct = 0
    wrong = 0
    total = len(questions)

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        while True:
            try:
                user_answer = int(input("Your answer (1-4): ").strip())
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
        if user_answer == q['answer']:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong! The correct answer was option {q['answer']}: {q['options'][q['answer'] - 1]}")
            wrong += 1

    percentage = (correct / total) * 100
    result = "Pass" if percentage >= 50 else "Fail"

    print("\n--- Quiz Results ---")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {correct}")
    print(f"Wrong Answers: {wrong}")
    print(f"Score: {percentage:.2f}%")
    print(f"Result: {result}")


if __name__ == "__main__":
    filename = "question.txt"
    questions = load_questions(filename)
    if questions:
        run_quiz(questions)
    else:
        print("No questions found in the file.")