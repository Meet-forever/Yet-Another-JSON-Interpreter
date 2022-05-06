import ply.lex as lex

tokens = ["LPR", "RPR", "LBR", "RBR", "STR", "NUM", "BOOL", "COLON", "COMMA"]

t_LPR = r'\{'
t_RPR = r'\}'
t_LBR = r'\['
t_RBR = r'\]'
t_COLON = r':'
t_COMMA = r','

def t_BOOL(t):
    r'(true)|(false)'
    t.type = 'BOOL'
    t.value = t.value == "true"
    return t
    
def t_string(t):
    r'"[a-zA-Z0-9]*"'
    t.type = 'STR'
    return t

def t_number(t):
    r'(\-|\+)?[0-9]+(\.[0-9]+)?'
    t.type = 'NUM'
    if '.' in t.value:
        t.value = float(t.value)
    else: t.value = int(t.value)
    return t

def t_error(t):
    pass

t_ignore = " \r\n\t"
# t_ignore_COMMENT = r'\#.*'

lexer = lex.lex()

# Debug
# data = '''
# {
#     "nice": ["nice", 4, 5],
#     "works" : [{"n"}],
#     sd
# }
# '''

# lexer.input(data.strip())

# while True:
#     try:
#         tok = lexer.token()
#         if not tok:
#             break
#     except:
#         break
#     # if not tok:
#         # break      # No more input
#     # print(tok)