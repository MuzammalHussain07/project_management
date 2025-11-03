from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <h1 style="text-align:center;">🏗️ Project Management App Demo</h1>
    <p style="text-align:center;">Dashboard | Companies | Projects | Tasks | Reports</p>
    <ul style="text-align:center; list-style:none;">
        <li><a href="/company">Company</a></li>
        <li><a href="/projects">Projects</a></li>
        <li><a href="/tasks">Tasks</a></li>
        <li><a href="/reports">Reports</a></li>
    </ul>
    """)

@app.route('/company')
def company():
    return "<h2>Company Page Demo</h2><p>Shows company info and members.</p>"

@app.route('/projects')
def projects():
    return "<h2>Projects Page Demo</h2><p>Displays sample projects list.</p>"

@app.route('/tasks')
def tasks():
    return "<h2>Tasks Page Demo</h2><p>Shows assigned tasks and deadlines.</p>"

@app.route('/reports')
def reports():
    return "<h2>Reports Page Demo</h2><p>Shows summary and insights.</p>"

if __name__ == "__main__":
    app.run()
