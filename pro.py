from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/stureg')
def stureg():
    return render_template('stureg.html')

@app.route('/teareg')
def teareg():
    return render_template('teareg.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/sreport')
def sreport():
    return render_template('sreport.html')

@app.route('/treport')
def treport():
    return render_template('treport.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

@app.route('/selectexam')
def selectexam():
    return render_template('selectexam.html')

@app.route('/reportdetails')
def reportdetails():
    return render_template('reportdetails.html') 


if __name__ == "__main__":
    app.run()