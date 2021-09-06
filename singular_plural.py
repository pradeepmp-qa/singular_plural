from flask import Flask, render_template, request
from textblob import TextBlob
from textblob import Word


# initialse the application
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit' , methods = ["POST"])
def form_data():
   word_text = request.form.get('singular_plural')
   valid_text = request.form.get('input_text')
   if word_text == 'singular':
       out = Word(valid_text).singularize()
   elif word_text == 'plural':
       out = Word(valid_text).pluralize()

   
   return render_template('predict.html' , data = f' {out}')
#    return render_template('predict.html' , sentence_data = f'Number of sentences are {sentence_length}')
if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host = '0.0.0.0',port = 8080)

