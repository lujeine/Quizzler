from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(self.window, text=f"Score:{self.score}", font=("Helvetica", 20), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=200, text="some question", fill=THEME_COLOR, font=("Arial", 20,"italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=true_image, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)
        self.incorrect_button = Button(image=false_image, command=self.false_pressed)
        self.incorrect_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="END"
                                   )
            self.correct_button.config(state=DISABLED)
            self.incorrect_button.config(state=DISABLED)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

