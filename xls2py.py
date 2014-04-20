#!/usr/bin/env python
from __future__ import print_function
import sys, xlrd



def repretty(L):
	''' Print each row on a separate line and indent it with one tab. '''
	return '(\n{},\n)'.format(',\n'.join([ '\t{!r}'.format(row) for row in L ]))


def main(src, sheet, constructor):
	wb = xlrd.open_workbook(src)
	sheet = wb.sheet_by_index(sheet)

	rows = []
	labels = [ cell.value for cell in sheet.row(0) ]
	for i in range(1, sheet.nrows):
		values = [ cell.value for cell in sheet.row(i) ]
		row = constructor(labels, values)
		rows.append(row)

	print(repretty(rows))


if __name__ == '__main__':
	if len(sys.argv) not in (2, 3, 4):
		print('Usage: {} [--tuples] path/to/source.xls[x] [sheet #]'.format(sys.argv[0]))
		sys.exit(1)

	if '--tuples' in sys.argv:
		constructor = lambda labels, values: tuple(values)
		sys.argv.remove('--tuples')
	else:
		constructor = lambda labels, values: dict(zip(labels, values))

	sheet = int(sys.argv[2]) if len(sys.argv) == 3 else 0
	main(sys.argv[1], sheet, constructor)
