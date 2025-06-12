class Question:
    def __init__(self, question_text, alternatives, correct_answer):
        self.question_text = question_text
        self.alternatives = alternatives
        self.correct_answer = correct_answer

    def display_question(self):
        print(f"\n{self.question_text}")
        for i, alternative in enumerate(self.alternatives, 1):
            print(f"{i}. {alternative}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


def run_quiz():
    # Definizione delle domande
    questions = [
        Question(
            question_text="Qual è la capitale della Francia?",
            alternatives=["Roma", "Parigi", "Londra", "Mosca"],
            correct_answer=2
        ),
        Question(
            question_text="Quale pianeta è più vicino al Sole?",
            alternatives=["Venere", "Terra", "Mercurio", "Marte"],
            correct_answer=3
        ),
        Question(
            question_text="Chi ha scritto 'I Promessi Sposi'?",
            alternatives=["Dante Alighieri", "Alessandro Manzoni",
                          "Giovanni Boccaccio", "Giacomo Leopardi"],
            correct_answer=2
        )
    ]

    score = 0
    total_questions = len(questions)

    print("=== QUESTIONARIO ===")
    print(
        f"Rispondi alle seguenti {total_questions} domande inserendo il numero della risposta corretta.")

    for i, question in enumerate(questions, 1):
        print(f"\n--- Domanda {i} ---")
        question.display_question()

        # Richiesta input utente
        while True:
            try:
                user_answer = int(input("\nInserisci la tua risposta (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Per favore inserisci un numero tra 1 e 4.")
            except ValueError:
                print("Per favore inserisci un numero valido.")

        # Controllo risposta
        if question.check_answer(user_answer):
            print("✓ Corretto!")
            score += 1
        else:
            print(
                f"✗ Sbagliato! La risposta corretta era: {question.correct_answer}. {question.alternatives[question.correct_answer-1]}")

    # Risultato finale
    print(f"\n=== RISULTATO FINALE ===")
    print(f"Hai risposto correttamente a {score} domande su {total_questions}")
    print(
        f"Punteggio: {score}/{total_questions} ({(score/total_questions)*100:.1f}%)")

    if score == total_questions:
        print("🎉 Perfetto! Hai risposto a tutte le domande correttamente!")
    elif score >= total_questions * 0.7:
        print("👍 Bravo! Buon risultato!")
    else:
        print("📚 Continua a studiare, puoi fare meglio!")


# Esecuzione del questionario
if __name__ == "__main__":
    run_quiz()
