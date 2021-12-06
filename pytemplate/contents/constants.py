from pytemplate.utils.constants import constra_class, CharSets, get_NewType
from .Tags import Tag

def set_Link(path, rel, _type):

	return Link(
				rel=rel if rel != None else 'stylesheet',
				type=_type if _type != None else 'text/css',
				href=path
			).start_tag

def set_Style(text):

	return Style(intext=text, type='text/css')

def set_Script(language, src):

	return Script(
				language=language if language != None else 'JavaScript',
				src=src
			).dump_string()

def create_tag(tag_name):

	new_class = get_NewType(tag_name, bases=(Tag,), **{})()
	def __init__(self, intext=CharSets.empty_string, *args, **kwargs):
		super(new_class, self).__init__(intext, *args, **kwargs)
		self.child_tags = {}

	new_class.__init__ = __init__

	return new_class

Div = create_tag('div')

Small = create_tag('small')

Link = create_tag('link')

Style = create_tag('Style')

Script = create_tag('Script')

Html = create_tag('Html')

Head = create_tag('head')

Title = create_tag('title')

Body = create_tag('Body')

Input = create_tag('input')

Form = create_tag('Form')

Table = create_tag('table')

Tr = create_tag('tr')

Th = create_tag('th')

Td = create_tag('td')

Br = create_tag('br')

Hr = create_tag('hr')

H1 = create_tag('h1')

P = create_tag('P')

Bold = create_tag('b')

Italic = create_tag('i')

Strong = create_tag('strong')

Em = create_tag('em')

Small = create_tag('small')

TagSets = constra_class(
		'TagSets',
		link=Link,
		style=Style,
		script=Script,
		html=Html,
		head=Head,
		title=Title,
		body=Body,
		div=Div,
		input=Input,
		form=Form,
		table=Table,
		br=Br,
		hr=Hr,
		h1=H1,
		p=P,
		bold=Bold,
		italic=Italic,
		strong=Strong,
		em=Em,
		small=Small,
	)





























