Flask-APIForm
=============

A simple form validator for REST APIs in Flask.

To install it :

    pip install Flask-APIForm


### Example ###

```
from flask import Flask, request, Response
from flaskext.apiform import Form, StringField, IntField

try:
	from json import dumps
except ImportError:
	from simplejson import dumps

def json(response='', code=200, headers=None):
	return Response(dumps(response), code, mimetype='application/json', headers=headers)

class IndexForm(Form):
	name = StringField(minlength=1, maxlength=20)
	age = IntField(min=1, max=120)


app = Flask(__name__)

@app.route("/")
def index():
	form = IndexForm(request)
	if not form.validate():
		return json({'message': 'Validation Failed', 'errors': form.errors}, 422)
		
	return json({'name': form.name, 'age': form.age})

if __name__ == "__main__":
	app.debug = True
	app.run()
```
