import re

def apply_op(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '*':
        return v1 * v2

def evaluate_expression(expression, precedence):
    result = None
    val_q = []
    op_q = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() and precedence:
            val_q.append(int(expression[i]))
            if op_q and op_q[-1] == '+':
                v1 = val_q.pop()
                v2 = val_q.pop()
                op = op_q.pop()
                val_q.append(apply_op(v1, v2, op))

        elif expression[i].isdigit() and not precedence:
            val_q.append(int(expression[i]))

        elif expression[i] in ('*', '+'):
            op_q.append(expression[i])

        elif expression[i] in ('('):
            c = 1
            for j in range(i+1, len(expression)):
                if expression[j] == '(':
                    c += 1
                if expression[j] == ')':
                    c -= 1
                if not c:
                    val_q.append(evaluate_expression(expression[i+1:j], precedence))
                    if precedence and op_q and op_q[-1] == '+':
                        v1 = val_q.pop()
                        v2 = val_q.pop()
                        op = op_q.pop()
                        val_q.append(apply_op(v1, v2, op))
                    i = j
                    break
        i += 1
    for op in op_q:
        v1 = val_q.pop(0)
        v2 = val_q.pop(0)
        val_q.insert(0, apply_op(v1, v2, op))
    return val_q.pop(0)

if __name__ == '__main__':
    file = open('day18_input.txt', 'r')
    expressions = list(file.read().split('\n'))

    results = [evaluate_expression(e, precedence=False) for e in expressions]
    print('Sum of expressions = {}'.format(sum(results)))

    results = [evaluate_expression(e, precedence=True) for e in expressions]
    print('Sum of expressions = {}'.format(sum(results)))
