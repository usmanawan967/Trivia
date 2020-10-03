import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "databasename"
        self.database_path = "postgresql://postgres:usman@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
 """
    def test_delete_question_inrange(self):
        question = Question(question='usman', answer='awan',difficulty=1, category=4)
        question.insert()
        id = question.id
        res = self.client().delete(f'/questions/{id}')
        data = json.loads(res.data)
        print("test4")
        question = Question.query.filter( Question.id == question.id).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], id)

    def test_422_deleting_question_not_inrange(self):
        res = self.client().delete('/questions/345')
        data = json.loads(res.data)
        print("test5")
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_select_category(self):
        res = self.client().get('/categories')
        print("test2")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_404_requesting_not_in_category(self):
        res = self.client().get('/categories/340')
        print("test3")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    def test_get_paginated_questions_inrange(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        print("usmanawan")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        ''''
        self.assertTrue(len(data['categories']))
         '''

    def test_404_requesting_invalid_page(self):
        res = self.client().get('/questions?page=1000')
        print("alviawan")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

"""







# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()