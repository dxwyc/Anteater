from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route('/')
def helloworld():
    return '<h2>Hello world!</h2>'

if __name__ == '__main__':
    app.run()
