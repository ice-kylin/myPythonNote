class Stack:
    def __init__(self, *elements) -> None:
        self._stack = list(elements)

    def push(self, element):
        self._stack.append(element)
        return self

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0


def calc_rpn_rst(rpns: str) -> float:
    calc_stack = Stack()

    for rpn in rpns:
        try:
            flt_rpn = float(rpn)
        except ValueError:
            num_2 = calc_stack.pop()
            num_1 = calc_stack.pop()
            if rpn == '+':
                calc_stack.push(num_1 + num_2)
            elif rpn == '-':
                calc_stack.push(num_1 - num_2)
            elif rpn == '*':
                calc_stack.push(num_1 * num_2)
            elif rpn == '/':
                calc_stack.push(num_1 / num_2)
        else:
            calc_stack.push(flt_rpn)

    return calc_stack.pop()


print(calc_rpn_rst('5328+2/4-*-'))
