
class FormatString:

	def __init__(self, *args):
		self.attributes = args
		self.format, self.format_count = self.get_format()

	@property
	def string(self):

		return self.get_string()
	
	def get_string(self):

		_string = ""
		_str_format, _ = self.get_format()

		return _str_format.format(*self.attributes)

	def get_format(self):
		format_list = ["{}" for arg in list(self.attributes)]
		format_count = len(format_list)

		_format = ''.join(format_list)
		return _format, format_count
