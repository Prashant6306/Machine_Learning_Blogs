from flask import Flask, render_template, request
import joblib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')