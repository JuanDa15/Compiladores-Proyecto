import ply.lex as lex
import sys
import re

# 
# Nombres:
#Juan David Osorio Ortiz
# Johnatan Palacios Londoño
# Valentina Gomez Isaza 
# -------------------------------------------------------------------------------------------------------------------
# ply doc: https://ply.readthedocs.io/en/latest/ply.html
# pass at the end of some rules are to discard the token, if you want to see the token comment the
# pass and write 'return t' or uncomment the line
# Other way to discard  a token is using the prefix "ignore_" like t_ignore_COMMENT = r''
# -------------------------------------------------------------------------------------------------------------------
# List of tokens
# reference:
# https://www.php.net/manual/en/reserved.keywords.php

# list of tokens
tokens = (
    # Reserverd words
    'BREAK',    
    'ELSE', 
    'ECHO', 
    'FOR',
    'IF', 
    'RETURN', 
    'WHILE', 
    'REQUIRE',
    'TRUE',
    'FALSE',
    'FUNCTION',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'CLASS',
    'PUBLIC',
    'PRIVATE',
    'PROTECTED',
    # OTHER
    # tags
    # reference:
    # https://www.php.net/manual/en/language.basic-syntax.phptags.php
    'OPEN_TAG',
    'CLOSE_TAG',

    'ID',
    'NUMBER',
    'STRING',
    'FUNCTION_NAME',

    # Operators
    # reference:
    # http://php.net/manual/en/language.operators.php
    # Arithmetic Operators
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',

    # Assignment Operators
    'EQUAL',

    # Comparison Operator
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'DEQUAL', 
    'ISEQUAL',

    # Increment / decrement operators
    'PLUSPLUS',
    'MINUSMINUS',

    # Symbols
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'\{'
t_RBLOCK   = r'\}'
t_COLON   = r':'
t_AMPERSANT = r'\&'

# Reserved words
def t_FALSE(t):
    r'false'
    return t

def t_TRUE(t):
    r'true'
    return t
    
def t_CLASS(t):
    r'class'
    return t    
    
def t_PRIVATE(t):
    r'private'
    return t
    
def t_PUBLIC(t):
    r'public'
    return t
    
def t_PROTECTED(t):
    r'protected'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_WHILE(t):
    r'while'
    return t
    
def t_FUNCTION(t):
    r'function'
    return t
    
def t_SWITCH(t):
    r'switch'
    return t
    
def t_CASE(t):
    r'case'
    return t
    
def t_DEFAULT(t):
    r'default'
    return t

def t_BREAK(t):
	r'break'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_ECHO(t):
	r'echo'
	return t

def t_FOR(t):
	r'for'
	return t

def t_IF(t):
	r'if'
	return t

def t_RETURN(t):
	r'return'
	return t

#------------------------------------
# tags
def t_OPEN_TAG(t):
    r'(<\?|<%)php'
    return t

def t_CLOSE_TAG(t):
    r'\?>|\%>'
    return t
#------------------------------------
def t_STRING(t):
    r'(\"(.)*?\"|\'(.)*?\')'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\$ \w+(_\d\w)*'
    return t

def t_FUNCTION_NAME(t):
    r'[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
    return t
#------------------------------------
def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
#-------------------------------------
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t
#-------------------------------------
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comments
# reference:
# https://www.php.net/manual/en/language.basic-syntax.comments.php
def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n') 

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1
#------------------------------------------------------------------
t_ignore = ' \t'
# default function of lex library.
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data) # assign the content to the lexer
	while True:  # loops through the entire string extracted from the test document
		tok = lexer.token() # if is a valid toked proceed to analyze it
		if not tok:
			break # Close the program if is not a valid token
		print (tok) # Print the result of the analysis

# this line is used to build the lexer
# do not delete it
lexer = lex.lex()

# Input command verification
if __name__ == '__main__':
    # if the input command accomplish the conditions, the program is executed
    if (len(sys.argv) > 1):
        fin = sys.argv[1]  # Assign the test doc address to fin
        # Open the file in read mode, ussing the open function
        f = open(fin, 'r')
        data = f.read()  # Copy the content of test doc to variable data
        #print(data)  # Print all the content
        lexer.input(data)  # assign the content to the lexer
        test(data, lexer)  # call the funcion that starts the lexical analysis
    else:
        print('##############################')
        print('#')
        print('#')
        print('the input mask is = python miniphp_lexer.py <test doc address> ')
        print('#')
        print('#')
        print('##############################')
        breakpoint
    # input()
