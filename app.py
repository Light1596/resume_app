from flask import Flask, render_template

# Create an instance of the app
app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
