# daupler-oncall

> A solution for https://github.com/Daupler/coding-challenge 

## Installation

### 1. Install dependencies

If you use `pyenv` and `pyenv-virtualenv` (recommended) you can run this from the project directory;

```bash
pyenv virtualenv daupler-oncall
pip install -r requirements.txt
```

Otherwise, on macOS/Linux make sure you have the latest Python 3 installed and run;

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Or on Windows;

```
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up database

Once you've got dependencies installed, the next step is to set up the database and create an admin user (optional) with;

```
python manage.py migrate
python manage.py createsuperuser
```

## Usage

Once you've got the project installed and set up, you can start the app with;

```
python manage.py runserver
```

Then visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser to browse the API.

Here are examples of all supported operations:

| Action👉 Item👇 | CREATE example | READ example | UPDATE example | DELETE example |
|:--:|:--:|:--:|:--:|:--:|
|Person|`curl --request POST --url http://127.0.0.1:8000/people/ --header 'content-type: application/json' --data '{"name": "Bill Gates"}'`|`curl --request GET --url http://127.0.0.1:8000/people/`|`curl --request PATCH --url http://127.0.0.1:8000/people/1/  --header 'content-type: application/json' --data '{"name": "William"}'`|`curl --request DELETE --url http://127.0.0.1:8000/people/1 --header 'content-type: application/json'`|
|Team|`curl --request POST --url http://127.0.0.1:8000/teams/ --header 'content-type: application/json' --data '{"name": "Engineering"}'`|`curl --request GET --url http://127.0.0.1:8000/teams/`|`curl --request PATCH --url http://127.0.0.1:8000/teams/1/  --header 'content-type: application/json' --data '{"name": "Top Engineers"}'`|`curl --request DELETE --url http://127.0.0.1:8000/teams/1 --header 'content-type: application/json'`|
|Assignment|`curl --request POST --url http://127.0.0.1:8000/assignments/ --header 'content-type: application/json' --data '{"person_id": 1, "team_id": 1, "team_role": "Lead Engineer","call_order": 1}'`|`curl --request GET --url http://127.0.0.1:8000/assignments/`|`curl --request PATCH --url http://127.0.0.1:8000/assignments/1/  --header 'content-type: application/json' --data '{"team_role": "Philanthropist"}'`|`curl --request DELETE --url http://127.0.0.1:8000/assignments/1 --header 'content-type: application/json'`|

And here is how to perform the tasks for the coding challenge requirements:

|| Task | Using the example from Row > Column above 👆 |
|:--:|:--:|:--:|
|✅| View a list of teams, including their members | Team > READ example |
|✅| Create new teams | Team > CREATE example |
|✅| Add and remove team members from a team | Assignment > CREATE example <br> Assignment > DELETE example |
|✅| Update the team call order | Assignment > UPDATE example |

## Tests

There are two tests that make sure that the `/teams/` endpoint correctly sorts team members by their call order, and displays them in the correct order in the API response. To run those tests, use this command:

```
python manage.py test  
```
