from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>\
            <p> this is a test server</p>"

@app.route("/home", methods=['GET','POST'], defaults={"name":"Nobody"})
@app.route("/home/<name>", methods=['GET','POST'])
def name(name):
    return f"""Hello {name}!"""

@app.route('/query')
def query():
    fname = request.args.get('name')
    location = request.args.get('location')
    return f"Hello {fname}, you are in {location}. This is the query page"

@app.route('/theform')
def theform():
    return """<form method='POST' action='/process'>
                <input type='text' name='name'>
                <input type='text' name='location'>
                <input type='submit' value='Submit'>
            </form>"""

@app.route('/process', methods=['POST'])
def process():
    name=request.form['name']
    location=request.form['location']
    return f"Hello {name}, you are from {location}"

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name=data['name']
    location=data['location']
    randomlist=data['randomlist']

    return {"result":"sucess!","name": name, "location": location, "randomkey": randomlist[1]}

if __name__ == '__main__':
    app.run(debug=True)