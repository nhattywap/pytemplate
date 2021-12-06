from pytemplate.utils.constants import START_DOC

def write_to_file(file_name, data):
	with open(f'{file_name}.html', 'w') as f:
		f.write(START_DOC)
		f.write(data)


def write_File(file_name, _type, data, mode='w'):

	with open(f'{file_name}.{_type}', mode) as f:
		f.write(data)

def write_js(file_name, data, mode='w'):

	write_File(file_name, 'js', data, mode)

def wiret_css(file_name, data, mode='w'):
	write_File(file_name, 'css', data, mode)

