import ply.yacc as yacc
from JSONLexer import tokens

def eval(d:list, st: str, sp: int, inc = 4):
    '''
        input: list, empty string, initial space
        optional: increment space (default inc =  4)
        output : string
    '''
    if d[0] in ['STR', 'NUM', 'BOOL']:
        st += d[1]
        return st
    elif d[0] == 'list':
        st += "["
        for i in d[1]:
            st = eval(i, st, sp) + ","    
        st = st[0:-1]
        st += "]"
        return st
    elif d[0] == 'pair':
        st += " "*sp + d[1] + " : "
        st = eval(d[2], st, sp)
        return st
    elif d[0] == 'kv':
        sp += inc
        st += "{\n"
        for i in d[1]:
            st = eval(i, st, sp) + ",\n"
        st = st[0:-2]
        sp -= inc
        st += "\n" + " "*sp + "}"
        return st
    else: return st


def p_start(p):
    '''start : singltons
            | keyvaluepairs
            | list'''
    p[0] = p[1]


def p_singleton(p):
    ''' singltons : NUM
                    | STR
                    | BOOL'''
    if isinstance(p[1], bool):
        p[0] = ["BOOL", 'true' if p[1] else 'false']
    elif isinstance(p[1], float) or isinstance(p[1],int):
        p[0]= ["NUM", str(p[1])]
    else:
        p[0] = ["STR", p[1]]

def p_key_value_pairs(p):
    '''keyvaluepairs : LPR body RPR'''
    p[0] = ['kv', p[2]]

def p_key_value_pairs2(p):
    '''keyvaluepairs : LPR RPR'''
    p[0] = ['kv', "{}"]

def p_body(p):
    '''body : body COMMA bodybase'''
    p[0] = p[1] + [p[3]]

def p_body2(p):
    '''body : bodybase'''
    p[0] = [p[1]]


def p_body_base(p):
    ''' bodybase : STR COLON start'''
    p[0] = ['pair', p[1], p[3]]


def p_list(p):
    '''list : LBR items RBR'''
    p[0] = ['list', p[2]]


def p_list_items(p):
    '''items : items COMMA baseitems'''
    p[0] = p[1] + [p[3]]


def p_items(p):
    '''items : baseitems'''
    p[0] = [p[1]]

def p_list_base_items(p):
    '''baseitems : singltons
                | keyvaluepairs'''
    p[0] = p[1]

def p_error(p):
    raise Exception("Parsing Error")


# Build the parser
parser = yacc.yacc()


# Debug
# data  = '''
# ["nice", 2 , true]'''
# data = '''"nice": 3'''

# data = '''
# {
#     "skdjf" : "lol", 
# "nice" : false,
#     "works" : {
#         "lol" : false
#     },
#     "skf" : [false, true, 2, 3, "jk", {
#         "great" : "parser"
#     }, {
#         "day" : "monday"}]
# }'''


# s = data.strip()
# try:
#     re = parser.parse(s)
#     if re:
#         e = eval(re, "", 0)
#     else:
#         e = False
#     print(e)
# except Exception as e:
#     print(e)
#     print("ERROR!")

# re = parser.parse(s)


# try:
#     result = parser.parse(s)
#     print(result if result else False)
# except:
#     print("lol")

# while True:
    # try:
        # s = data
    # except EOFError:
    #     break
    # if s == "exit;":
    #     break
    # if not s: break
    # result = parser.parse(s)
    # print(result)