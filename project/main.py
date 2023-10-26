from flask import (
    Flask,
    render_template,
    request,
)
from project.recogniser import RecogniserClient

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SERVER_NAME='127.0.0.1:8000',
    MAX_COOKIE_SIZE=0,
)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def recognise():
    response: list[str] = RecogniserClient().recognise(
        photo=request.files['file']
    )

    return render_template('result.html', data=response)


if __name__ == '__main__':
    app.run()
