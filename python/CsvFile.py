import csv

class CsvFile:
    def __init__(self, fileName=""):
        self.fileName = fileName
        self.handle = open(self.fileName,"wb")
                                 
    def writeHeader(self,lHeaders):
        writer = csv.writer(self.handle, delimiter=',', lineterminator="\n")
        writer.writerow(lHeaders)

    def output(self,lData):
        fieldnames = ['TIMESTP', 'ACTION', 'USER', 'FOLDER', 'FILENE', 'IP']
        writer = csv.DictWriter(self.handle,fieldnames=fieldnames, quotechar="\"", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(lData)
