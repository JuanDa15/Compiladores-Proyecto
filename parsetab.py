
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSANT BREAK CASE CLASS CLOSE_TAG COLON COMMA DEFAULT DEQUAL DIVIDE ECHO ELSE EQUAL FALSE FOR FUNCTION FUNCTION_NAME GREATER GREATEREQUAL ID IF ISEQUAL LBLOCK LBRACKET LESS LESSEQUAL LPAREN MINUS MINUSMINUS NUMBER OPEN_TAG PLUS PLUSPLUS PRIVATE PROTECTED PUBLIC RBLOCK RBRACKET REQUIRE RETURN RPAREN SEMICOLON STRING SWITCH TIMES TRUE WHILEprogram : OPEN_TAG declaration_list CLOSE_TAGdeclaration_list : declaration_list declarationdeclaration_list : declarationdeclaration : var_declaration\n\t\t\t\t\t\t\t\t\t| fun_declaration\n\t\t\t\t\t\t\t\t\t| header_declaration\n\t\t\t\t\t\t\t\t\t| class_declaration\n\t\t\t\t\t\t\t\t\t| print_stmt\n\t\t\t\t\t\t\t\t\t| selection_stmt\n\t\t\t\t\t\t\t\t\t| iteration_stmt\n    print_stmt : print_stmt ECHO STRING SEMICOLON\n\t\t\t\t\t\t\t\t\t| print_stmt ECHO ID SEMICOLON\n\t\t\t\t\t\t\t\t\t| empty\n    header_declaration : REQUIRE LPAREN STRING RPAREN SEMICOLON \n\t\t\t\t\t\t\t\t\t\t\t\t\t| REQUIRE STRING SEMICOLON\n\t\tclass_declaration : CLASS FUNCTION_NAME class_stmtclass_stmt : LBLOCK attributes methods RBLOCKclass_stmt : LBLOCK empty RBLOCKclass_stmt : LBLOCK attributes RBLOCKattributes : attributes scope var_declarationattributes : scope var_declarationmethods : methods scope fun_declarationmethods : scope fun_declarationscope : PRIVATE\n                | PUBLIC\n                | PROTECTED\n    var_declaration : ID SEMICOLON var_declaration\n\t\t\t\t\t\t\t\t\t\t\t\t| ID SEMICOLON\n\t\t\t\t\t\t\t\t\t\t\t\t| ID EQUAL NUMBER SEMICOLON var_declaration\n\t\t\t\t\t\t\t\t\t\t\t\t| ID EQUAL NUMBER SEMICOLON\n\t\t\t\t\t\t\t\t\t\t\t\t| ID EQUAL boolean SEMICOLON var_declaration\n\t\t\t\t\t\t\t\t\t\t\t\t| ID EQUAL boolean SEMICOLON\n\t\t\t\t\t\t\t\t\t\t\t\t| ID EQUAL ID SEMICOLON var_declaration\n\t\t\t\t\t\t\t\t\t\t\t\t| ID EQUAL ID SEMICOLON\n\t\t\t\t\t\t\t\t\t\t\t\t| AMPERSANT ID SEMICOLON var_declaration\n\t\t\t\t\t\t\t\t\t\t\t\t| AMPERSANT ID SEMICOLON\n    fun_declaration : FUNCTION FUNCTION_NAME LPAREN params RPAREN compount_stmtparams : param_listparams : emptyparam_list : param_list COMMA paramparam_list : paramparam : IDparam : ID LBRACKET RBRACKETcompount_stmt : LBLOCK print_stmt local_declarations print_stmt statement_list print_stmt RBLOCKlocal_declarations : local_declarations var_declarationlocal_declarations : emptystatement_list : statement_list statementstatement_list : emptystatement : expression_stmt\n\t\t\t\t| compount_stmt\n\t\t\t\t| selection_stmt\n\t\t\t\t| iteration_stmt\n\t\t\t\t| return_stmt\n\texpression_stmt : expression SEMICOLONexpression_stmt : SEMICOLONselection_stmt : IF LPAREN expression RPAREN statement\n\t\t\t\t\t\t| IF LPAREN expression RPAREN statement ELSE statement\n\t\t\t\t\t\t| SWITCH LPAREN var RPAREN statement\n\t\t\t\t\t\t| CASE NUMBER COLON statement BREAK SEMICOLON\n\t\t\t\t\t\t| DEFAULT COLON statement BREAK SEMICOLON\n\t\t\t\t\t\t| print_stmt\n\titeration_stmt : FOR LPAREN var_declaration SEMICOLON expression SEMICOLON additive_expression RPAREN statement \n\t\t\t\t\t| WHILE LPAREN expression RPAREN statement\n\titeration_stmt : print_stmtreturn_stmt : RETURN SEMICOLONreturn_stmt : RETURN expression SEMICOLONexpression : var EQUAL expressionexpression : simple_expressionexpression : var EQUAL AMPERSANT IDvar : IDvar : ID LBRACKET expression RBRACKETsimple_expression : additive_expression relop additive_expressionsimple_expression : additive_expressionrelop : LESS \n\t\t\t| LESSEQUAL\n\t\t\t| GREATER\n\t\t\t| GREATEREQUAL\n\t\t\t| DEQUAL\n\t\t\t| ISEQUAL\n\tadditive_expression : additive_expression addop termadditive_expression : termadditive_expression : term MINUSMINUSadditive_expression : term PLUSPLUSaddop : PLUS \n\t\t\t| MINUS\n\tterm : term mulop factorterm : factormulop : TIMES\n\t\t\t| DIVIDE\n\tfactor : LPAREN expression RPARENfactor : varfactor : callfactor : NUMBERfactor : booleancall : ID LPAREN args RPARENargs : args_list\n\t\t\t| empty\n\targs_list : args_list COMMA expressionargs_list : expressionboolean : TRUE\n\t\t\t\t\t| FALSE\n\tempty : '
    
