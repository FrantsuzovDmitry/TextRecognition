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
            'X-RapidAPI-Key': '3e206a5515msh8dc6feebe272ac1p1bab71jsn725382c87289',
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
