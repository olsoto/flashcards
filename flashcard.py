class Flashcard:
    def __init__(self, question, answer):
        self.answer = answer
        self.question = question

    def get_question(self):
        return f"{self.question}"

    def get_answer(self):
        return f"{self.answer}"

    def __str__(self):
        return f"{self.question} - {self.answer}"