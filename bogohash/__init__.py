
__title__ = 'bogohash'
__version__ = '0.1'
__author__ = 'Jimmy Wahlberg'
__license__ = 'GLWT (Good Luck With That) Public License'


class bogohash:

    def __init__(self, content=""):
        self.content = content

    def update(self, content):
        self.content += content

    def digest(self):
        return "*" * len(self.content)


def bogo(content=""):
    return bogohash(content)
