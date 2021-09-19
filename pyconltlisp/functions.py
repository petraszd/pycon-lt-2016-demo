class Func:
    def call(self, env, nodes):
        raise NotImplementedError()


class Plus(Func):
    def call(self, env, nodes):
        return sum(x.evaluate(env) for x in nodes)


class Minus(Func):
    def call(self, env, nodes):
        return nodes[0].evaluate(env) - sum(x.evaluate(env) for x in nodes[1:])


class Less(Func):
    def call(self, env, nodes):
        return int(nodes[0].evaluate(env) < nodes[1].evaluate(env))


class If(Func):
    def call(self, env, nodes):
        condition = nodes[0]
        when_true = nodes[1]
        when_false = nodes[2]

        if condition.evaluate(env) != 0:
            return when_true.evaluate(env)
        else:
            return when_false.evaluate(env)


class DefineFunc(Func):
    def call(self, env, nodes):
        func_name = nodes[0].name
        func_params = [x.name for x in nodes[1].children]
        func_body = nodes[2:]

        env.define(func_name, FuncCall(func_params, func_body))
        return 1


class Display(Func):
    def call(self, env, nodes):
        print(nodes[0].evaluate(env))
        return 1


class FuncCall(Func):
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def call(self, env, nodes):
        with env.new_scope():
            new_definitions = []
            for i, name in enumerate(self.params):
                new_definitions.append((name, nodes[i].evaluate(env)))

            for name, value in new_definitions:
                env.define(name, value)

            result = 0
            for node in self.body:
                result = node.evaluate(env)
            return result
