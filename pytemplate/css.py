from pytemplate.utils.fmt import FormatString
from pytemplate.utils.constants import  CharSets

class Css(CharSets):

	def __init__(self,  _class, _type=CharSets.dot, **kwargs):
		self._class = _class
		self._type = _type
		self.attributes = kwargs
		self.style = self.get_css_file()
		self.css_list = []

	def update(self, **kwargs):

		self.attributes.update(**kwargs)
	
	def configure(self, **kwargs):

		for k,v in kwargs.items():
			if hasattr(self, k):
				setattr(self, k, v)

	def get_css_file(self):

		self.attributes = {k.replace(self.dash, self.hyfen):v for k,v in self.attributes.items()}
		css_file = FormatString(self._type, self._class).string
		css_file += FormatString(self.open_bres, self.newline).string

		for key,value in self.attributes.items():
			css_file += FormatString(self.tab, key, self.colon, self.space, value, self.semicolon, self.newline).string
		css_file += FormatString(self.close_bres, self.newline).string

		return css_file

	@classmethod
	def new_class(cls, _class, _type=CharSets.dot, **kwargs):

		return cls(_class, _type=_type, **kwargs)

	def new_css(self, _class, _type=CharSets.dot, **kwargs):

		_cls = self.new_class
		if kwargs:
			css_obj = _cls(_class, _type=_type, **kwargs)
		else:
			css_obj = _cls(_class, _type=_type, **self.attributes)

		self.css_list.append(css_obj)
		return css_obj

	def has_css_list(self):

		if self.css_list:
			return True
		return False

	def dump_css(self):

		style = self.empty_string
		style += self.get_css_file()

		def get_css(_css_objs):
			_style = self.empty_string

			for _css in _css_objs:
				if _css.has_css_list():
					_style += get_css(_css.css_list)
				else:
					_style += FormatString(_css.dump_css(), self.newline).string

			return _style

		if self.css_list:
			style += get_css(self.css_list)

		return style

class GenericBoxStyle(Css):

	def __init__(self,  _class, _type=CharSets.dot, **kwargs):
		self._class = _class
		self._type = _type
		self.attributes = kwargs

		super(GenericBoxStyle, self).__init__(self._class, self._type, **self.attributes)

	def get_dict(self, **kwargs):

		return kwargs

	def get_generic_style(self):

		self.update(**self.get_dict(
				width='auto',
				height='auto',
				padding='auto',
				margin='auto',
				border='1px solid #f1f1f1',
			))

