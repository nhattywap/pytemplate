from pytemplate.utils.fmt import FormatString
from pytemplate.utils.constants import CharSets

class BaseTag(CharSets):

	def __init__(self, intext=CharSets.empty_string, *args, **kwargs):
		self.args = args
		self.attributes = dict(kwargs)
		self.intext = intext
		self.style = None

	def __str__(self):

		return FormatString(self.__class__.__name__, self.open_braket, self.start_tag[:-1], self.close_braket).string

	def __repr__(self):

		return FormatString(self.__class__.__name__, self.open_braket, self.start_tag[:-1], self.close_braket).string

	def config(self, **kwargs):

		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	@property
	def start_tag(self):
		
		return self.get_start_tag()

	@property
	def end_tag(self):

		return self.get_end_tag()

	def get_start_tag(self):
		start_attrs = self.empty_string

		if self.args:

			for arg in self.args:
				start_attrs += FormatString(arg, self.space).string

		if self.attributes:

			for key, value in self.attributes.items():

				if key == '_class':
					key = 'class'
				start_attrs += FormatString(key, self.equal_sign, '"%s"' %(value), self.space).string

		start_tag = FormatString(self.lt_sign, self.tag_name, self.space, start_attrs, self.gt_sign, self.newline).string
		return start_tag

	def get_end_tag(self):

		end_tag = FormatString(self.lt_sign, self.fw_slash, self.tag_name, self.gt_sign, self.newline).string
		return end_tag
	
	def add_child_tags(self, **kwargs):

		for vr_name, tag in kwargs.items():
			if tag.has_child_tag():
				raise AttributeError('child tag is not allowed to have another child tag')
				
		self.child_tags.update(**kwargs)

	def has_child_tag(self):

		if self.child_tags:
			return True
		return False

	def get_child_tag(self, key):

		if key in self.child_tags:
			return self.child_tags[key]

	def has_attribute(self, key):

		if key in self.attributes:
			return True
		return False

	def set_attribute(self, **kwargs):

		self.attributes.update(**kwargs)

	def get_attribute(self, key):

		if self.has_attribute(key):
			return self.attributes[key]

	def has_intext(self):

		if self.intext:
			return True
		return False

	def add_intext(self, intxt):
		_txt = self.empty_string

		if isinstance(intxt, Tag):
			_txt = intxt.dump_string()
		else:
			_txt = intxt

		self.intext += _txt

	def set_style(self, stl):

		self.style = stl

	def has_style(self):

		if self.style:
			return True
		return False

	def dump_string(self):
		tag_doc = self.empty_string

		tag_doc += self.start_tag

		if self.has_intext():
			tag_doc += self.dump_intext()

		if self.has_child_tag():
			tag_doc += self.dump_childs(self.child_tags)

		tag_doc += self.end_tag
		return tag_doc

	def dump_intext(self):
		text = self.empty_string

		if isinstance(self.intext, Tag):
			text = self.intext.dump_string()
		else:
			text = self.intext

		return FormatString(text, self.newline).string

	def dump_self(self):
		_doc = self.empty_string
		_doc += self.start_tag

		_doc += self.dump_intext()
		_doc += self.end_tag

		return _doc

	def dump_childs(self, children):
		_doc = self.empty_string

		child_tags = self.reverse_dict(self.child_tags)
		while len(child_tags):
			ctag = child_tags.popitem()[1]
			_doc += ctag.dump_self()

		return _doc

	def reverse_dict(self, d):
		
		keys = list(d.keys())
		values = list(d.values())
		keys.reverse(), values.reverse()

		return {k:v for k,v in zip(keys, values)}

class MetaTagClass(type):

	def __new__(mcs, name, bases, attrs):

		new_class = super(MetaTagClass, mcs).__new__(mcs, name, bases, attrs)
		cls_name = new_class.__mro__[0].__name__.lower()
		new_class.tag_name = cls_name

		return new_class


class Tag(BaseTag, metaclass=MetaTagClass): pass
