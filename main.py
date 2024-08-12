from lexer import Lexer
from parser import Parser
text_input = ""
print(4 + 5 - 2)
""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token) 