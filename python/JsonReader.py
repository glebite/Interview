import json


class JsonReader:
    def __init__(self, fileName=""):
        self.list = []
        self.index = 0
        if fileName == "":
            self.fileName = ""
        else:
            self.fileName = fileName

    def read(self):
        if self.fileName == "":
            print "Cannot do that, Jim!"
        else:
            try:
                with open(self.fileName, 'r') as f:
                    self.data = f.read()
            except IOError:
                print "File does not exist."

    def parse(self):
        for record in self.data.split('\n'):
            if record == "":
                continue
            data = json.loads(record)
            self.list.append(data)
            self.index += 1

    def __iter__(self):
        return self

    def next(self):
        try:
            result = self.list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __len__(self):
        return len(self.list)

if __name__ == "__main__":
    pass
