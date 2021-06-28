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
# To handle  reserverd words, the rules were writen in a dicc ID/KEYS : VALUE  cause it reduces the number
# or regular expression rules and prevents some issues with identifiers
reserved = {
    'abstract': 'ABSTRACT',
    'array': 'ARRAY',
    'as': 'AS',
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'catch': 'CATCH',
    'clone': 'CLONE',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'declare': 'DECLARE',
    'default': 'DEFAULT',
    'do': 'DO',
    'echo': 'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'empty': 'EMPTY',
    'enddeclare': 'ENDDECLARE',
    'endfor': 'ENDFOR',
    'endforeach': 'ENDFOREACH',
    'endif': 'ENDIF',
    'endswitch': 'ENDSWITCH',
    'endwhile': 'ENDWHILE',
    'eval': 'EVAL',
    'exit': 'EXIT',
    'extends': 'EXTENDS',
    'final': 'FINAL',
    'finally': 'FINALLY',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'function': 'FUNCTION',
    'global': 'GLOBAL',
    'goto': 'GOTO',
    'if': 'IF',
    'include': 'INCLUDE',
    'implements': 'IMPLEMENTS',
    'include_once': 'INCLUDE_ONCE',
    'instanceof': 'INSTANCEOF',
    'isset': 'ISSET',
    'insteadog': 'INSTEADOF',
    'interface': 'INTERFACE',
    'list': 'LIST',
    'new': 'NEW',
    'print': 'PRINT',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'public': 'PUBLIC',
    'require': 'REQUIRE',
    'require_once': 'REQUIRE_ONCE',
    'return': 'RETURN',
    'static': 'STATIC',
    'switch': 'SWITCH',
    'unset': 'UNSET',
    'use': 'USE',
    'var': 'VAR',
    'while': 'WHILE',
    'try': 'TRY',
    'throw': 'THROW',
    'trait': 'TRAIT',
    'yield': 'YIELD',
    'namespace': 'NAMESPACE',
}

# unparsed
other = [
    # invisible characters
    'WHITESPACE', 'NEWLINE',
    # tags
    # reference:
    # https://www.php.net/manual/en/language.basic-syntax.phptags.php
    'OPEN_TAG', 'CLOSE_TAG',
    # Comments
    # reference:
    # https://www.php.net/manual/en/language.basic-syntax.comments.php
    'ONE_LINE_COMMENT', 'MULTI_LINE_COMMENT',
    # Variable
    'VARIABLE', 'NUMBER', 'STRING','FUNCTION_NAME',
    # Boolean 
    'TRUE','FALSE',
]

tokens = list(reserved.values()) + other + [
    # Operators
    # reference:
    # http://php.net/manual/en/language.operators.php
    # Arithmetic Operators
    'PLUS', 'MINUS', 'TIMES', 'DIVISION', 'MODULO', 'EXPONENTIATION',
    # Bitwise Operator
    # ref:
    # https://www.php.net/manual/en/language.operators.bitwise.php 'BITWISE_AND', 
    'BITWISE_OR', 'BITWISE_XOR','BITWISE_NOT',  'SHIFT_LEFT', 'SHIFT_RIGHT',
    
    # Assignment Operators
    'EQUAL', 'TIMES_EQUAL', 'DIVISION_EQUAL', 'MOD_EQUAL', 'PLUS_EQUAL',
    'MINUS_EQUAL', 'SL_EQUAL', 'SR_EQUAL', 'AND_EQUAL', 'OR_EQUAL', 'XOR_EQUAL',
    'CONCAT_EQUAL',
    # Comparison Operator
    # LT -> Less than
    # LTE -> Less than or equal
    # GT -> Greater than
    # GTE -> Greather than or equal
    # SO -> Spaceship operator
    'EQUALS', 'IDENTICAL', 'NOT_EQUAL', 'NOT_IDENTICAL', 'LT', 'LTE', 'GT', 'GTE', 'SO',
    # Execution  Operator
    'BACKTICKS',
    # Error control operator
    'AT_SIGN',
    # Increment / decrement operators
    # INC -> INCREMENT
    # DEC -> DECREMENT
    'INC', 'DEC',
    # Logical Operator
    'AND', 'OR', 'NOT', 'XOR',
    # String Operator
    'CONCATENATION',
    # OTher operators
    # object operator : ->
    # double arrow : =>
    # double colon : ::
    # reference:
    # https://www.php.net/manual/en/language.oop5.paamayim-nekudotayim.php
    # https://www.php.net/manual/en/functions.arrow.php
    # https://www.php.net/manual/en/language.types.object.php
    'OBJECT_OPERATOR', 'DOUBLE_ARROW', 'DOUBLE_COLON',
    # Symbols
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'DOLLAR', 'COMMA', 'QUESTION',
    'COLON', 'SEMICOLON', 'NS_SEPARATOR','SINGLE_QUOTE', 'AMPERSANT'
]

