from flask import (
    Flask,
    render_template,
    request,
)
from datetime import datetime
from project.recogniser import RecogniserClient

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SERVER_NAME='127.0.0.1:8000',
    MAX_COOKIE_SIZE=0,
)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        start_time: datetime = datetime.now()

        response: list[str] = RecogniserClient().recognise(
            photo=request.files['photo']
        )

        execution_time: str = str(datetime.now() - start_time)

        with open('time_tracking.txt', 'a') as f:
            f.write('Total request-response time: ' + execution_time + '\n')

        return response, {'Content-Type': 'application/json'}
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
