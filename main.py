from flask import Flask
import functions

app = Flask(__name__)


@app.route("/")
def index():
    result = '<br>'
    candidates = functions.get_all()

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route("/candidate/<int:pk>")
def get_candidate_by_pk(pk):
    candidate = functions.get_by_pk(pk)

    if candidate == 'Not Found':
        return candidate

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'

    return f"""
        <img src="{candidate['picture']}>
        <pre> {result} </pre>
    """

@app.route("/candidate/<skill>")
def get_candidate_by_skill(skill):
    result = '<br>'
    candidates = functions.get_by_skill(skill)

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


app.run(debug=True)
