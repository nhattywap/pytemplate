from pytemplate.contents.constants import Script
from pytemplate.utils.fmt import FormatString
from pytemplate.utils.constants import CharSets

class JavaScript(CharSets):

	def __init__(self, formated=1):
		self.tag = Script(type='text/javascript')
		self.funcs = []
		self.formated = formated

	@property
	def script(self):

		self.tag.config(intext=self.dump_script())
		return self.tag

	def create_func(self, funk_name, fattrs=[], *fargs):

		if isinstance(fattrs, (list, tuple)):
			func = Function(funk_name, *fattrs)
			func.add_argument(*fargs)

			return func

	def add_func(self, *funcs):

		for func in funcs:

			if isinstance(func, Function):
				self.funcs.append(func)

	def add_statment(self, stet):
		
		if not self.formated:
			self.newline = self.empty_string

		self.funcs.append(FormatString(stet, self.semicolon, self.newline).string)

	def dump_script(self):
		_script = self.empty_string

		if not self.formated:
			self.tab = self.empty_string

		for func_or_str in self.funcs:
			if isinstance(func_or_str, Function):
				_script += FormatString(self.tab, func_or_str.get_func(self.formated)).string
			else:
				_script += FormatString(self.tab, func_or_str).string

		return _script

class Function(CharSets):

	def __init__(self, func_name, *args):
		self.func_name = func_name
		self.attrs = list(args)
		self.argument = []

	def add_argument(self, *args):

		self.argument.extend(list(args))

	def print_args(self):

		for i, arg in enumerate(self.argument):
			print(i, self.space, arg)

	def remove_arg(self, index):
		
		if len(self.argument) != 0 and len(self.argument) >= index:
			self.argument.remove(self.argument[index])

	def add_arg(self, arg, index=None):

		if index is None:
			self.argument.append(arg)
		else:
			self.argument.insert(index, arg)

	def get_func(self, formated=1):

		if not formated:
			self.tab , self.newline = self.empty_string, self.empty_string

		_func = FormatString('function', self.space, self.func_name).string
		if self.attrs:
			_func += self.open_braket
			_func += FormatString(self.coma, self.space).string.join(self.attrs)
			_func += self.close_braket
		else:
			_func += FormatString(self.open_braket, self.close_braket).string

		_func += FormatString(self.open_bres, self.newline).string
		if self.argument:
			for arg in self.argument:
				_func += FormatString(self.tab*2, arg, self.semicolon, self.newline).string

		_func += FormatString(self.tab, self.close_bres, self.newline).string
		return _func
