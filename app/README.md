### Activate Virtual Environment
```
myprojects$ venv/Script/activate
```
###Installing requirements
```
app$ pip install -r requirements.txt
```

### Run Flask Rest Api
```
app$ set FLASK_APP=app.py (Windows)
app$ export FLASK_APP=hello (Bash)
app$ FLASK_APP = "hello" (Power Shell)
```
```
app$ flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Usage of Api

http://localhost:5000/Users
![Users](img/Users.png)

http://localhost:5000/Users/1/albums
![Users](img/id1.png)

http://localhost:5000/Users/6/albums
![Users](img/id6.png)

http://localhost:5000/swagger
![Users](img/swaggeruser.png)
![Users](img/swaggerid.png)

**NOTE**:
Swagger id is not working but route working in search bar