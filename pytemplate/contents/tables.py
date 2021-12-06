from pytemplate.utils.constants import EMPTY_STRING
from pytemplate.css import Css
from .constants import Table, Tr, Td, Th
from .Tags import Tag

def is_tag(obj):

	if isinstance(obj, Tag):
		return True
	return False

class Table_Class:

	def __init__(self, *args, **kwargs):
		self.table_tag = Table(*args, **kwargs)
		self.table_vals = []

	def get_table(self):

		self.table_tag.config(intext=self.dump_table())
		return self.table_tag

	def add_row(self, row, *rowargs):
		row = Row(row, *rowargs)
		self.table_vals.append(row)

	def insert_to_row(self, rIndex, *rowargs):
		row = self.table_vals[rIndex]
		if len(row.values) == len(rowargs):
			for i in range(len(row.values)):
				row.values[i].config(intext=rowargs[i])

	def add_column(self, rIndex, *cols):
		row = self.table_vals[rIndex]
		row.values.extend(list(cols))

	def create_table(self, row, col):
		_table = []

		for i in range(row):
			tds = [Td() for j in range(col)]
			_row = Row(Tr(), *tds)
			_table.append(_row)

		self.table_vals = _table

	def dump_table(self):
		table_doc = EMPTY_STRING

		for row in self.table_vals:
			row_doc = EMPTY_STRING
			
			for data in row.values:
				row_doc += data.dump_string()
			row.row.config(intext=row_doc)
			table_doc += row.row.dump_string()

		return table_doc

class Row:

	def __init__(self, row, *values):
		self.row = row if is_tag(row) else Td()
		self.values = [val if is_tag(val) else Td() for val in values]



















