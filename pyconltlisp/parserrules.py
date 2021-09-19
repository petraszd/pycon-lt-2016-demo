from pyconltlisp.lexerrules import tokens
from pyconltlisp import nodes


class ParserWalker:
    def __init__(self):
        self.reset()

    def reset(self):
        self.root = nodes.Block()
        self.stack = [self.root]
        self.current = self.root

    @property
    def tokens(self):
        return tokens

    def p_root(self, t):
        'root : blocks'

    def p_blocks_list(self, t):
        'blocks : block blocks'

    def p_blocks_last(self, t):
        'blocks : block'

    def p_block(self, t):
        'block : begin elements end'

    def p_begin(self, t):
        'begin : S_BEGIN'
        block = nodes.Block()
        self.current.children.append(block)
        self.stack.append(block)
        self.current = block

    def p_end(self, t):
        'end : S_END'
        self.stack.pop()
        self.current = self.stack[-1]

    def p_elements_list(self, t):
        'elements : elem elements'

    def p_elements_last(self, t):
        'elements : elem'

    def p_elem_number(self, t):
        'elem : NUMBER'
        self.current.children.append(nodes.Number(t[1]))

    def p_elem_symbol(self, t):
        'elem : SYMBOL'
        self.current.children.append(nodes.Symbol(t[1]))

    def p_elem_block(self, t):
        'elem : block'

    def p_error(self, t):
        print("Parser error")
