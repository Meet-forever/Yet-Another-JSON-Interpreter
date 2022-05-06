# Yet Another JSON Parser 
## (A JSON Validator + Formatter + Interpreter)

When a user writes an input, it first goes to Lexical Analyzer, i.e., JSONLexer, which tokenizes the given string input into a sequence of tokens. Once it's finished with the lexer and no error occurs, the given input string is syntactically correct.

Then, it goes to the parsing stage, where it recursively checks whether the given input is semantically correct or not, and if there are no grammatical mistakes, it generates an AST. So, at this stage, we know that the input is syntactically valid.

The AST tree is used for formatting the JSON input, which recursively builds the input JSON with proper spaces and newlines.

One can also use the JSON Formatter independently. 

Copy JSONLexer and JSONParser:
<a href="https://github.com/Meet-forever/Yet-Another-JSON-Parser/blob/main/JSONLexer.py" target="_blank">JSONLexer</a>
<a href="https://github.com/Meet-forever/Yet-Another-JSON-Parser/blob/main/JSONParser.py" target="_blank">JSONParser</a>

Required library to run Lexer and Parser:
```bash
pip install ply 
```
Done!

A simple snippet:
```python
from JSONParser import parser, eval
json_input = '"works"' 
''' 
Instead of simple string, one can also use file, 
input function or Docstrings to validate the JSON input. 
'''
try:
    parse = parser.parse(json_input)
    if parse:
        print("Valid!")
    else:
        print("Invalid!")
except Exception as e:
    print(e.message)
```
