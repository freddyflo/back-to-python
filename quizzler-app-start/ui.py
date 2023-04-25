from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(150, 125, text="Sample Question", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR) 
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.false_btn = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)

        self.true_btn.grid(row=2,column=0)
        self.false_btn.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        pass

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        pass

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        pass

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
        pass

    pass