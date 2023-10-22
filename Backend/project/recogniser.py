from requests import (
    post,
    Response,
)
from datetime import datetime
from werkzeug.datastructures import FileStorage


class RecogniserClient:
    def __init__(self):
        self.url: str = 'https://img-to-text1.p.rapidapi.com/api/2d3652243be692de40304031b868aea0'
        self.files: dict = {}
        self.headers: dict = {
            'X-RapidAPI-Key': 'bfea5bdeeemsh335a3af6d5ce6f2p1fa505jsn5c83d42a3675',
            'X-RapidAPI-Host': 'img-to-text1.p.rapidapi.com',
        }

    def recognise(self, photo: FileStorage) -> Response.json:
        file: bytes = photo.stream.read()
        self.files.update(
            {
                'image': file
            }
        )

        start_time = datetime.now()

        response: Response = post(
            self.url,
            files=self.files,
            headers=self.headers
        )

        execution_time: str = str(datetime.now() - start_time)

        with open('time_tracking.txt', 'a') as f:
            f.write('API request-response time: ' + execution_time + '\n')

        return response.json()
