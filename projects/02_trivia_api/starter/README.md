Full Stack Trivia
Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
Delete questions.
Add questions and require that they include question and answer text.
Search for questions based on a text query string.
Play the quiz game, randomizing either all questions or within a specific category.
Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

Starting and Submitting the Project
Fork the project repository and Clone your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

Once you're ready, you can submit your project on the last page.

About the Stack
We started the full stack application for you. It is designed with some key functional areas:

Backend
The ./backend directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in __init__.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

./backend/flaskr/__init__.py
./backend/test_flaskr.py
Frontend
The ./frontend directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

What are the end points and HTTP methods the frontend is expecting to consume?
How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?
Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with TODO. These are the files you'd want to edit in the frontend:

./frontend/src/components/QuestionView.js
./frontend/src/components/FormView.js
./frontend/src/components/QuizView.js
By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

View the README within ./frontend for more details.

API Reference

Just Getting Started? 
The Udacitrivia API is organized around REST. The API has predictable resource-oriented URLs,
accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard
HTTP response codes, authentication, and verbs.

BASE URL
http://127.0.0.1:5000/. 
At present this app is only run locallly and not hosted as a base
URL from the backend and runs a proxy on the frontend.

### AUTHENTICATION
This version does not require authentification or API keys.

### ERRORS
Library uses conventional HTTP response codes to indicate the success or failure of
an API request. In general: Codes in the 2xx range indicate success. Codes in the 
4xx range indicate an error that failed given the information provided (e.g., a 
required parameter was omitted, a charge failed, etc.). 

### Error Handling
Erros are returned in JSON objects in the following format:

{
    "success: "false",
    "error": "404",
    "mesage": "BAd Request"
}

Endpoints

GET /categories
This represents a list of categories and a success message. 

Sample: 
curl http://127.0.0.1:5000/categories
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

GET /questions
This represents a list of questions with its answer and difficulty, categories and total number of questions. 
Results are paginated in groups of 10 and includes an argument to choose page number.

Sample: 
curl http://127.0.0.1:5000/questions

  {
    "categories": {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    },
    "questions": [
      {
        "answer": "Maya Angelou",
        "category": 2,
        "difficulty": 2,
        "id": 5,
        "question": Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "Maya Angelou",
        "category": 2,
        "difficulty": 2,
        "id": 20,
        "question": Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "Maya Angelou",
        "category": 2,
        "difficulty": 2,
        "id": 10,
        "question": Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "Maya Angelou",
        "category": 2,
        "difficulty": 2,
        "id": 8,
        "question": Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "Maya Angelou",
        "category": 2,
        "difficulty": 2,
        "id": 19,
        "question": Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "Maya Angelou",
        "category": 2,
        "difficulty": 2,
        "id": 12,
        "question": Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
      },
      {
        "answer": "Uraguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
      },
      {
        "answer": "Lake Victoria",
        "category": 3,
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
      },
      {
        "answer": "One",
        "category": 2,
        "difficulty": 4,
        "id": 18,
        "question": "How many paintings did Van Gogh sell in his lifetime?"
      }
    ],
    "success": true,
    "total_questions": 19
  }
DELETE /questions/<int:id>
Deletes a question of a given ID. Returns a success value, an id of question deleted, a formatted list of 
remaining questions and total number of questions.

Sample: 
curl -X DELETE http://127.0.0.1:5000/questions/8
{
    "deleted": 8,
    "success": true
}

POST /questions
Creates a new question using the submitted question, answer, difficulty and category. Returns the id of the 
success value, total questions, and question list based on current page number to update the frontend.

Sample: 
curl  -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{ "question": "What goes up and never comes down", "answer": "Age", "difficulty": 3, "category": "4" }'
{
    "created": 25,
    "questions": [
        {
        "answer": "Lake Victoria",
        "category": 3,
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
      },
      {
        "answer": "One",
        "category": 2,
        "difficulty": 4,
        "id": 18,
        "question": "How many paintings did Van Gogh sell in his lifetime?"
      }
    ],
    "success": true,
    "total_questions": 20
}

SearchTerm
POST /questions
Search questions which contains 'searchTerm' in JSON parameters
Sample: 
curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"searchTerm": "Whose"}'
{
  "questions": [
    {
      "answer": "Maya angelo",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }
  ],
  "success": true,
  "total_questions": 1
}

GET /categories/<int:id>/questions
This represents a list of questions with a particular id, with its answer and difficulty and total number of questions. 
Results are paginated in groups of 10 and includes an argument to choose page number.

Sample: 
curl http://127.0.0.1:5000/categories/1/questions
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 4
}
POST /quizzes
This returns a random question based on a selected category with a guess option, the returned question should be not one of previous questions

Sample:
curl  -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [4, 15], "quiz_category": {"type": "Science", "id": "20"}}'
    {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
    },
    "success": true
}

Deployment N/A

Authors
Iwuh Ikechukwu Daniel

Acknowledgements
The awesome team at Udacity.