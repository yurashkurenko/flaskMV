### MVC - Module View Controller 


```python
from flask import Flask
```

# in order to use the app, you must create an instance of the app 
```python
app = Flask(__name__)
```
# synatax to create flask instance 

#syntax for decorators 
# create a method to display on the homepage/default page 

```python
@app.route("/")
```
# define the page where the informatuon is being displayed (route of the page)
```python
def index_page():
    return "<h1>Welcome to Flask MVC project</h1>"
    ```

# the index_page method will be called at the endpoint (where it is being displayed)

# syntax to run app 
```
@app.route("/<username>")

def welcome_user(username):
```

    return f"<h1>Welcome to the {username}'s page</h1>"

if __name__ == "__main__":
    app.run(debug=True)