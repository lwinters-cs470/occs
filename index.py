from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

# Include a module runner to allow local testing
if __name__ == '__main__':
    app.run(debug=True)  # Set to false for production