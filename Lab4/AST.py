
class Node(object):
    def accept(self, visitor):
        return visitor.visit(self)


class Instructions(Node):
    def __init__(self, new_instruction, instructions=None):
        if instructions is not None:
            self.instructions = instructions.instructions
        else:
            self.instructions = []
        self.instructions.append(new_instruction)


class BinExpr(Node):
    def __init__(self, bin_op, left, right, line):
        self.bin_op = bin_op
        self.left = left
        self.right = right
        self.line = line


class Cond(Node):
    def __init__(self, rel_op, left, right, line):
        self.rel_op = rel_op
        self.left = left
        self.right = right
        self.line = line


class AssignOperation(Node):
    def __init__(self, variable, op, expression, line):
        self.variable = variable
        self.op = op
        self.expression = expression
        self.line = line


class If(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction


class IfElse(Node):
    def __init__(self, condition, instruction, else_instruction):
        self.condition = condition
        self.instruction = instruction
        self.else_instruction = else_instruction


class WhileLoop(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction


class ForLoop(Node):
    def __init__(self, l_id, f_range, instruction):
        self.l_id = l_id
        self.f_range = f_range
        self.instruction = instruction


class Break(Node):
    def __init__(self, line):
        self.line = line


class Continue(Node):
    def __init__(self, line):
        self.line = line


class Return(Node):
    def __init__(self, val):
        self.val = val


class Print(Node):
    def __init__(self, print_vars):
        self.print_vars = print_vars


class Matrix(Node):
    def __init__(self, new_vector,line, matrix=None):
        if matrix is not None:
            self.matrix = matrix.matrix.copy()
        else:
            self.matrix = []    
        self.matrix.append(new_vector)
        self.line = line


class Vector(Node):
    def __init__(self, new_elem, line, vector=None):
        self.vector = vector.vector.copy() if vector else []
        self.vector.append(new_elem)
        self.line = line


class PrintVals(Node):
    def __init__(self, new_val, vals=None):
        self.vals = vals.vals.copy() if vals else []
        self.vals.append(new_val)


class Num(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name, line):
        self.name = name
        self.line = line


class Range(Node):
    def __init__(self, start, end, line):
        self.start = start
        self.end = end
        self.line = line


class MatrixFunction(Node):
    def __init__(self, func, value, line):
        self.func = func
        self.value = value
        self.line = line


class Transposition(Node):
    def __init__(self, matrix):
        self.matrix = matrix


class Uminus(Node):
    def __init__(self, expression):
        self.expression = expression


class ID(Node):
    def __init__(self, id, line):
        self.id = id
        self.line = line


class VectorElement(Node):
    def __init__(self, id, index, line):
        self.id = id
        self.index = index
        self.line = line


class MatrixElement(Node):
    def __init__(self, id, index_x, index_y, line):
        self.id = id
        self.index_x = index_x
        self.index_y = index_y
        self.line = line


class Error(Node):
    def __init__(self):
        pass


class Empty(Node):
    def __init__(self):
        pass

