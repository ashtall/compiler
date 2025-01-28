from lexer import *
from parser import *
from emitter import *

if __name__ == '__main__':
    file = open("test.fc", 'r')
    code = file.read()
    file.close()
    result = ''
    lexer = Lexer(code)
    emitter = Emitter("test.c")
    parser = Parser(lexer, emitter)

    parser.program()
    emitter.writeFile()