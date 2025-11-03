from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    app.run()