# Ignored characters
t_ignore = " \t\r"
# Operators
# Arithmetic operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVISION = r'\/'
t_MODULO = r'\%'
t_EXPONENTIATION = r'\*\*'
# Bitwise Operator
#t_BITWISE_AND = r'\&'
t_BITWISE_OR = r'\|'
t_BITWISE_XOR = r'\^'
t_BITWISE_NOT = r'\~'
t_SHIFT_LEFT = r'\<\<'
t_SHIFT_RIGHT = r'\>\>'
# Assignment Operators
t_EQUAL = r'\='
t_TIMES_EQUAL = r'\*\='
t_DIVISION_EQUAL = r'\/\='
t_MOD_EQUAL = r'\%\='
t_PLUS_EQUAL = r'\+\='
t_MINUS_EQUAL = r'\-\='
t_SL_EQUAL = r'\<\<\='
t_SR_EQUAL = r'\>\>\='
t_AND_EQUAL = r'\&\='
t_OR_EQUAL = r'\|\='
t_XOR_EQUAL = r'\^\='
t_CONCAT_EQUAL = r'\.\='
# Comparison Operator
t_EQUALS = r'\=\='
t_IDENTICAL = r'\=\=\='
t_NOT_EQUAL = r'\!\='
t_NOT_IDENTICAL = r'\!\=\='
t_LT = r'\<'
t_LTE = r'\<\='
t_GT = r'\>'
t_GTE = r'\>\='
t_SO = r'\<\=\>'
# Execution  Operator
t_BACKTICKS = r'\`'
# Error control operator
t_AT_SIGN = r'\@'
# Increment / decrement operators
t_INC = r'\+\+'
t_DEC = r'\-\-'
# Logical Operator
t_AND = r'(\&\&)|(and)'
t_OR = r'\|\|'
t_NOT = r'\!'
t_XOR = r'xor'
# String Operator
t_CONCATENATION = r'\.'
# OTher operators
t_OBJECT_OPERATOR = r'\-\>'
t_DOUBLE_ARROW = r'\=\>'
t_DOUBLE_COLON = r'\:\:'
# Symbols
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOLLAR = r'\$'
t_COMMA = r'\,'
t_QUESTION = r'\?'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_NS_SEPARATOR = r'\\'
t_SINGLE_QUOTE = r'\''
t_AMPERSANT = r'\&'

def t_FUNCTION_NAME(t):
    r'function[ ][a-zA-Z_][a-zA-Z_0-9]*'
    return t
    
# March reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # Regular expresion for reserved words
    # with reserved.get(t.value,'ID'), the t.value is send to be find in the reserved words dicc, if it is the
    # value of 'ID'  is overwritten by the dicc value equivalent to t.type:
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    #If the value  is not found in the dicc by default the returned value is ID
    #if it happens the function t_error if is diferent the token is returned
    if t.type == 'ID': 
        t_error(t)
    else:
        return t

# Other
# Newline
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# tags
def t_OPEN_TAG(t):
    r'(<\?|<%)php'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_CLOSE_TAG(t):
    r'[?]>(\t\n\r)?'
    t.lexer.lineno += t.value.count("\n")
    return t

# comments
def t_ONE_LINE_COMMENT(t):
    r'[ |\t]*?(\/\/(.|\t| )*|\#(.|\t| )*)'
    t.lexer.lineno += t.value.count("\n")
    # return t
    pass

def t_MULTI_LINE_COMMENT(t):
    r'\/\*(.|\n)*?\*\/'
    t.lexer.lineno += t.value.count("\n")
    # return t
    pass

# others
def t_VARIABLE(t):
    r'\$[A-Za-z_][\w_]*'
    return t

def t_NUMBER(t):
    r'(\+|\-)?[0-9]+((.[0-9]+((e|E)(\-|\+)?[0-9]+(.[0-9]+))?)|(e|E)(\-|\+)?[0-9]+)?'
    return t

def t_STRING(t):
    r'(\".*?(?<!\\)\") | (\'.*?(?<!\\)\')'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_TRUE(t):
    r'true'
    return t

# default function of lex library.
def t_error(t):
    #Function to take the first word found in t.value
    #ord() to take and character and return the ascci code
    word = ''
    for letter in t.value:
        if (ord(letter) != 10):
            word += letter
        else:
            break #stop the for if find an ascci 10
    #----------------------------------------------------
    print("Lexical error '%s'" % word)
    t.lexer.skip(1)

# this line is used to build the lexer
# do not delete it
lexer = lex.lex()

def test(data, lexer):
    lexer.input(data)  # assign the content to the lexer
    while True:  # loops through the entire string extracted from the test document
        tok = lexer.token()  # if is a valid toked proceed to analyze it
        if not tok:
            break# Close the program if is not a valid token
        print(tok)  # Print the result of the analysis

# Input command verification
if __name__ == '__main__':
    # if the input command accomplish the conditions, the program is executed
    if (len(sys.argv) > 1):
        fin = sys.argv[1]  # Assign the test doc address to fin
        # Open the file in read mode, ussing the open function
        f = open(fin, 'r')
        data = f.read()  # Copy the content of test doc to variable data
        print(data)  # Print all the content
        lexer.input(data)  # assign the content to the lexer
        test(data, lexer)  # call the funcion that starts the lexical analysis
    else:
        print('##############################')
        print('#')
        print('#')
        print('the input mask is = python minilexer_php.py <test doc address> ')
        print('#')
        print('#')
        print('##############################')
        breakpoint
    # input()
