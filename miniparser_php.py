import ply.yacc as yacc
from miniphp_lexer import tokens
import miniphp_lexer
import sys



# 
# Nombres:
#Juan David Osorio Ortiz
# Johnatan Palacios Londoño
# Valentina Gomez Isaza 


VERBOSE = 1

def p_program(p):
    'program : OPEN_TAG declaration_list CLOSE_TAG'
    pass

def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    pass

def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass

def p_declaration(p):
    '''declaration : var_declaration
									| fun_declaration
									| header_declaration
									| class_declaration
									| print_stmt
									| selection_stmt
									| iteration_stmt
    '''
    pass

def p_print_stmt(p):
    '''print_stmt : print_stmt ECHO STRING SEMICOLON
									| print_stmt ECHO ID SEMICOLON
									| empty
    '''
    pass

def p_header_declaration(p):
    '''header_declaration : REQUIRE LPAREN STRING RPAREN SEMICOLON 
													| REQUIRE STRING SEMICOLON
		'''
    pass

def p_class_declaration(p):
    'class_declaration : CLASS FUNCTION_NAME class_stmt'
    pass

def p_class_stmt1(p):
    'class_stmt : LBLOCK attributes methods RBLOCK'
    pass

def p_class_stmt2(p):
    'class_stmt : LBLOCK empty RBLOCK'
    pass

def p_class_stmt3(p):
    'class_stmt : LBLOCK attributes RBLOCK'
    pass

def p_attributes1(p):
    'attributes : attributes scope var_declaration'
    pass

def p_attributes2(p):
    'attributes : scope var_declaration'
    pass

def p_methods1(p):
    'methods : methods scope fun_declaration'
    pass

def p_methods2(p):
    'methods : scope fun_declaration'
    pass

def p_scope(p):
    '''scope : PRIVATE
                | PUBLIC
                | PROTECTED
    '''
    pass

def p_var_declaration(p):
    '''var_declaration : ID SEMICOLON var_declaration
												| ID SEMICOLON
												| ID EQUAL NUMBER SEMICOLON var_declaration
												| ID EQUAL NUMBER SEMICOLON
												| ID EQUAL boolean SEMICOLON var_declaration
												| ID EQUAL boolean SEMICOLON
												| ID EQUAL ID SEMICOLON var_declaration
												| ID EQUAL ID SEMICOLON
												| AMPERSANT ID SEMICOLON var_declaration
												| AMPERSANT ID SEMICOLON
    '''
    pass

def p_fun_declaration(p):
    'fun_declaration : FUNCTION FUNCTION_NAME LPAREN params RPAREN compount_stmt'
    pass

def p_params_1(p):
	'params : param_list'
	pass

def p_params_2(p):
	'params : empty'
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_1(p):
	'param : ID'
	pass

def p_param_2(p):
	'param : ID LBRACKET RBRACKET'
	pass

def p_compount_stmt(p):
	'compount_stmt : LBLOCK print_stmt local_declarations print_stmt statement_list print_stmt RBLOCK'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'	
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
	'''
	pass	

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt(p):
	'''selection_stmt : IF LPAREN expression RPAREN statement
						| IF LPAREN expression RPAREN statement ELSE statement
						| SWITCH LPAREN var RPAREN statement
						| CASE NUMBER COLON statement BREAK SEMICOLON
						| DEFAULT COLON statement BREAK SEMICOLON
						| print_stmt
	'''
	pass

def p_iteration_stmt(p):
	'''iteration_stmt : FOR LPAREN var_declaration SEMICOLON expression SEMICOLON additive_expression RPAREN statement 
					| WHILE LPAREN expression RPAREN statement
	'''
	pass

def p_iteration_stmt_3(p):
	'iteration_stmt : print_stmt'
	pass

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var EQUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var EQUAL AMPERSANT ID'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass

def p_relop(p):
	'''relop : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| ISEQUAL
	'''
	pass

def p_additive_expression_1(p):
	'additive_expression : additive_expression addop term'
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_additive_expression_3(p):
	'additive_expression : term MINUSMINUS'
	pass

def p_additive_expression_4(p):
	'additive_expression : term PLUSPLUS'
	pass

def p_addop(p):
	'''addop : PLUS 
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : TIMES
			| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMBER' 
	pass
	
def p_factor_5(p):
	'factor : boolean' 
	pass

def p_call(p):
	'call : ID LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass
	
def p_boolean(p):
	'''boolean : TRUE
					| FALSE
	'''
	pass

def p_empty(p):
	'empty : '
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(miniphp_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'PRUEBA.php'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("El parser reconocio correctamente todo")
	#input()