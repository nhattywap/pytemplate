from pytemplate import Html, DHtml
from pytemplate.css import Css
from pytemplate.utils.files import write_to_file
from pytemplate.utils.constants import START_DOC
from pytemplate.contents.constants import H1, P, Div, Tr, Td, Input, Small
from pytemplate.contents.tables import Table_Class
from pytemplate.js import JavaScript

html = Html()
html.set_title('this is title')
html.import_css('css/style.css')
html.import_css('css/style2.css')
html.import_script('js/script.js')

p = P('try paragraph', _class='pra', id='kk')
h1 = H1('Hello World', _class='heading')

_css_ = Css('default', 	color="#a3ffd4",
						border="1px solid #123456",
						padding="5px",
						margin="5px",
						width="40%"
						)


box1 = Div(h1, _class='box1')
box1.set_style(_css_.new_css('box1'))
box1.add_child_tags(para=p)
box1.style.update(float='right')

box2 = Div(_class='box2')
box2.config(intext=box1)
box2.add_child_tags(para=p)
box2.set_style(_css_.new_css('box2'))
box2.style.update(float='right')

box3 = Div(_class='box3')
box3.set_style(_css_.new_css('box3'))
box3.config(intext=h1)
box3.add_child_tags(para=p)
box3.style.update(float='left')

box4 = Div(_class='box4')
box4.set_style(_css_.new_css('box4'))
box4.add_child_tags(heading=h1)
box4.style.update(float='left')

table = Table_Class(_class='table', border=1)
table.table_tag.set_style(_css_.new_css('table'))
table.table_tag.style.update(color='#000')

table.create_table(3, 5)
table.insert_to_row(0, 'name', 'age', 'sex', 'gen', 'addr')
table.insert_to_row(1, P('jo').dump_string(), '22', 'm', 'M', 'ass')
table.insert_to_row(2, 'lil', '23', 'f', 'F', 'ass')

html.add_container(box1)
html.add_container(box2)
html.add_container(box3)
html.add_container(box4)
html.add_container(Input(type='button', onclick='aler();', value='click'))
html.add_container(table.get_table())


js = JavaScript()
f1 = js.create_func('add', ('a', 'b'))
f2 = js.create_func('aler')
f2.add_arg('alert("hello")')

js.add_statment('var i = 0')

f1.add_arg('c = 0')
f1.add_arg('c = a + b')
f1.add_arg('return d')
f1.add_arg('d = c', 2)

js.add_func(f1)
js.add_statment('let k = 10')
js.add_func(f2)
#f1.print_args()
#js.add_func(f1, f2)

html.head.add_intext(js.script)

print(START_DOC)

html.prepare()

print(html.get_html())
write_to_file('new_htm', html.get_html())

'''
dhtml = DHtml(box1, box2, box3, box4)

dhtml.rename_index(box1='cont-1', box2='cont-2')
b1 = dhtml.get_container('cont-1')
b1.config(child_tag=Tag('h5', intext='heading 5'))
b2 = dhtml.get_container('cont-2')

b2.config(child_tag=Tag('div', _class='box3', child_tag=Tag('div', _class='box4', child_tag=Tag('p', id='p-last', intext='inner tag'))))

dhtml.import_css('css/style.css')
script = 'function(){ return 1+2}'
js = JavaScript(script)
dhtml.head.add_intext(js.script.dump_string())

dhtml.prepare()
print('----------------------')
print(dhtml.get_html())
write_to_file('new_htm', dhtml.get_html())
'''


















































