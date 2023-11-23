from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/new"
mongo = PyMongo(app)

@app.route('/submit', methods=['GET','POST','DELETE'])
def submit_form():
    global data
    data = request.json
    painting_name = data.get('paintingName')
    painting_id = data.get('paintingId')
    painter = data.get('painter')
    year = data.get('year')
    style = data.get('style')
    medium = data.get('medium')
    dimensions = data.get('dimensions')
    description = data.get('description')

    new_painting = {
        'paintingName': painting_name,
        'paintingId': painting_id,
        'painter' : painter,
        'year' : year,
        'style' : style,
        'medium' : medium,
        'dimensions' : dimensions,
        'description' : description

    }

    try:
       
        inserted = mongo.db.paintings.insert_one(new_painting)
        if inserted:
            return jsonify({'message': 'Form data successfully inserted into MongoDB'}), 200
        
        else:
            return jsonify({'message': 'Failed to insert data into MongoDB'}), 500
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method Not Allowed'}), 405

# @app.route("/") #website URL
# def hello_world():
#     return "<p>sup!</p>"

if __name__ == '__main__':
    app.run(debug=True)

