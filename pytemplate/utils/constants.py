from pytemplate.utils.fmt import FormatString

LT_SIGN = '<'
GT_SIGN = '>'
TEMEHERTE_ANKERO = '!'
FW_SLASH = '/'
EQUAL_SIGN = '='
DOT = '.'
COMA = ','
HASH = '#'
SPACE = ' '
NEWLINE = '\n'
TAB = '\t'
COLON = ':'
SEMICOLON = ';'
DASH = '_'
HYFEN = '-'
OPEN_BRES = '{'
CLOSE_BRES = '}'
OPEN_BRAKET = '('
CLOSE_BRAKET = ')'
EMPTY_STRING = ''

START_DOC = FormatString(LT_SIGN, TEMEHERTE_ANKERO, 'DOCTYPE html', GT_SIGN, '\n').string

class get_NewType:

	def __init__(self, cls_name, bases=(), **kwargs):
		self.cls_name = cls_name
		self.bases = bases
		self.kwargs = kwargs

	def __call__(self):

		return type(
				self.cls_name,
				self.bases,
				self.kwargs
			)

def constra_class(cls_name,/, **kwargs):

	new_cls = get_NewType(cls_name=cls_name, **kwargs)

	return new_cls()

CharSets = constra_class(
						'CharSets',
						lt_sign = LT_SIGN,
						gt_sign = GT_SIGN,
						temeherte_ankero = TEMEHERTE_ANKERO,
						fw_slash = FW_SLASH,
						equal_sign = EQUAL_SIGN,
						dot = DOT,
						coma = COMA,
						hash = HASH,
						space = SPACE,
						newline = NEWLINE,
						tab = TAB,
						colon = COLON,
						semicolon = SEMICOLON,
						dash = DASH,
						hyfen = HYFEN,
						open_bres = OPEN_BRES,
						close_bres = CLOSE_BRES,
						open_braket = OPEN_BRAKET,
						close_braket = CLOSE_BRAKET,
						empty_string = EMPTY_STRING
						)































