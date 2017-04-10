from Json2Reader import Json2Reader
from StatsFilter import *
from CsvFile import CsvFile
import sys
import os

class interview:
    def __init__(self, inFile, outFile):
        self.inFile = inFile
        self.outFile = outFile

    def run(self):
        jsonHandler = Json2Reader(self.inFile)
        filter = StatsFilter("eventId", "activity")
        csvFile = CsvFile(self.outFile)
        csvFile.writeHeader(gsMapping)
        for record in jsonHandler.recordsFromFile():
            for filteredRecord in filter.through(record):
                csvFile.output(filteredRecord)
        print filter.report()

def usage():
    print "\nUsage: python interview.py infile.json outfile.csv"
    sys.exit(1)
    
def checkArgs(argv):
    if len(argv) != 3:
        usage()
    else:
        if os.path.isfile(argv[1]) == False:
            print "File " + argv[1] + " does not exist."
            usage()
        else:
            pass
    
if __name__ == "__main__":
    checkArgs(sys.argv)
    intObj = interview(sys.argv[1],sys.argv[2])
    intObj.run()
