"""The main data structure"""
from v1.data_store.collections import UserCollection, QuestionCollection, AnswerCollection


class StackOverflowLiteDB:
    def __init__(self):
        """Create a collection for each model"""
        self.users = UserCollection()
        self.answers = AnswerCollection()
        self.questions = QuestionCollection()

    def clear(self):
        """Clear all data in the collections"""
        self.users.clear()
        self.answers.clear()
        self.questions.clear()
