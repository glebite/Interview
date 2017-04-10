# Introduction:
Deviated from Java - alerted this to Andrea  Writing in python for now.



# NOTES:
I hadn't used the csv class before - found it to be a bit odd but once I got the hang
of it, it grooved - last minute fix went in to add the lineterminator as without it, the
programme failed the diff test between the sample output csv file and the one I generated.



# execution:
python interview.py inFile.json outfile.csv

output: stdout report in pretty print json output indent=4 



# coolness:
Made use of generator capabilities in python for a nice flow from json input through record
filtering and then out to the csvFile.

StatsFilter class retains information to report on in the end.



# syntax checks:
pyflakes execution for all .py files:

-*- mode: compilation; default-directory: "~/projects/interset/python/" -*-
Compilation started at Mon Apr 10 13:40:55

pyflakes StatsFilter.py

Compilation finished at Mon Apr 10 13:40:55


-*- mode: compilation; default-directory: "~/projects/interset/python/" -*-
Compilation started at Mon Apr 10 13:40:14

pyflakes CsvFile.py

Compilation finished at Mon Apr 10 13:40:14

-*- mode: compilation; default-directory: "~/projects/interset/python/" -*-
Compilation started at Mon Apr 10 13:39:40

pyflakes Json2Reader.py

Compilation finished at Mon Apr 10 13:39:40

-*- mode: compilation; default-directory: "~/projects/interset/python/" -*-
Compilation started at Mon Apr 10 13:38:40

pyflakes interview.py

Compilation finished at Mon Apr 10 13:38:40