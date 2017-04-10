import json
from datetime import datetime
import os

gsActivities = {'createdDoc', 'deletedDoc', 'viewedDoc', 'addedText',
                'changedText', 'deletedText', 'hashed', 'replicated',
                'archived', 'restored'}

gsActions = {'ADD','REMOVE','ACCESSED'}

gsActivityMapping = {"createdDoc":"ADD", "deletedDoc":"REMOVE", "viewedDoc":"ACCESSED", 
                     "addedText":"ADD","changedText":"ADD", "deletedText":"REMOVE",
                     "archived":"REMOVE"}

gsMapping = ["TIMESTP","ACTION","USER","FOLDER","FILENE","IP"]


class StatsFilter:
    def __init__(self, uniqueField, interestField):
        self.unique = {}
        self.uniqueField = uniqueField
        self.interestField = interestField
        self.noActionMapping = 0
        self.duplicates = 0
        self.linesRead = 0
        self.dropped = 0
        self.acceptedRecords = 0
        self.sta-ts = {}
        self.users = set()
        self.files = set()
        self.dates = {}
        for x in gsActions:
            self.stats[x] = 0
        pass

    def dateTracker(self, dateString):
        if 'first' not in self.dates:
            self.dates['first'] = dateString
        else:
            self.dates['last'] = dateString
    
    def report(self):
        json_report = json.dumps({'linesRead':str(self.linesRead),
                                  'droppedEventsCounts':str(self.dropped),
                                  'droppedEvents':{
                                      'No action mapping':str(self.noActionMapping),
                                      'Duplicates':str(self.duplicates)},
                                  'uniqueUsers':len(self.users),
                                  'uniqueFiles':len(self.files),
                                  'startDate':self.dates['first'],
                                  'endDate':self.dates['last'],
                                  'actions':{
                                      'ADD':str(self.stats['ADD']),
                                      'REMOVE':str(self.stats['REMOVE']),
                                      'ACCESSED':str(self.stats['ACCESSED'])
                                  }}, indent=4)
        return json_report

    def transposeRecord(self, record):
        newRecord = {}

        # handle date/time here
        if "timeOffset" in record.keys():
            timeOffset = record['timeOffset']
        else:
            timeOffset="Z"
        in_time = datetime.strptime(record['timestamp'], "%m/%d/%Y %I:%M:%S%p")
        out_time = datetime.strftime(in_time, "%Y-%m-%dT%H:%M:%S")+timeOffset
        self.dateTracker(str(out_time))
        newRecord['TIMESTP'] = out_time
        
        newRecord['ACTION'] = gsActivityMapping[record['activity']]
        self.stats[newRecord['ACTION']] += 1
        
        # remove email from user record
        newRecord['USER'] = record['user'].split("@")[0]
        self.users.add(newRecord['USER'])
        
        newRecord['IP'] = record['ipAddr']

        # NOTE: os.path.dirname trims the trailing separator add it
        newRecord['FOLDER'] = os.path.dirname(record['file'])+os.sep
        newRecord['FILENE'] = os.path.basename(record['file'])
        self.files.add(newRecord['FILENE'])
        
        return newRecord

    def through(self, record):
        global gsActivities
        self.linesRead += 1
        if record[self.uniqueField] in self.unique.keys():
            self.duplicates += 1
            self.dropped += 1
            pass
        else:
            # check for unique field entries
            self.unique[record[self.uniqueField]] = 1
            if record['activity'] not in gsActivityMapping.keys():
                self.noActionMapping += 1
                self.dropped += 1
                pass
            elif record[self.interestField] in gsActivities:
                self.acceptedRecords += 1
                transposed = self.transposeRecord(record)
                yield transposed
            else:
                pass
