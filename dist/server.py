from flask import Flask,render_template
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def index():
    return render_template('index.html')
mytxtfile ="./port.ini"
with open(mytxtfile, "r", encoding='utf-8') as f:
    data = f.read()
if __name__ == '__main__':
    app.run(host='0.0.0.0',port= data,debug=True)
