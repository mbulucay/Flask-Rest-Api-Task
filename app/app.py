from flask import Flask,jsonify,render_template,request
from flasgger import Swagger
from flasgger import LazyString, LazyJSONEncoder
from flasgger.utils import swag_from
import requests
import json
from models import *


app = Flask(__name__, static_url_path='/templates')

# Swagger config
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True, 
            "model_filter": lambda tag: True, 
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

template = dict( swaggerUiPrefix=LazyString(lambda: request.environ.get("HTTP_X_SCRIPT_NAME", "")) )

app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, config=swagger_config, template=template)
# end of swagger config

@app.route("/")
def index():
    return render_template('home.html')


@app.route('/Users', methods=['GET'])
@swag_from("swagger.yaml")
def users():

    objectUsers = []
    url = 'https://jsonplaceholder.typicode.com/users'
    
    try:
        response = requests.get(url)                                        # Getting data from url
    
        if response.status_code == 200:

            jsonUsers = json.loads(json.dumps(response.json()))             # Data converting to json format

            for userdata in jsonUsers:
                objectUsers.append( createUser(userdata) )                  # Adding all user in a list 
            return jsonify(jsonUsers)
            # return render_template('/users.html',users  = objectUsers)
        else :
            return 'bad request!'

    except requests.ConnectionError:
        return "Connection Error"


@app.route('/Users/<int:id>/albums', methods=['GET'])
@swag_from("swagger.yaml")
def albums(id):
    
    url = 'https://jsonplaceholder.typicode.com/albums'
    objectAlbums = [] 
      
    try:
        response = requests.get(url)                                    # Getting data from url

        if response.status_code == 200:
            
            jsonAlbums = json.loads(json.dumps(response.json()))        # Data converting to json format
            
            for albumdata in jsonAlbums:
                album = createAlbum(albumdata)                          # Creating object from json data
                if album.userId == id: 
                    objectAlbums.append(albumdata)                      # Adding object with matching user id
            
            return jsonify(objectAlbums)
            # return render_template('/album.html',uid = id,albums = objectAlbums)
        else:
            return 'bad request!'

    except requests.ConnectionError:
        return "Connection Error"

#To create an album Object from Json data
def createAlbum(data):
    return Album(data['userId'], data['id'], data['title'])

#To create a User Object from Json data
def createUser(data):
    user = User(data['id'],data['name'], data['username'], data['email'],
            Address(data['address']['street'],data['address']['suite'],data['address']['city'],
            data['address']['zipcode'],Geo(data['address']['geo']['lat'],data['address']['geo']['lng'])),
            data['phone'],data['website'], Company(data['company']['name'],data['company']['catchPhrase'],data['company']['bs'] ))
    return user


if __name__ == "__main__":
    app.run(debug = True)

