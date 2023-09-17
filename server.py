from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def hello_name(name):
    return f"Hi {name}"
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num,word):
    return num * word
if __name__ == "__main__":
    app.run(debug=True)