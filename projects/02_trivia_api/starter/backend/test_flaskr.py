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
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'caryn', 'mypass', 'localhost:5432', self.database_name
        )
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
    # def test_categories(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)
    #     print(data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["categories"])

    # def test_404_could_not_get_categories(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data['message'], 'Resource not Found')
    # def test_get_questions(self):
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['message'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(data["current_category"])
    #     self.assertTrue(data["categories"])


    



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()