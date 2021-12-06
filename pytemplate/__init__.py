from pytemplate.contents.Tags import Tag
from pytemplate.contents.constants import TagSets, set_Style, set_Script, set_Link
from pytemplate.utils.constants import (
		EMPTY_STRING,
		HYFEN,
		DASH,
		DOT
	)
from pytemplate.css import GenericBoxStyle

class Html:

	def __init__(self):
		self.title = TagSets.title()
		self.head = TagSets.head()
		self.body = TagSets.body()
		self.html = TagSets.html()
		self.containers = {}
		self.style = EMPTY_STRING

	def set_title(self, _tit):

		self.title.config(intext=_tit)

	def prepare(self):
		content = self.get_containers()

		self.head.add_child_tags(title=self.title)
		
		if self.style:
			style = set_Style(text=self.style)
			self.head.add_child_tags(style=style)
		
		self.body.config(intext=content)

	def get_html(self):
		
		self.html.config(intext=self.head)
		self.html.add_child_tags(body=self.body)

		return self.html.dump_string()

	def import_css(self, path, rel=None, _type=None):

		link = set_Link(path=path, rel=rel, _type=_type)
		self.head.add_intext(link)

	def import_script(self, src, lang=None):

		script = set_Script(lang, src)
		self.head.add_intext(script)

	def add_container(self, _box):
		if isinstance(_box, Tag):

			self.containers.update({_box: _box.style})
		else:
			print('Value Muse Be Tag Object')

	def get_containers(self):
		content_string = EMPTY_STRING

		if self.containers:
			for contain, style in self.containers.items():
				content_string += contain.dump_string()
				if style is not None:
					
					self.style += style.dump_css()

		return content_string

class DHtml(Html):

	def __init__(self, *args):
		super().__init__()
		self.args = [arg for arg in args if isinstance(arg, Tag)]
		self.html_containers = self.get_mapping()
		self.containers = {tag: tag.style for tag in self.args}

	def get_mapping(self):

		return {tag.style._class.replace(DASH, HYFEN): tag for tag in self.args}

	def rename_index(self, **kwargs):

		for key, nkey in kwargs.items():

			key = key.replace(DASH, HYFEN)
			if key in self.html_containers:
				_val = self.html_containers[key]
				self.html_containers.pop(key)
				self.html_containers[nkey] = _val

	def get_container(self, tag_refr):

		if tag_refr in self.html_containers:
			return self.html_containers[tag_refr]
