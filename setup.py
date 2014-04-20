from setuptools import setup

setup(
	name = 'xls2py',
	version = '0.1.0',
	author = 'Vita Smid',
	author_email = 'me@ze.phyr.us',
	packages = ['xls2py',],
	url = 'https://github.com/ze-phyr-us/xls2py',
	license = 'LICENSE.txt',
	description = 'Convert Excel sheets to tuples of Python dicts or Python tuples.',
	install_requires = ['xlrd >= 0.9.2'],
	entry_points = {
		'console_scripts': [
			'xls2py = xls2py:main',
		]
	}
)
