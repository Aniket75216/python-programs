# Abstract question evaluation

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        return answer == "A"


class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        return answer.lower() == "true"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        return len(answer.strip()) > 10


print("MCQ:", MCQQuestion().evaluate_answer("A"))
print("True/False:", TrueFalseQuestion().evaluate_answer("True"))
print("Descriptive:", DescriptiveQuestion().evaluate_answer("This is an answer"))\n