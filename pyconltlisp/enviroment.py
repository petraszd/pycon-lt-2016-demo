from pyconltlisp import functions

from contextlib import contextmanager


class Enviroment(object):
    def __init__(self):
        self.scope_stack = [self.get_buildin_scope()]

    def get_buildin_scope(self):
        return {
            '+': functions.Plus(),
            '-': functions.Minus(),
            '<': functions.Less(),
            'if': functions.If(),
            'display': functions.Display(),
            'func': functions.DefineFunc(),
        }

    @contextmanager
    def new_scope(self):
        self.enter_scope()
        yield
        self.exit_scope()

    def enter_scope(self):
        self.scope_stack.append({})

    def exit_scope(self):
        self.scope_stack.pop()

    def get(self, key):
        for scope in reversed(self.scope_stack):
            if key in scope:
                return scope[key]

    def define(self, key, val):
        self.scope_stack[-1][key] = val
