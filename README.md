Flask-APIForm
=============

A simple form validator for REST APIs in Flask.

To install it :

    pip install Flask-APIForm
    
    
### Fields ###
<table>
  <tr>
    <th>Field</th>
    <th>Properties</th>
  </tr>
  <tr>
    <td>Field</td>
    <td>required (boolean, default=True), allowed (list or tuple), default, source (args [default], form, files, or url)</td>
  </tr>
  <tr>
    <td>FileField</td>
    <td>extensions (list or tuple), </td>
  </tr>
  <tr>
    <td>StringField</td>
    <td>minlength, maxlength, regex</td>
  </tr>
  <tr>
    <td>EmailField</td>
    <td> </td>
  </tr>
  <tr>
    <td>NumField</td>
    <td>min, max</td>
  </tr>
  <tr>
    <td>IntField</td>
    <td>base (default=10)</td>
  </tr>
  <tr>
    <td>HexField</td>
    <td>length, filter (function)</td>
  </tr>
</table>


### Example ###

```python
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
