import os
from flask import Flask, request, abort, jsonify, json
from sqlalchemy.sql.expression import true
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1)* QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection] 
  current_question = questions[start:end]

  return current_question

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  
  
  @app.after_request
  def after_request(response):
      response.headers.add(
          "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
      )
      response.headers.add(
          "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
      )
      return response

  
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    dictCategories = {}

    for category in categories:
      dictCategories[category.id] = category.type
  
    if len(categories) ==0:
      abort(404)

    return jsonify({
        'success': True,
        'categories':dictCategories
    })


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/questions')
  def get_questions():
    questions = Question.query.all()
    current_questions = paginate_questions(request, questions)
    categories = Category.query.all()
    dictCategories = {}

    for category in categories:
      dictCategories[category.id] = category.type

    if len(questions) ==0:
      abort(404)

    return jsonify({
        'success': True,
        'questions':current_questions,
        'total_questions': len(questions),
        'categories': dictCategories,
        'current_category': None
    })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id==question_id).first()
      if question is None:
        abort(404)

      question.delete()
      questions = Question.query.all()
      current_questions = paginate_questions(request, questions)
      categories = Category.query.all()
      dictCategories = {}

      for category in categories:
        dictCategories[category.id] = category.type

      return jsonify({
      'success': True,
      'deleted': question.id,
      'questions':current_questions,
      'total_questions': len(questions),
      'current_category': None,
      'categories': dictCategories
      })
    

    except  ValueError as e:
      print(e)
      abort(422)
      
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=["POST"])
  def create_question():
    body = request.get_json()

    question = body.get('question', None)
    answer = body.get('answer', None)
    difficulty = body.get('difficulty', None)
    category = body.get('category', None)
    search = body.get('searchTerm', None)

    try:
      if search:
        questions = Question.query.order_by(Question.id).filter(
                    Question.question.ilike("%{}%".format(search))
                )
        current_questions = paginate_questions(request, questions)

        return jsonify({
          'success': True,
          'questions':current_questions,
          'total_questions': len(questions.all()),
          'current_category': None
        })

      else:
        question = Question(question=question, answer=answer, difficulty=difficulty, category=category)
        question.insert()

        questions = Question.query.all()
        current_questions = paginate_questions(request, questions)
        categories = Category.query.all()
        dictCategories = {}

        for category in categories:
          dictCategories[category.id] = category.type

        return jsonify({
          'success': True,
          'created': question.id,
          'questions':current_questions,
          'total_questions': len(questions),
          'categories': dictCategories
        })
    except ValueError as e:
      print(e)
      abort(422)
      


  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def get_questions_based_on_category(category_id):
    try:
      category = Category.query.filter_by(id=category_id).first()
      print(category)
      if (category is None):
        abort(404)

            
      questions = Question.query.filter_by(category=category.id).all()
      print(questions)
      current_questions = paginate_questions(request, questions)

      return jsonify({
        'success': True,
        'questions':current_questions,
        'total_questions': len(questions),
        'current_category': category.type
      })
    except ValueError as e:
      print(e)
      abort(404)

  '''
  @TODO: 
  Create a POST endpoint to . 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route("/quizzes", methods=['POST'])
  def play_quiz_question():
        if request.data:
            search_key = json.loads(request.data)
            if (('quiz_category' in search_key and 'id' in search_key['quiz_category'])
              and 'previous_questions' in search_key):
              questions_query = Question.query.filter_by(category=search_key['quiz_category']['id'])\
              .filter().all()
              length_of_available_question = len(questions_query)
              if length_of_available_question > 0:
                    result = {
                          "success": True,
                          "question": Question.format(
                              questions_query[random.randrange(
                                  0,
                                  length_of_available_question
                              )]
                          )
                    }
              else:
                    result = {
                          "success": True,
                          "question": None
                    }
              return jsonify(result)
            abort(404)
        abort(422)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not Found"
      }), 404

  @app.errorhandler(422)
  def unproccesable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
         "message": "Method not allowed"
    }), 405

  return app

    