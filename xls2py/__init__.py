#!/usr/bin/env python
from __future__ import print_function
import sys, xlrd



def main(argv = sys.argv):
	if len(sys.argv) not in (2, 3, 4):
		print('Usage: {} [--tuples] path/to/source.xls[x] [sheet #]'.format(sys.argv[0]))
		sys.exit(1)

	if '--tuples' in sys.argv:
		fn = readTuples
		sys.argv.remove('--tuples')
	else:
		fn = readDicts

	sheetIndex = int(sys.argv[2]) if len(sys.argv) == 3 else 0

	rows = fn(sys.argv[1], sheetIndex)
	print(repretty(rows))



def readTuples(fileName, sheetIndex):
	return _read(fileName, sheetIndex, lambda labels, values: tuple(values))



def readDicts(fileName, sheetIndex):
	return _read(fileName, sheetIndex, lambda labels, values: dict(zip(labels, values)))



def _read(fileName, sheetIndex, constructor):
	wb = xlrd.open_workbook(fileName)
	sheet = wb.sheet_by_index(sheetIndex)

	rows = []
	labels = [ cell.value for cell in sheet.row(0) ]
	for i in range(1, sheet.nrows):
		values = [ cell.value for cell in sheet.row(i) ]
		row = constructor(labels, values)
		rows.append(row)

	return rows



def repretty(L):
	'''
	Print each row on a separate line and indent it with one tab.
	'''
	return '(\n{},\n)'.format(',\n'.join([ '\t{!r}'.format(row) for row in L ]))



if __name__ == '__main__':
	main()