_lr_action_items = {'OPEN_TAG':([0,],[2,]),'$end':([1,24,],[0,-1,]),'ID':([2,3,4,5,6,7,8,9,10,11,13,17,25,26,27,28,34,35,37,38,39,42,48,49,51,52,54,67,69,70,71,72,73,74,76,77,78,81,82,83,84,85,86,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,122,123,124,126,127,128,129,130,132,134,136,137,138,141,143,153,155,156,157,158,160,161,164,168,172,173,174,175,176,178,180,181,183,184,185,186,187,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,29,-13,-2,41,12,43,58,66,58,12,58,-27,12,91,-15,-16,58,58,-55,-49,-50,-51,-52,-53,-102,-61,58,-11,-12,12,12,12,-35,12,-24,-25,-26,58,58,58,58,58,58,-74,-75,-76,-77,-78,-79,-84,-85,58,-88,-89,58,-54,-102,-65,58,58,-33,-29,-31,91,-14,-19,12,-18,-56,169,-58,-60,12,-46,-66,-63,-37,-17,58,58,-59,-102,-45,58,-57,58,-48,-61,-47,58,-44,-62,]),'AMPERSANT':([2,3,4,5,6,7,8,9,10,11,17,25,27,38,42,48,51,52,69,70,71,72,73,74,76,77,81,82,83,84,85,86,95,96,97,98,100,101,119,122,123,124,127,128,129,130,134,136,137,138,141,153,155,156,157,158,160,161,164,168,173,175,178,185,186,187,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,13,13,-27,13,-15,-16,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,13,13,13,-35,13,-24,-25,-26,-102,143,-102,-54,-102,-65,-102,-33,-29,-31,-14,-19,13,-18,-56,-58,-60,13,-46,-66,-63,-37,-17,-102,-59,-45,-57,-102,-44,-62,]),'FUNCTION':([2,3,4,5,6,7,8,9,10,11,17,25,27,42,48,51,52,69,70,71,72,73,74,77,81,82,83,84,85,86,96,97,98,100,119,122,124,127,128,129,130,134,136,137,138,141,153,155,158,160,161,164,165,168,173,178,185,186,187,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,-27,-36,-15,-16,-55,-49,-50,-51,-52,-53,-61,-11,-12,-34,-30,-32,-35,-24,-25,-26,-102,-102,-54,-65,-102,-33,-29,-31,-14,-19,14,-18,-56,-58,-60,-66,-63,-37,-17,14,-102,-59,-57,-102,-44,-62,]),'REQUIRE':([2,3,4,5,6,7,8,9,10,11,17,25,27,42,48,51,52,69,70,71,72,73,74,77,81,82,83,84,85,86,100,119,122,124,127,128,129,130,134,136,138,141,153,155,158,160,161,164,168,173,178,185,186,187,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,-27,-36,-15,-16,-55,-49,-50,-51,-52,-53,-61,-11,-12,-34,-30,-32,-35,-102,-102,-54,-65,-102,-33,-29,-31,-14,-19,-18,-56,-58,-60,-66,-63,-37,-17,-102,-59,-57,-102,-44,-62,]),'CLASS':([2,3,4,5,6,7,8,9,10,11,17,25,27,42,48,51,52,69,70,71,72,73,74,77,81,82,83,84,85,86,100,119,122,124,127,128,129,130,134,136,138,141,153,155,158,160,161,164,168,173,178,185,186,187,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,-27,-36,-15,-16,-55,-49,-50,-51,-52,-53,-61,-11,-12,-34,-30,-32,-35,-102,-102,-54,-65,-102,-33,-29,-31,-14,-19,-18,-56,-58,-60,-66,-63,-37,-17,-102,-59,-57,-102,-44,-62,]),'IF':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,18,-27,-36,-15,-16,18,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,18,18,-54,-102,-65,18,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,18,-59,-102,-45,-57,18,-48,-61,-47,18,-44,-62,]),'SWITCH':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,19,-27,-36,-15,-16,19,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,19,19,-54,-102,-65,19,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,19,-59,-102,-45,-57,19,-48,-61,-47,19,-44,-62,]),'CASE':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,20,-27,-36,-15,-16,20,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,20,20,-54,-102,-65,20,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,20,-59,-102,-45,-57,20,-48,-61,-47,20,-44,-62,]),'DEFAULT':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,21,-27,-36,-15,-16,21,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,21,21,-54,-102,-65,21,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,21,-59,-102,-45,-57,21,-48,-61,-47,21,-44,-62,]),'FOR':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,22,-27,-36,-15,-16,22,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,22,22,-54,-102,-65,22,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,22,-59,-102,-45,-57,22,-48,-61,-47,22,-44,-62,]),'WHILE':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,23,-27,-36,-15,-16,23,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,23,23,-54,-102,-65,23,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,23,-59,-102,-45,-57,23,-48,-61,-47,23,-44,-62,]),'ECHO':([2,3,4,5,6,7,8,9,10,11,17,25,27,37,42,48,51,52,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,134,136,138,141,153,155,156,157,158,160,161,164,168,173,174,175,178,180,181,183,184,185,186,187,],[-102,-102,-3,-4,-5,-6,-7,26,-9,-10,-13,-2,-28,-102,-27,-36,-15,-16,-102,-55,-49,-50,-51,-52,-53,-102,26,-11,-12,-34,-30,-32,-35,-102,-102,-54,26,-65,-102,-33,-29,-31,-14,-19,-18,-56,-58,-60,-102,-46,-66,-63,-37,-17,-102,-59,26,-45,-57,-102,-48,26,-47,-102,-44,-62,]),'CLOSE_TAG':([2,3,4,5,6,7,8,9,10,11,17,25,27,42,48,51,52,69,70,71,72,73,74,77,81,82,83,84,85,86,100,119,122,124,127,128,129,130,134,136,138,141,153,155,158,160,161,164,168,173,178,185,186,187,],[-102,24,-3,-4,-5,-6,-7,-8,-9,-10,-13,-2,-28,-27,-36,-15,-16,-55,-49,-50,-51,-52,-53,-61,-11,-12,-34,-30,-32,-35,-102,-102,-54,-65,-102,-33,-29,-31,-14,-19,-18,-56,-58,-60,-66,-63,-37,-17,-102,-59,-57,-102,-44,-62,]),'SEMICOLON':([12,17,27,29,32,37,40,41,42,43,44,45,46,47,48,56,57,58,59,60,61,62,63,64,67,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,92,100,114,115,119,121,122,123,124,125,127,128,129,130,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,168,169,170,171,173,174,175,178,180,181,183,184,185,186,187,],[27,-13,-28,48,51,69,81,82,-27,83,84,85,-100,-101,-36,-91,-68,-70,-73,-81,-87,-92,-93,-94,69,-55,-49,-50,-51,-52,-53,122,-102,-61,124,126,-11,-12,-34,-30,-32,-35,134,69,-82,-83,69,155,-54,-102,-65,158,69,-33,-29,-31,-90,-56,-67,-72,-91,-80,-86,-58,173,-60,-102,-46,-66,176,-63,69,-69,-71,-95,-59,-102,-45,-57,69,-48,-61,-47,69,-44,-62,]),'EQUAL':([12,56,58,170,],[28,101,-70,-71,]),'FUNCTION_NAME':([14,16,],[30,33,]),'LPAREN':([15,17,18,19,22,23,27,30,34,37,39,42,48,54,58,67,69,70,71,72,73,74,76,77,78,81,82,83,84,85,86,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,122,123,124,126,127,128,129,130,141,153,155,156,157,158,160,168,172,173,174,175,176,178,180,181,183,184,185,186,187,],[31,-13,34,35,38,39,-28,49,54,54,54,-27,-36,54,103,54,-55,-49,-50,-51,-52,-53,-102,-61,54,-11,-12,-34,-30,-32,-35,54,54,54,54,54,54,-74,-75,-76,-77,-78,-79,-84,-85,54,-88,-89,54,-54,-102,-65,54,54,-33,-29,-31,-56,-58,-60,-102,-46,-66,-63,54,54,-59,-102,-45,54,-57,54,-48,-61,-47,54,-44,-62,]),'STRING':([15,26,31,],[32,40,50,]),'BREAK':([17,37,67,68,69,70,71,72,73,74,77,81,82,100,119,120,122,124,127,141,153,155,158,160,168,173,178,185,186,187,],[-13,-102,-102,121,-55,-49,-50,-51,-52,-53,-61,-11,-12,-102,-102,154,-54,-65,-102,-56,-58,-60,-66,-63,-102,-59,-57,-102,-44,-62,]),'LBLOCK':([17,27,33,37,42,48,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,131,141,153,155,156,157,158,160,168,173,174,175,178,180,181,183,184,185,186,187,],[-13,-28,53,76,-27,-36,76,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,76,76,-54,-102,-65,76,-33,-29,-31,76,-56,-58,-60,-102,-46,-66,-63,76,-59,-102,-45,-57,76,-48,-61,-47,76,-44,-62,]),'RETURN':([17,27,37,42,48,67,69,70,71,72,73,74,76,77,81,82,83,84,85,86,100,119,122,123,124,127,128,129,130,141,153,155,156,157,158,160,168,173,174,175,178,180,181,183,184,185,186,187,],[-13,-28,78,-27,-36,78,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,78,78,-54,-102,-65,78,-33,-29,-31,-56,-58,-60,-102,-46,-66,-63,78,-59,-102,-45,-57,78,-48,-61,-47,78,-44,-62,]),'NUMBER':([17,20,27,28,34,37,39,42,48,54,67,69,70,71,72,73,74,76,77,78,81,82,83,84,85,86,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,122,123,124,126,127,128,129,130,141,153,155,156,157,158,160,168,172,173,174,175,176,178,180,181,183,184,185,186,187,],[-13,36,-28,44,63,63,63,-27,-36,63,63,-55,-49,-50,-51,-52,-53,-102,-61,63,-11,-12,-34,-30,-32,-35,63,63,63,63,63,63,-74,-75,-76,-77,-78,-79,-84,-85,63,-88,-89,63,-54,-102,-65,63,63,-33,-29,-31,-56,-58,-60,-102,-46,-66,-63,63,63,-59,-102,-45,63,-57,63,-48,-61,-47,63,-44,-62,]),'TRUE':([17,27,28,34,37,39,42,48,54,67,69,70,71,72,73,74,76,77,78,81,82,83,84,85,86,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,122,123,124,126,127,128,129,130,141,153,155,156,157,158,160,168,172,173,174,175,176,178,180,181,183,184,185,186,187,],[-13,-28,46,46,46,46,-27,-36,46,46,-55,-49,-50,-51,-52,-53,-102,-61,46,-11,-12,-34,-30,-32,-35,46,46,46,46,46,46,-74,-75,-76,-77,-78,-79,-84,-85,46,-88,-89,46,-54,-102,-65,46,46,-33,-29,-31,-56,-58,-60,-102,-46,-66,-63,46,46,-59,-102,-45,46,-57,46,-48,-61,-47,46,-44,-62,]),'FALSE':([17,27,28,34,37,39,42,48,54,67,69,70,71,72,73,74,76,77,78,81,82,83,84,85,86,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,122,123,124,126,127,128,129,130,141,153,155,156,157,158,160,168,172,173,174,175,176,178,180,181,183,184,185,186,187,],[-13,-28,47,47,47,47,-27,-36,47,47,-55,-49,-50,-51,-52,-53,-102,-61,47,-11,-12,-34,-30,-32,-35,47,47,47,47,47,47,-74,-75,-76,-77,-78,-79,-84,-85,47,-88,-89,47,-54,-102,-65,47,47,-33,-29,-31,-56,-58,-60,-102,-46,-66,-63,47,47,-59,-102,-45,47,-57,47,-48,-61,-47,47,-44,-62,]),'RBLOCK':([17,27,42,48,53,69,70,71,72,73,74,76,77,81,82,83,84,85,86,93,94,100,119,122,123,124,127,128,129,130,135,139,141,153,155,156,157,158,160,161,166,167,168,173,174,175,177,178,180,181,183,184,185,186,187,],[-13,-28,-27,-36,-102,-55,-49,-50,-51,-52,-53,-102,-61,-11,-12,-34,-30,-32,-35,136,138,-102,-102,-54,-102,-65,-102,-33,-29,-31,164,-21,-56,-58,-60,-102,-46,-66,-63,-37,-20,-23,-102,-59,-102,-45,-22,-57,-102,-48,186,-47,-102,-44,-62,]),'ELSE':([17,69,70,71,72,73,74,77,81,82,100,119,122,124,127,141,153,155,158,160,168,173,178,185,186,187,],[-13,-55,-49,-50,-51,-52,-53,-61,-11,-12,-102,-102,-54,-65,-102,168,-58,-60,-66,-63,-102,-59,-57,-102,-44,-62,]),'COLON':([21,36,],[37,67,]),'PRIVATE':([27,42,48,53,83,84,85,86,93,128,129,130,135,139,161,166,167,177,186,],[-28,-27,-36,96,-34,-30,-32,-35,96,-33,-29,-31,96,-21,-37,-20,-23,-22,-44,]),'PUBLIC':([27,42,48,53,83,84,85,86,93,128,129,130,135,139,161,166,167,177,186,],[-28,-27,-36,97,-34,-30,-32,-35,97,-33,-29,-31,97,-21,-37,-20,-23,-22,-44,]),'PROTECTED':([27,42,48,53,83,84,85,86,93,128,129,130,135,139,161,166,167,177,186,],[-28,-27,-36,98,-34,-30,-32,-35,98,-33,-29,-31,98,-21,-37,-20,-23,-22,-44,]),'MINUSMINUS':([46,47,56,58,60,61,62,63,64,140,150,152,170,171,],[-100,-101,-91,-70,114,-87,-92,-93,-94,-90,-91,-86,-71,-95,]),'PLUSPLUS':([46,47,56,58,60,61,62,63,64,140,150,152,170,171,],[-100,-101,-91,-70,115,-87,-92,-93,-94,-90,-91,-86,-71,-95,]),'TIMES':([46,47,56,58,60,61,62,63,64,140,150,151,152,170,171,],[-100,-101,-91,-70,117,-87,-92,-93,-94,-90,-91,117,-86,-71,-95,]),'DIVIDE':([46,47,56,58,60,61,62,63,64,140,150,151,152,170,171,],[-100,-101,-91,-70,118,-87,-92,-93,-94,-90,-91,118,-86,-71,-95,]),'LESS':([46,47,56,58,59,60,61,62,63,64,114,115,140,150,151,152,170,171,],[-100,-101,-91,-70,106,-81,-87,-92,-93,-94,-82,-83,-90,-91,-80,-86,-71,-95,]),'LESSEQUAL':([46,47,56,58,59,60,61,62,63,64,114,115,140,150,151,152,170,171,],[-100,-101,-91,-70,107,-81,-87,-92,-93,-94,-82,-83,-90,-91,-80,-86,-71,-95,]),'GREATER':([46,47,56,58,59,60,61,62,63,64,114,115,140,150,151,152,170,171,],[-100,-101,-91,-70,108,-81,-87,-92,-93,-94,-82,-83,-90,-91,-80,-86,-71,-95,]),'GREATEREQUAL':([46,47,56,58,59,60,61,62,63,64,114,115,140,150,151,152,170,171,],[-100,-101,-91,-70,109,-81,-87,-92,-93,-94,-82,-83,-90,-91,-80,-86,-71,-95,]),'DEQUAL':([46,47,56,58,59,60,61,62,63,64,114,115,140,150,151,152,170,171,],[-100,-101,-91,-70,110,-81,-87,-92,-93,-94,-82,-83,-90,-91,-80,-86,-71,-95,]),'ISEQUAL':([46,47,56,58,59,60,61,62,63,64,114,115,140,150,151,152,170,171,],[-100,-101,-91,-70,111,-81,-87,-92,-93,-94,-82,-83,-90,-91,-80,-86,-71,-95,]),'PLUS':([46,47,56,58,59,60,61,62,63,64,114,115,140,149,150,151,152,170,171,182,],[-100,-101,-91,-70,112,-81,-87,-92,-93,-94,-82,-83,-90,112,-91,-80,-86,-71,-95,112,]),'MINUS':([46,47,56,58,59,60,61,62,63,64,114,115,140,149,150,151,152,170,171,182,],[-100,-101,-91,-70,113,-81,-87,-92,-93,-94,-82,-83,-90,113,-91,-80,-86,-71,-95,113,]),'RPAREN':([46,47,49,50,55,56,57,58,59,60,61,62,63,64,65,66,80,87,88,89,90,91,99,103,114,115,140,142,145,146,147,148,149,150,151,152,162,163,169,170,171,179,182,],[-100,-101,-102,92,100,-91,-68,-70,-73,-81,-87,-92,-93,-94,119,-70,127,131,-38,-39,-41,-42,140,-102,-82,-83,-90,-67,171,-96,-97,-99,-72,-91,-80,-86,-40,-43,-69,-71,-95,-98,185,]),'RBRACKET':([46,47,56,57,58,59,60,61,62,63,64,114,115,133,140,142,144,149,150,151,152,169,170,171,],[-100,-101,-91,-68,-70,-73,-81,-87,-92,-93,-94,-82,-83,163,-90,-67,170,-72,-91,-80,-86,-69,-71,-95,]),'COMMA':([46,47,56,57,58,59,60,61,62,63,64,88,90,91,114,115,140,142,146,148,149,150,151,152,162,163,169,170,171,179,],[-100,-101,-91,-68,-70,-73,-81,-87,-92,-93,-94,132,-41,-42,-82,-83,-90,-67,172,-99,-72,-91,-80,-86,-40,-43,-69,-71,-95,-98,]),'LBRACKET':([58,66,91,],[102,102,133,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([2,],[3,]),'declaration':([2,3,],[4,25,]),'var_declaration':([2,3,27,38,48,83,84,85,95,137,156,],[5,5,42,79,86,128,129,130,139,166,175,]),'fun_declaration':([2,3,137,165,],[6,6,167,177,]),'header_declaration':([2,3,],[7,7,]),'class_declaration':([2,3,],[8,8,]),'print_stmt':([2,3,37,67,76,100,119,127,156,168,180,185,],[9,9,77,77,123,77,77,77,174,77,183,77,]),'selection_stmt':([2,3,37,67,100,119,127,168,180,185,],[10,10,72,72,72,72,72,72,72,72,]),'iteration_stmt':([2,3,37,67,100,119,127,168,180,185,],[11,11,73,73,73,73,73,73,73,73,]),'empty':([2,3,37,49,53,67,76,100,103,119,123,127,156,168,174,180,185,],[17,17,17,89,94,17,17,17,147,17,157,17,17,17,181,17,17,]),'boolean':([28,34,37,39,54,67,78,100,101,102,103,104,105,116,119,126,127,168,172,176,180,185,],[45,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'class_stmt':([33,],[52,]),'expression':([34,37,39,54,67,78,100,101,102,103,119,126,127,168,172,180,185,],[55,75,80,99,75,125,75,142,144,148,75,159,75,75,179,75,75,]),'var':([34,35,37,39,54,67,78,100,101,102,103,104,105,116,119,126,127,168,172,176,180,185,],[56,65,56,56,56,56,56,56,56,56,56,150,150,150,56,56,56,56,56,150,56,56,]),'simple_expression':([34,37,39,54,67,78,100,101,102,103,119,126,127,168,172,180,185,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'additive_expression':([34,37,39,54,67,78,100,101,102,103,104,119,126,127,168,172,176,180,185,],[59,59,59,59,59,59,59,59,59,59,149,59,59,59,59,59,182,59,59,]),'term':([34,37,39,54,67,78,100,101,102,103,104,105,119,126,127,168,172,176,180,185,],[60,60,60,60,60,60,60,60,60,60,60,151,60,60,60,60,60,60,60,60,]),'factor':([34,37,39,54,67,78,100,101,102,103,104,105,116,119,126,127,168,172,176,180,185,],[61,61,61,61,61,61,61,61,61,61,61,61,152,61,61,61,61,61,61,61,61,]),'call':([34,37,39,54,67,78,100,101,102,103,104,105,116,119,126,127,168,172,176,180,185,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'statement':([37,67,100,119,127,168,180,185,],[68,120,141,153,160,178,184,187,]),'expression_stmt':([37,67,100,119,127,168,180,185,],[70,70,70,70,70,70,70,70,]),'compount_stmt':([37,67,100,119,127,131,168,180,185,],[71,71,71,71,71,161,71,71,71,]),'return_stmt':([37,67,100,119,127,168,180,185,],[74,74,74,74,74,74,74,74,]),'params':([49,],[87,]),'param_list':([49,],[88,]),'param':([49,132,],[90,162,]),'attributes':([53,],[93,]),'scope':([53,93,135,],[95,137,165,]),'relop':([59,],[104,]),'addop':([59,149,182,],[105,105,105,]),'mulop':([60,151,],[116,116,]),'methods':([93,],[135,]),'args':([103,],[145,]),'args_list':([103,],[146,]),'local_declarations':([123,],[156,]),'statement_list':([174,],[180,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> OPEN_TAG declaration_list CLOSE_TAG','program',3,'p_program','miniparser_php.py',18),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list_1','miniparser_php.py',22),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list_2','miniparser_php.py',26),
  ('declaration -> var_declaration','declaration',1,'p_declaration','miniparser_php.py',30),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','miniparser_php.py',31),
  ('declaration -> header_declaration','declaration',1,'p_declaration','miniparser_php.py',32),
  ('declaration -> class_declaration','declaration',1,'p_declaration','miniparser_php.py',33),
  ('declaration -> print_stmt','declaration',1,'p_declaration','miniparser_php.py',34),
  ('declaration -> selection_stmt','declaration',1,'p_declaration','miniparser_php.py',35),
  ('declaration -> iteration_stmt','declaration',1,'p_declaration','miniparser_php.py',36),
  ('print_stmt -> print_stmt ECHO STRING SEMICOLON','print_stmt',4,'p_print_stmt','miniparser_php.py',41),
  ('print_stmt -> print_stmt ECHO ID SEMICOLON','print_stmt',4,'p_print_stmt','miniparser_php.py',42),
  ('print_stmt -> empty','print_stmt',1,'p_print_stmt','miniparser_php.py',43),
  ('header_declaration -> REQUIRE LPAREN STRING RPAREN SEMICOLON','header_declaration',5,'p_header_declaration','miniparser_php.py',48),
  ('header_declaration -> REQUIRE STRING SEMICOLON','header_declaration',3,'p_header_declaration','miniparser_php.py',49),
  ('class_declaration -> CLASS FUNCTION_NAME class_stmt','class_declaration',3,'p_class_declaration','miniparser_php.py',54),
  ('class_stmt -> LBLOCK attributes methods RBLOCK','class_stmt',4,'p_class_stmt1','miniparser_php.py',58),
  ('class_stmt -> LBLOCK empty RBLOCK','class_stmt',3,'p_class_stmt2','miniparser_php.py',62),
  ('class_stmt -> LBLOCK attributes RBLOCK','class_stmt',3,'p_class_stmt3','miniparser_php.py',66),
  ('attributes -> attributes scope var_declaration','attributes',3,'p_attributes1','miniparser_php.py',70),
  ('attributes -> scope var_declaration','attributes',2,'p_attributes2','miniparser_php.py',74),
  ('methods -> methods scope fun_declaration','methods',3,'p_methods1','miniparser_php.py',78),
  ('methods -> scope fun_declaration','methods',2,'p_methods2','miniparser_php.py',82),
  ('scope -> PRIVATE','scope',1,'p_scope','miniparser_php.py',86),
  ('scope -> PUBLIC','scope',1,'p_scope','miniparser_php.py',87),
  ('scope -> PROTECTED','scope',1,'p_scope','miniparser_php.py',88),
  ('var_declaration -> ID SEMICOLON var_declaration','var_declaration',3,'p_var_declaration','miniparser_php.py',93),
  ('var_declaration -> ID SEMICOLON','var_declaration',2,'p_var_declaration','miniparser_php.py',94),
  ('var_declaration -> ID EQUAL NUMBER SEMICOLON var_declaration','var_declaration',5,'p_var_declaration','miniparser_php.py',95),
  ('var_declaration -> ID EQUAL NUMBER SEMICOLON','var_declaration',4,'p_var_declaration','miniparser_php.py',96),
  ('var_declaration -> ID EQUAL boolean SEMICOLON var_declaration','var_declaration',5,'p_var_declaration','miniparser_php.py',97),
  ('var_declaration -> ID EQUAL boolean SEMICOLON','var_declaration',4,'p_var_declaration','miniparser_php.py',98),
  ('var_declaration -> ID EQUAL ID SEMICOLON var_declaration','var_declaration',5,'p_var_declaration','miniparser_php.py',99),
  ('var_declaration -> ID EQUAL ID SEMICOLON','var_declaration',4,'p_var_declaration','miniparser_php.py',100),
  ('var_declaration -> AMPERSANT ID SEMICOLON var_declaration','var_declaration',4,'p_var_declaration','miniparser_php.py',101),
  ('var_declaration -> AMPERSANT ID SEMICOLON','var_declaration',3,'p_var_declaration','miniparser_php.py',102),
  ('fun_declaration -> FUNCTION FUNCTION_NAME LPAREN params RPAREN compount_stmt','fun_declaration',6,'p_fun_declaration','miniparser_php.py',107),
  ('params -> param_list','params',1,'p_params_1','miniparser_php.py',111),
  ('params -> empty','params',1,'p_params_2','miniparser_php.py',115),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list_1','miniparser_php.py',119),
  ('param_list -> param','param_list',1,'p_param_list_2','miniparser_php.py',123),
  ('param -> ID','param',1,'p_param_1','miniparser_php.py',127),
  ('param -> ID LBRACKET RBRACKET','param',3,'p_param_2','miniparser_php.py',131),
  ('compount_stmt -> LBLOCK print_stmt local_declarations print_stmt statement_list print_stmt RBLOCK','compount_stmt',7,'p_compount_stmt','miniparser_php.py',135),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations_1','miniparser_php.py',139),
  ('local_declarations -> empty','local_declarations',1,'p_local_declarations_2','miniparser_php.py',143),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list_1','miniparser_php.py',147),
  ('statement_list -> empty','statement_list',1,'p_statement_list_2','miniparser_php.py',151),
  ('statement -> expression_stmt','statement',1,'p_statement','miniparser_php.py',155),
  ('statement -> compount_stmt','statement',1,'p_statement','miniparser_php.py',156),
  ('statement -> selection_stmt','statement',1,'p_statement','miniparser_php.py',157),
  ('statement -> iteration_stmt','statement',1,'p_statement','miniparser_php.py',158),
  ('statement -> return_stmt','statement',1,'p_statement','miniparser_php.py',159),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt_1','miniparser_php.py',164),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt_2','miniparser_php.py',168),
  ('selection_stmt -> IF LPAREN expression RPAREN statement','selection_stmt',5,'p_selection_stmt','miniparser_php.py',172),
  ('selection_stmt -> IF LPAREN expression RPAREN statement ELSE statement','selection_stmt',7,'p_selection_stmt','miniparser_php.py',173),
  ('selection_stmt -> SWITCH LPAREN var RPAREN statement','selection_stmt',5,'p_selection_stmt','miniparser_php.py',174),
  ('selection_stmt -> CASE NUMBER COLON statement BREAK SEMICOLON','selection_stmt',6,'p_selection_stmt','miniparser_php.py',175),
  ('selection_stmt -> DEFAULT COLON statement BREAK SEMICOLON','selection_stmt',5,'p_selection_stmt','miniparser_php.py',176),
  ('selection_stmt -> print_stmt','selection_stmt',1,'p_selection_stmt','miniparser_php.py',177),
  ('iteration_stmt -> FOR LPAREN var_declaration SEMICOLON expression SEMICOLON additive_expression RPAREN statement','iteration_stmt',9,'p_iteration_stmt','miniparser_php.py',182),
  ('iteration_stmt -> WHILE LPAREN expression RPAREN statement','iteration_stmt',5,'p_iteration_stmt','miniparser_php.py',183),
  ('iteration_stmt -> print_stmt','iteration_stmt',1,'p_iteration_stmt_3','miniparser_php.py',188),
  ('return_stmt -> RETURN SEMICOLON','return_stmt',2,'p_return_stmt_1','miniparser_php.py',192),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt_2','miniparser_php.py',196),
  ('expression -> var EQUAL expression','expression',3,'p_expression_1','miniparser_php.py',200),
  ('expression -> simple_expression','expression',1,'p_expression_2','miniparser_php.py',204),
  ('expression -> var EQUAL AMPERSANT ID','expression',4,'p_expression_3','miniparser_php.py',208),
  ('var -> ID','var',1,'p_var_1','miniparser_php.py',212),
  ('var -> ID LBRACKET expression RBRACKET','var',4,'p_var_2','miniparser_php.py',216),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression_1','miniparser_php.py',220),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression_2','miniparser_php.py',224),
  ('relop -> LESS','relop',1,'p_relop','miniparser_php.py',228),
  ('relop -> LESSEQUAL','relop',1,'p_relop','miniparser_php.py',229),
  ('relop -> GREATER','relop',1,'p_relop','miniparser_php.py',230),
  ('relop -> GREATEREQUAL','relop',1,'p_relop','miniparser_php.py',231),
  ('relop -> DEQUAL','relop',1,'p_relop','miniparser_php.py',232),
  ('relop -> ISEQUAL','relop',1,'p_relop','miniparser_php.py',233),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression_1','miniparser_php.py',238),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression_2','miniparser_php.py',242),
  ('additive_expression -> term MINUSMINUS','additive_expression',2,'p_additive_expression_3','miniparser_php.py',246),
  ('additive_expression -> term PLUSPLUS','additive_expression',2,'p_additive_expression_4','miniparser_php.py',250),
  ('addop -> PLUS','addop',1,'p_addop','miniparser_php.py',254),
  ('addop -> MINUS','addop',1,'p_addop','miniparser_php.py',255),
  ('term -> term mulop factor','term',3,'p_term_1','miniparser_php.py',260),
  ('term -> factor','term',1,'p_term_2','miniparser_php.py',264),
  ('mulop -> TIMES','mulop',1,'p_mulop','miniparser_php.py',268),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','miniparser_php.py',269),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_1','miniparser_php.py',274),
  ('factor -> var','factor',1,'p_factor_2','miniparser_php.py',278),
  ('factor -> call','factor',1,'p_factor_3','miniparser_php.py',282),
  ('factor -> NUMBER','factor',1,'p_factor_4','miniparser_php.py',286),
  ('factor -> boolean','factor',1,'p_factor_5','miniparser_php.py',290),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','miniparser_php.py',294),
  ('args -> args_list','args',1,'p_args','miniparser_php.py',298),
  ('args -> empty','args',1,'p_args','miniparser_php.py',299),
  ('args_list -> args_list COMMA expression','args_list',3,'p_args_list_1','miniparser_php.py',304),
  ('args_list -> expression','args_list',1,'p_args_list_2','miniparser_php.py',308),
  ('boolean -> TRUE','boolean',1,'p_boolean','miniparser_php.py',312),
  ('boolean -> FALSE','boolean',1,'p_boolean','miniparser_php.py',313),
  ('empty -> <empty>','empty',0,'p_empty','miniparser_php.py',318),
]
