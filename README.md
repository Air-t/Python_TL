# Transmital letter for SDS/2 engineerign software
This code uses SDS/2 software API to output raport like file. May be usefull for those who would like avoid tedious work,
connectied to transmital drawing letter.

## Installation
TL.py will require setting up TL file os path. Please see TL.py and set up "path" variable inside as required.

## Usage
TL file represents the output SDS/2 drawing log JSON file. Based on this TL file program will generate output.
Use SDS/2 load "run python file" command and use TL.py

Output sample:
```
----------------------------------------------------------------------
TL created on:  03-21-2019 11:44
----------------------------------------------------------------------
RANGE OF DWG'S      |REV   |ITEM TYPE      |SIZE           |QTY
----------------------------------------------------------------------
E14001 and E14002   |0     |Erection Sheet |36" x 24"      |2
E15001              |0     |Erection Sheet |36" x 24"      |1
14101 thru 14113    |0     |Detail Sheet   |8.5" x 14"     |13
14201 thru 14266    |0     |Detail Sheet   |14" x 8.5"     |66
14301 thru 14309    |0     |Detail Sheet   |24" x 18"      |9
14321               |0     |Detail Sheet   |36" x 24"      |1
14401               |0     |Detail Sheet   |14" x 8.5"     |1
14451 thru 14453    |0     |Detail Sheet   |24" x 18"      |3
----------------------------------------------------------------------
Total items count: 96
----------------------------------------------------------------------
```

## Notes
Technologies used: Python.

## Author
Air-t
