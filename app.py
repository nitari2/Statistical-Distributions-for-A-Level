from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/discrete')
def discrete():
    return render_template('discrete.html')

@app.route('/binomial')
def binomial():
    return render_template('binomial.html')

@app.route('/normal')
def normal():
    return render_template('normal.html')

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=True)