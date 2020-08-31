from flask import Flask

app =  Flask(__name__)

@app.route("/")
def head():
    return "Hello World!"

@app.route("/second")
def second():
    return "Hello AI ERA!"

@app.route("/third/subthird")
def third():
    return "Subthird of the Third!!!"

@app.route("/fourth/<string:id>")
def fourth(id):
    return f"Dinamic ID is: {id}"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80)