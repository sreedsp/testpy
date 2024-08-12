# app.py

from flask import Flask 

def create_app():
    x= 5
    y=7
    app = Flask(__name__)
    a()
    @app.route('/')
    def home():
        return 'Hi Devops Geeks Welcome to the class123'

    return app

def a():
    print("hi")
    a()
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
