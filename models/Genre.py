import config


class Genre:

    def __init__(self, data):
        self.id = data.get('id')
        self.title = data.get('title')

    def to_msx(self, category):
        return {
            "type": "default",
            "label": self.title,
            "action": f"content:request:interaction:{config.MSX_HOST}/msx/category?id={{ID}}&category={category}&genre={self.id}&offset={{OFFSET}}&limit={{LIMIT}}|20@http://msx.benzac.de/interaction/paging.html"
        }