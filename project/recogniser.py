import base64

from requests import (
    post,
    Response,
)
from werkzeug.datastructures import FileStorage


class RecogniserClient:
    def __init__(self):
        self.url: str = 'https://img-to-text1.p.rapidapi.com/api/2d3652243be692de40304031b868aea0'
        self.files: dict = {}
        self.headers: dict = {
            'X-RapidAPI-Key': 'bfea5bdeeemsh335a3af6d5ce6f2p1fa505jsn5c83d42a3675',
            'X-RapidAPI-Host': 'img-to-text1.p.rapidapi.com',
        }

    def recognise(self, photo: FileStorage) -> Response:
        file: bytes = photo.stream.read()
        # file: bytes = base64.b64decode(photo.stream.read()) # for Apache Benchmark

        self.files.update(
            {
                'image': file,
            },
        )

        response: Response = post(
            url=self.url,
            files=self.files,
            headers=self.headers,
        )

        return response
