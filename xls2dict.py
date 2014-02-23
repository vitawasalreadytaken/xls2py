#!/usr/bin/env python
from __future__ import print_function
import sys, xlrd



def main(src, sheet = 0):
	wb = xlrd.open_workbook(src)
	sheet = wb.sheet_by_index(sheet)

	rows = []
	labels = [ cell.value for cell in sheet.row(0) ]
	for i in range(1, sheet.nrows):
		values = [ cell.value for cell in sheet.row(i) ]
		row = dict(zip(labels, values))
		rows.append(row)

	print(tuple(rows))


if __name__ == '__main__':
	if len(sys.argv) not in (2, 3):
		print('Usage: {} path/to/source.xls[x] [sheet #]'.format(sys.argv[0]))
		sys.exit(1)

	sheet = int(sys.argv[2]) if len(sys.argv) == 3 else 0
	main(sys.argv[1], sheet)
