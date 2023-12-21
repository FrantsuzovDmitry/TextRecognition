from requests import Response


class Parser:
    def __init__(self, response: Response):
        self.response: Response = response

    def parse(self) -> str:
        result = self.response.json()
        if result['message'] != '':
            return 'Invalid image :('
        return result['text']
