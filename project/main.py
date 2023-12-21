from flask import (
    Flask,
    render_template,
    request,
)

from project.recogniser import RecogniserClient
from project.parser import Parser

app = Flask(__name__)


@app.route(rule='/', methods=['GET'])
def index():
    return render_template(template_name_or_list='index.html')


@app.route(rule='/', methods=['POST'])
def recognise():
    result: str = Parser(
        response=RecogniserClient().recognise(
            photo=request.files['file'],
        ),
    ).parse()

    return render_template(template_name_or_list='result.html', data=result)


if __name__ == '__main__':
    app.run()
