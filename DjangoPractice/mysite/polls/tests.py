from django.test import TestCase
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


# Create your tests here.
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        returns False for questions whose pub_date is in the future; else True
        :return: boolean
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        should return False for questions whose pub_date is older than 1 day (old questions)
        :return: Boolean
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        should return False for questions whose pub_date is within 1 day
        :return: Boolean
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# TODO: add test class for each model & view
# TODO: make a method for each condition to be tested


