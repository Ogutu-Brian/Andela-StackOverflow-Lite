import json
import datetime
from flask import jsonify
from datetime import date
"""The modes will be used to store the data in a data structure"""


class BaseModel:
    """Contains common functionalities across models"""

    def __init__(self, created_at, updated_at):
        self.id = 0
        self.created_at = self.date_formatter(created_at)
        self.updated_at = self.date_formatter(updated_at)

    def date_formatter(self, event_time):
        """
        Formats the created and updated dates
        :params created_at,updated_at
        :return event_time.strftime('%m/%d/%y') 
        """
        return event_time.strftime('%m/%d/%y')


class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, created_at=date.today(),
                 updated_at=date.today(), active="False"):
        super().__init__(created_at, updated_at)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = self.active

    def __str__(self):
        """What gets printed when someone views the user object"""
        return " ".join([self.first_name, self.last_name])


class Question(BaseModel):
    def __init__(self, user, subject, question, created_at=date.today(), updated_at=date.today()):
        self.user = user
        self.subject = subject
        self.question = question
        super().__init__(created_at, updated_at)

    def __str__(self):
        """What gets printed when one views the question object"""
        return self.question


class Answer(BaseModel):
    def __init__(self, user, question, answer, thumbs_up=0, thumbs_down=0, created_at=date.today(),
                 updated_at=date.today()):
        self.user = user
        self.question = question
        self.answer = answer
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        super().__init__(created_at, updated_at)

    def __str__(self):
        """What will be displayed when the answer object is printed"""
        return self.answer
