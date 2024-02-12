qwe=input()



def check_brackets(text):
    stack = []
    for i, char in enumerate(text):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return f'неправильно расставлены скобки: лишняя закрывающая скобка в позиции {i}'
            stack.pop()
    if stack:
        return f'неправильно расставлены скобки: {len(stack)} лишних открывающих скобок'
    return 'скобки расставлены правильно'
check_brackets(qwe)
