import json

class Json2Reader:
    def __init__(self, fileName=""):
        self.fileName = fileName
        self.open()

    def open(self):
        self.handle = open(self.fileName)

    def recordsFromFile(self):
        for record in self.handle:
            yield json.loads(record)

    def run(self):
        for record in self.recordsFromFile():
            print record
