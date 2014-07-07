#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
"""
gitlog complete:
    usage:
        git log --date=short --pretty=format:'%ad, %an' > foobar.csv
"""


def main(validate_name, outputfile):
    date_matrix = {}

    for row in csv.reader(sys.stdin):
        date = row[0]
        name = row[1].rstrip().strip()
        if name == '%s' % validate_name:
            if date in date_matrix:
                date_matrix[date] += 1
            else:
                date_matrix[date] = 1

    w = open(outputfile, 'w')
    w.write("date, num_commit\n")

    for w_date in sorted(date_matrix.keys()):
        w.write('"%s", %s\n' % (w_date, date_matrix[w_date]))

    w.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Invalid number of argument: " , sys.argv
        print "Usage:"
        print "  gitlog_date.py validate_name outputfile.csv"
        sys.exit(0)

    validate_name = sys.argv[1]
    outputfile = sys.argv[2]
    main(validate_name, outputfile)
