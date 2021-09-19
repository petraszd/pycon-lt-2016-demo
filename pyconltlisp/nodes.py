class Node:
    def evaluate(self, env):
        raise NotImplementedError()

    def can_be_a_funtion_name(self):
        return False


class Block(Node):
    def __init__(self):
        self.children = []

    def evaluate(self, env):
        if self.is_a_function_call():
            return self.evaluate_function_call(env)
        else:
            return self.evaluate_each_child(env)

    def is_a_function_call(self):
        return self.children and self.children[0].can_be_a_funtion_name()

    def evaluate_each_child(self, env):
        with env.new_scope():
            result = 0
            for c in self.children:
                result = c.evaluate(env)
            return result

    def evaluate_function_call(self, env):
        function = env.get(self.children[0].name)
        return function.call(env, self.children[1:])


class Number(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value


class Symbol(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self, env):
        return env.get(self.name)

    def can_be_a_funtion_name(self):
        return True
