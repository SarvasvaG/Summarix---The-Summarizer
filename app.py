from flask import Flask,render_template,request,redirect,url_for
import summariser
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input',methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        s = request.form['inputText']
        summary = summariser.funSum(s)
        # f = request.files['documentUpload']
        return render_template('output.html',out = summary, inp = s)
    return render_template('input.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True,port=8080)