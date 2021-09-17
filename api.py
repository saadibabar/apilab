import flask
from flask import request, jsonify
     
app = flask.Flask(__name__)
app.config["DEBUG"] = True
     
# Create some test data for our catalog in the form of a list of dictionaries.
cheeseType = [
	{'id': 0,
        'title': 'Gouda',
         'author': 'The XSS Rat',
         'description': 'Dutch: Goudse kaas, "cheese from Gouda") is a sweet, creamy, yellow cows milk cheese originating from the Netherlands. ...',
         'year': '1992'},
    {'id': 1,
         'title': 'Casu marzu',
         'author': 'The XSS Rat',
         'description': 'Casu martzu[1] (Sardinian pronunciation; literally rotten/putrid cheese)is a traditional Sardinian sheep milk cheese that contains live insect larvae (maggots)',
         'year': '2020'},
    {'id': 2,
         'title': 'Roquefort',
         'author': 'The XSS Rat',
         'description': 'Roquefort is a popular French cheese, reported to be a favourite of Emperor Charlemagne. In France, it is called the cheese of kings and popes.',
         'year': '2020'}
    ]
     
cars=[
{'id':100,'name':'Suzuki'},{'id':101,'name':'Honda'}

]

CreditCards = [
{'id': 0,
     'creditCard': '1234567901234',
     'user': 'API',
     'CVV': '677',
     'validUntil': '1992'},
{'id': 1,
     'creditCard': '1234567901235',
     'user': 'API',
     'CVV': '677',
     'validUntil': '2022'},
{'id': 2,
     'creditCard': '1234567901239',
     'user': 'API',
     'CVV': '677',
     'validUntil': '2023'}
]

# Create some test data for our catalog in the form of a list of dictionaries.
comments = [
    {'id': 0,
     'comment': '1234567901234',
     'user': 'testUser',
     'user email': 'test@bla.com',
     'user adress': 'testlane, testing - 340043 testing in testland'}
]



# A route to return all of the available entries in our catalog.
@app.route('/api/v2/resources/cheese/all', methods=['GET'])
def api_all():
	return jsonify(cheeseType)

#A route to return all of the available entries in our cars catalog.
@app.route('/api/v2/resources/cars/all', methods=['GET'])
def api_cars_all():
	return jsonify(cars)

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/creditCards/all', methods=['GET'])
def api_CCall():
    return jsonify(CreditCards)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>
<p><ul>
<li>/api/v2/resources/cheese/all</li>
<li>/api/v2/resources/cars/all</li>
<li>/api/v1/resources/creditCards/all</li>
<li>/api/v1/comments --> required parameter id</li>
<li>POST --> /api/v1/changeUserSettings </li>




</ul></p>'''
 
# A route to return all of the available entries in our admin log.
@app.route('/api/v1/comments', methods=['GET'])
def api_cards():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
 
    # Create an empty list for our results
    results = []
 
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for comment in comments:
        if comment['id'] == id:
            results.append(comment)
 
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/', methods=['POST'])
def api_home():
         return "paths '/api/v1/changeUserSettings'"

# A route to return all of the available entries in our admin log.
@app.route('/api/v1/changeUserSettings', methods=['POST'])
def api_cards2():
	if 'username' in request.args:
		name = request.args['name']
	else:
		return "Error: No username field provided. Please specify an accountType,name,firstname and adress."

	if 'name' in request.args:
		name = request.args['name']
	else:
		return "Error: No name field provided. Please specify an accountType,name,firstname and adress."
	if 'firstname' in request.args:
		name = request.args['name']
	else:
		return "Error: No firstname field provided. Please specify an accountType,name,firstname and adress."

	if 'adress' in request.args:
		name = request.args['name']
	else:
		return "Error: No adress field provided. Please specify an accountType,name,firstname and adress."

	if 'accountType' in request.args:
		type = request.args['accountType']
	else:
		return "Error: No type field provided. Please specify an accountType,name,firstname and adress. The type can be either user or reader"

	if type == 'admin':
		return "Good job!! Flag: (21384324-03240324)"
	else:
		return "account settings saved"

    



     
app.run(host="0.0.0.0")
