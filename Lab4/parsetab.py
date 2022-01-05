
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programnonassocIFXnonassocELSEnonassoc<>GELEEQNEQrightMULASSIGNDIVASSIGNSUBASSIGNADDASSIGNleft+-leftDOTADDDOTSUBleft*/leftDOTMULDOTDIVrightUMINUSleft\'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GE ID IF INT LE MULASSIGN NEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROS empty :program : instructions_optinstructions_opt : instructions instructions_opt : emptyinstructions : instruction\n                    | instructions instructioninstruction : assignment \';\'\n                | statement \';\'\n                | \'{\' instructions \'}\'\n                instruction : IF \'(\' condition \')\' instruction %prec IFX instruction : IF \'(\' condition \')\' instruction ELSE instruction instruction : WHILE \'(\' condition \')\' instruction instruction : FOR var \'=\' range instruction range : expression \':\' expression condition : expression EQ expression\n                 | expression NEQ expression\n                 | expression LE expression\n                 | expression GE expression\n                 | expression \'<\' expression\n                 | expression \'>\' expression assignment_op : MULASSIGN\n                   | DIVASSIGN\n                   | SUBASSIGN\n                   | ADDASSIGN\n                   | \'=\' assignment : var assignment_op expression\n                | matrix_element assignment_op expression\n                | vector_element assignment_op expression matrix_function : EYE \'(\' INT \')\'\n                       | ONES \'(\' INT \')\'\n                       | ZEROS \'(\' INT \')\' matrix : \'[\' vectors \']\' vectors : vectors \',\' vector\n               | vector vector : \'[\' variables \']\' variables : variables \',\' variable\n                 | variable variable : number\n                 | var\n                 | element  element : vector_element\n               | matrix_element vector_element : var "[" INT "]"  matrix_element : var "[" INT "," INT "]" number : INT\n             | FLOAT string : STRING expression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expression\n                  | expression DOTADD expression\n                  | expression DOTSUB expression\n                  | expression DOTMUL expression\n                  | expression DOTDIV expressionexpression : num_expression\n            | matrix\n            | matrix_function\n            | vector\n            | uminus\n            | transposition\n            | matrix_element\n            | vector_element num_expression : number\n                      | var  var : ID uminus : \'-\' expression %prec UMINUS transposition : expression "\'" statement : BREAKstatement : CONTINUEstatement : RETURN expression statement : PRINT print_vals print_vals : print_vals \',\' print_val\n                  | print_val print_val : string\n                 | expression'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,20,21,22,59,121,128,129,141,],[-1,0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-12,-13,-11,]),'{':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[8,8,-5,8,-66,-6,-7,-8,8,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,8,8,8,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,8,-14,-44,-11,]),'IF':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[9,9,-5,9,-66,-6,-7,-8,9,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,9,9,9,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,9,-14,-44,-11,]),'WHILE':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[10,10,-5,10,-66,-6,-7,-8,10,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,10,10,10,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,10,-14,-44,-11,]),'FOR':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[11,11,-5,11,-66,-6,-7,-8,11,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,11,11,11,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,11,-14,-44,-11,]),'BREAK':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[15,15,-5,15,-66,-6,-7,-8,15,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,15,15,15,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,15,-14,-44,-11,]),'CONTINUE':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[16,16,-5,16,-66,-6,-7,-8,16,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,16,16,16,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,16,-14,-44,-11,]),'RETURN':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[17,17,-5,17,-66,-6,-7,-8,17,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,17,17,17,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,17,-14,-44,-11,]),'PRINT':([0,3,5,8,19,20,21,22,23,38,39,40,41,42,43,44,45,46,47,50,53,59,76,77,92,99,100,103,104,105,106,107,108,109,110,111,112,114,121,128,129,135,136,137,138,139,140,141,],[18,18,-5,18,-66,-6,-7,-8,18,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-9,-68,-67,18,18,18,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-10,-12,-13,-29,-30,-31,18,-14,-44,-11,]),'ID':([0,3,5,8,11,17,18,19,20,21,22,23,24,25,27,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,50,53,59,63,68,69,70,71,72,73,74,75,76,77,78,91,92,93,94,95,96,97,98,99,100,103,104,105,106,107,108,109,110,111,112,114,115,121,128,129,130,135,136,137,138,139,140,141,],[19,19,-5,19,19,19,19,-66,-6,-7,-8,19,19,19,19,-21,-22,-23,-24,-25,19,19,19,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,19,-45,-46,-9,19,19,19,19,19,19,19,19,19,-68,-67,19,19,19,19,19,19,19,19,19,19,19,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,19,-10,-12,-13,19,-29,-30,-31,19,-14,-44,-11,]),'}':([5,20,21,22,23,59,121,128,129,141,],[-5,-6,-7,-8,59,-9,-10,-12,-13,-11,]),';':([6,7,15,16,19,36,38,39,40,41,42,43,44,45,46,47,50,53,54,55,56,57,58,64,66,67,76,77,103,104,105,106,107,108,109,110,111,112,114,120,135,136,137,140,],[21,22,-69,-70,-66,-71,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-72,-74,-75,-76,-47,-26,-27,-28,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-73,-29,-30,-31,-44,]),'(':([9,10,49,51,52,],[24,25,88,89,90,]),'[':([12,17,18,19,24,25,27,29,30,31,32,33,34,35,37,47,48,63,68,69,70,71,72,73,74,75,84,91,93,94,95,96,97,98,113,130,],[28,48,48,-66,48,48,48,-21,-22,-23,-24,-25,48,48,48,28,78,48,48,48,48,48,48,48,48,48,116,48,48,48,48,48,48,48,78,48,]),'MULASSIGN':([12,13,14,19,103,140,],[29,29,29,-66,-43,-44,]),'DIVASSIGN':([12,13,14,19,103,140,],[30,30,30,-66,-43,-44,]),'SUBASSIGN':([12,13,14,19,103,140,],[31,31,31,-66,-43,-44,]),'ADDASSIGN':([12,13,14,19,103,140,],[32,32,32,-66,-43,-44,]),'=':([12,13,14,19,26,103,140,],[33,33,33,-66,63,-43,-44,]),'EYE':([17,18,24,25,27,29,30,31,32,33,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[49,49,49,49,49,-21,-22,-23,-24,-25,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'ONES':([17,18,24,25,27,29,30,31,32,33,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[51,51,51,51,51,-21,-22,-23,-24,-25,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'ZEROS':([17,18,24,25,27,29,30,31,32,33,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[52,52,52,52,52,-21,-22,-23,-24,-25,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'-':([17,18,19,24,25,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,57,61,63,64,66,67,68,69,70,71,72,73,74,75,76,77,91,93,94,95,96,97,98,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,130,135,136,137,139,140,],[37,37,-66,37,37,37,-21,-22,-23,-24,-25,37,37,69,37,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,69,69,37,69,69,69,37,37,37,37,37,37,37,37,-68,-67,37,37,37,37,37,37,37,69,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,69,69,69,69,69,69,37,-29,-30,-31,69,-44,]),'INT':([17,18,24,25,27,28,29,30,31,32,33,34,35,37,48,63,68,69,70,71,72,73,74,75,78,88,89,90,91,93,94,95,96,97,98,102,115,116,130,],[50,50,50,50,50,65,-21,-22,-23,-24,-25,50,50,50,50,50,50,50,50,50,50,50,50,50,50,117,118,119,50,50,50,50,50,50,50,131,50,134,50,]),'FLOAT':([17,18,24,25,27,29,30,31,32,33,34,35,37,48,63,68,69,70,71,72,73,74,75,78,91,93,94,95,96,97,98,115,130,],[53,53,53,53,53,-21,-22,-23,-24,-25,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'STRING':([18,91,],[58,58,]),'+':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,68,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,68,68,68,68,68,-68,-67,68,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,68,68,68,68,68,68,-29,-30,-31,68,-44,]),'*':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,70,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,70,70,70,70,70,-68,-67,70,-43,70,70,-50,-51,70,70,-54,-55,-32,-35,70,70,70,70,70,70,-29,-30,-31,70,-44,]),'/':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,71,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,71,71,71,71,71,-68,-67,71,-43,71,71,-50,-51,71,71,-54,-55,-32,-35,71,71,71,71,71,71,-29,-30,-31,71,-44,]),'DOTADD':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,72,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,72,72,72,72,72,-68,-67,72,-43,72,72,-50,-51,-52,-53,-54,-55,-32,-35,72,72,72,72,72,72,-29,-30,-31,72,-44,]),'DOTSUB':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,73,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,73,73,73,73,73,-68,-67,73,-43,73,73,-50,-51,-52,-53,-54,-55,-32,-35,73,73,73,73,73,73,-29,-30,-31,73,-44,]),'DOTMUL':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,74,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,74,74,74,74,74,-68,-67,74,-43,74,74,74,74,74,74,-54,-55,-32,-35,74,74,74,74,74,74,-29,-30,-31,74,-44,]),'DOTDIV':([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,75,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,75,75,75,75,75,-68,-67,75,-43,75,75,75,75,75,75,-54,-55,-32,-35,75,75,75,75,75,75,-29,-30,-31,75,-44,]),"'":([19,36,38,39,40,41,42,43,44,45,46,47,50,53,57,61,64,66,67,76,77,101,103,104,105,106,107,108,109,110,111,112,114,122,123,124,125,126,127,135,136,137,139,140,],[-66,76,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,76,76,76,76,76,-68,76,76,-43,76,76,76,76,76,76,76,76,-32,-35,76,76,76,76,76,76,-29,-30,-31,76,-44,]),',':([19,38,39,40,41,42,43,44,45,46,47,50,53,54,55,56,57,58,65,76,77,79,80,81,82,83,84,85,86,87,103,104,105,106,107,108,109,110,111,112,114,120,132,133,134,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,91,-74,-75,-76,-47,102,-68,-67,113,115,-34,-37,-38,-39,-40,-41,-42,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-73,-33,-36,102,-29,-30,-31,-44,]),'EQ':([19,38,39,40,41,42,43,44,45,46,47,50,53,61,76,77,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,93,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),'NEQ':([19,38,39,40,41,42,43,44,45,46,47,50,53,61,76,77,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,94,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),'LE':([19,38,39,40,41,42,43,44,45,46,47,50,53,61,76,77,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,95,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),'GE':([19,38,39,40,41,42,43,44,45,46,47,50,53,61,76,77,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,96,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),'<':([19,38,39,40,41,42,43,44,45,46,47,50,53,61,76,77,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,97,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),'>':([19,38,39,40,41,42,43,44,45,46,47,50,53,61,76,77,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,98,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),':':([19,38,39,40,41,42,43,44,45,46,47,50,53,76,77,101,103,104,105,106,107,108,109,110,111,112,114,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,-68,-67,130,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,-29,-30,-31,-44,]),')':([19,38,39,40,41,42,43,44,45,46,47,50,53,60,62,76,77,103,104,105,106,107,108,109,110,111,112,114,117,118,119,122,123,124,125,126,127,135,136,137,140,],[-66,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-45,-46,92,99,-68,-67,-43,-48,-49,-50,-51,-52,-53,-54,-55,-32,-35,135,136,137,-15,-16,-17,-18,-19,-20,-29,-30,-31,-44,]),']':([19,50,53,65,79,80,81,82,83,84,85,86,87,103,114,131,132,133,134,140,],[-66,-45,-46,103,112,114,-34,-37,-38,-39,-40,-41,-42,-43,-35,140,-33,-36,103,-44,]),'ELSE':([21,22,59,121,128,129,141,],[-7,-8,-9,138,-12,-13,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,8,],[3,23,]),'empty':([0,],[4,]),'instruction':([0,3,8,23,92,99,100,138,],[5,20,5,20,121,128,129,141,]),'assignment':([0,3,8,23,92,99,100,138,],[6,6,6,6,6,6,6,6,]),'statement':([0,3,8,23,92,99,100,138,],[7,7,7,7,7,7,7,7,]),'var':([0,3,8,11,17,18,23,24,25,27,34,35,37,48,63,68,69,70,71,72,73,74,75,78,91,92,93,94,95,96,97,98,99,100,115,130,138,],[12,12,12,26,47,47,12,47,47,47,47,47,47,84,47,47,47,47,47,47,47,47,47,84,47,12,47,47,47,47,47,47,12,12,84,47,12,]),'matrix_element':([0,3,8,17,18,23,24,25,27,34,35,37,48,63,68,69,70,71,72,73,74,75,78,91,92,93,94,95,96,97,98,99,100,115,130,138,],[13,13,13,44,44,13,44,44,44,44,44,44,87,44,44,44,44,44,44,44,44,44,87,44,13,44,44,44,44,44,44,13,13,87,44,13,]),'vector_element':([0,3,8,17,18,23,24,25,27,34,35,37,48,63,68,69,70,71,72,73,74,75,78,91,92,93,94,95,96,97,98,99,100,115,130,138,],[14,14,14,45,45,14,45,45,45,45,45,45,86,45,45,45,45,45,45,45,45,45,86,45,14,45,45,45,45,45,45,14,14,86,45,14,]),'assignment_op':([12,13,14,],[27,34,35,]),'expression':([17,18,24,25,27,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[36,57,61,61,64,66,67,77,101,104,105,106,107,108,109,110,111,57,122,123,124,125,126,127,139,]),'num_expression':([17,18,24,25,27,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'matrix':([17,18,24,25,27,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'matrix_function':([17,18,24,25,27,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'vector':([17,18,24,25,27,34,35,37,48,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,113,130,],[41,41,41,41,41,41,41,41,81,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,132,41,]),'uminus':([17,18,24,25,27,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'transposition':([17,18,24,25,27,34,35,37,63,68,69,70,71,72,73,74,75,91,93,94,95,96,97,98,130,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'number':([17,18,24,25,27,34,35,37,48,63,68,69,70,71,72,73,74,75,78,91,93,94,95,96,97,98,115,130,],[46,46,46,46,46,46,46,46,83,46,46,46,46,46,46,46,46,46,83,46,46,46,46,46,46,46,83,46,]),'print_vals':([18,],[54,]),'print_val':([18,91,],[55,120,]),'string':([18,91,],[56,56,]),'condition':([24,25,],[60,62,]),'vectors':([48,],[79,]),'variables':([48,78,],[80,80,]),'variable':([48,78,115,],[82,82,133,]),'element':([48,78,115,],[85,85,85,]),'range':([63,],[100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','Mparser.py',30),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',35),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',40),
  ('instructions_opt -> empty','instructions_opt',1,'p_instructions_opt_2','Mparser.py',45),
  ('instructions -> instruction','instructions',1,'p_instructions','Mparser.py',50),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',51),
  ('instruction -> assignment ;','instruction',2,'p_instruction','Mparser.py',59),
  ('instruction -> statement ;','instruction',2,'p_instruction','Mparser.py',60),
  ('instruction -> { instructions }','instruction',3,'p_instruction','Mparser.py',61),
  ('instruction -> IF ( condition ) instruction','instruction',5,'p_instruction_if','Mparser.py',70),
  ('instruction -> IF ( condition ) instruction ELSE instruction','instruction',7,'p_instruction_if_else','Mparser.py',75),
  ('instruction -> WHILE ( condition ) instruction','instruction',5,'p_instruction_while','Mparser.py',79),
  ('instruction -> FOR var = range instruction','instruction',5,'p_instruction_for','Mparser.py',83),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',87),
  ('condition -> expression EQ expression','condition',3,'p_condition','Mparser.py',91),
  ('condition -> expression NEQ expression','condition',3,'p_condition','Mparser.py',92),
  ('condition -> expression LE expression','condition',3,'p_condition','Mparser.py',93),
  ('condition -> expression GE expression','condition',3,'p_condition','Mparser.py',94),
  ('condition -> expression < expression','condition',3,'p_condition','Mparser.py',95),
  ('condition -> expression > expression','condition',3,'p_condition','Mparser.py',96),
  ('assignment_op -> MULASSIGN','assignment_op',1,'p_assignment_op','Mparser.py',100),
  ('assignment_op -> DIVASSIGN','assignment_op',1,'p_assignment_op','Mparser.py',101),
  ('assignment_op -> SUBASSIGN','assignment_op',1,'p_assignment_op','Mparser.py',102),
  ('assignment_op -> ADDASSIGN','assignment_op',1,'p_assignment_op','Mparser.py',103),
  ('assignment_op -> =','assignment_op',1,'p_assignment_op','Mparser.py',104),
  ('assignment -> var assignment_op expression','assignment',3,'p_assignment','Mparser.py',109),
  ('assignment -> matrix_element assignment_op expression','assignment',3,'p_assignment','Mparser.py',110),
  ('assignment -> vector_element assignment_op expression','assignment',3,'p_assignment','Mparser.py',111),
  ('matrix_function -> EYE ( INT )','matrix_function',4,'p_matrix_function','Mparser.py',116),
  ('matrix_function -> ONES ( INT )','matrix_function',4,'p_matrix_function','Mparser.py',117),
  ('matrix_function -> ZEROS ( INT )','matrix_function',4,'p_matrix_function','Mparser.py',118),
  ('matrix -> [ vectors ]','matrix',3,'p_matrix','Mparser.py',123),
  ('vectors -> vectors , vector','vectors',3,'p_vectors','Mparser.py',128),
  ('vectors -> vector','vectors',1,'p_vectors','Mparser.py',129),
  ('vector -> [ variables ]','vector',3,'p_vector','Mparser.py',137),
  ('variables -> variables , variable','variables',3,'p_variables','Mparser.py',142),
  ('variables -> variable','variables',1,'p_variables','Mparser.py',143),
  ('variable -> number','variable',1,'p_variable','Mparser.py',151),
  ('variable -> var','variable',1,'p_variable','Mparser.py',152),
  ('variable -> element','variable',1,'p_variable','Mparser.py',153),
  ('element -> vector_element','element',1,'p_element','Mparser.py',158),
  ('element -> matrix_element','element',1,'p_element','Mparser.py',159),
  ('vector_element -> var [ INT ]','vector_element',4,'p_vector_element','Mparser.py',164),
  ('matrix_element -> var [ INT , INT ]','matrix_element',6,'p_matrix_element','Mparser.py',168),
  ('number -> INT','number',1,'p_number','Mparser.py',172),
  ('number -> FLOAT','number',1,'p_number','Mparser.py',173),
  ('string -> STRING','string',1,'p_string','Mparser.py',178),
  ('expression -> expression + expression','expression',3,'p_bin_expression','Mparser.py',182),
  ('expression -> expression - expression','expression',3,'p_bin_expression','Mparser.py',183),
  ('expression -> expression * expression','expression',3,'p_bin_expression','Mparser.py',184),
  ('expression -> expression / expression','expression',3,'p_bin_expression','Mparser.py',185),
  ('expression -> expression DOTADD expression','expression',3,'p_bin_expression','Mparser.py',186),
  ('expression -> expression DOTSUB expression','expression',3,'p_bin_expression','Mparser.py',187),
  ('expression -> expression DOTMUL expression','expression',3,'p_bin_expression','Mparser.py',188),
  ('expression -> expression DOTDIV expression','expression',3,'p_bin_expression','Mparser.py',189),
  ('expression -> num_expression','expression',1,'p_expression','Mparser.py',193),
  ('expression -> matrix','expression',1,'p_expression','Mparser.py',194),
  ('expression -> matrix_function','expression',1,'p_expression','Mparser.py',195),
  ('expression -> vector','expression',1,'p_expression','Mparser.py',196),
  ('expression -> uminus','expression',1,'p_expression','Mparser.py',197),
  ('expression -> transposition','expression',1,'p_expression','Mparser.py',198),
  ('expression -> matrix_element','expression',1,'p_expression','Mparser.py',199),
  ('expression -> vector_element','expression',1,'p_expression','Mparser.py',200),
  ('num_expression -> number','num_expression',1,'p_num_expression','Mparser.py',205),
  ('num_expression -> var','num_expression',1,'p_num_expression','Mparser.py',206),
  ('var -> ID','var',1,'p_var','Mparser.py',211),
  ('uminus -> - expression','uminus',2,'p_uminus','Mparser.py',216),
  ("transposition -> expression '",'transposition',2,'p_transposition','Mparser.py',221),
  ('statement -> BREAK','statement',1,'p_break_statement','Mparser.py',226),
  ('statement -> CONTINUE','statement',1,'p_continue_statement','Mparser.py',231),
  ('statement -> RETURN expression','statement',2,'p_return_statement','Mparser.py',236),
  ('statement -> PRINT print_vals','statement',2,'p_print_statement','Mparser.py',241),
  ('print_vals -> print_vals , print_val','print_vals',3,'p_print_vals','Mparser.py',246),
  ('print_vals -> print_val','print_vals',1,'p_print_vals','Mparser.py',247),
  ('print_val -> string','print_val',1,'p_print_val','Mparser.py',255),
  ('print_val -> expression','print_val',1,'p_print_val','Mparser.py',256),
]
