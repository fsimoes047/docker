from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>\
            <p> this is a test server</p>"


@app.route("/name/")
def name():
    return """<form>\
            <label for="fname">First name:</label><br>\
            <input type="text" id="fname" name="fname"><br>\
            <label for="lname">Last name:</label><br>\
            <input type="text" id="lname" name="lname">\
            <input type="submit" value="Submit answer">
            </form>"""
