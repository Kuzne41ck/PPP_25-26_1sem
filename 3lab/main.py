#Задание 2
journal = []

def evaluate(expr, deystviye=0):
    global journal
    expr = expr.strip()
    journal.append(f"Действие {deystviye}: Вычисление {expr}")
    if expr.startswith("(") and expr.endswith(")"):
        index = 0
        is_fully_wrapped = True
        for i, char in enumerate(expr[:-1]):
            if char == "(":
                index += 1
            elif char == ")":
                index -= 1
            if index == 0:
                is_fully_wrapped = False
                break
        if is_fully_wrapped:
            return evaluate(expr[1:-1], deystviye)

    index = 0
    for i in range(len(expr) - 1, -1, -1):
        char = expr[i]
        if char == ")":
            index += 1
        elif char == "(":
            index -= 1
        elif index == 0 and char in "+-":
            left = evaluate(expr[:i], deystviye + 1)
            right = evaluate(expr[i + 1 :], deystviye + 1)
            result = left + right if char == "+" else left - right
            journal.append(
                f"Действие {deystviye}: Результат {expr[:i].strip()} {char} {expr[i + 1 :].strip()} = {result}"
            )
            return result

    index = 0
    for i in range(len(expr) - 1, -1, -1):
        char = expr[i]
        if char == ")":
            index += 1
        elif char == "(":
            index -= 1
        elif index == 0 and char in "*/":
            left = evaluate(expr[:i], deystviye + 1)
            right = evaluate(expr[i + 1 :], deystviye + 1)
            result = left * right if char == "*" else left // right
            journal.append(
                f"Действие {deystviye}: Результат {expr[:i].strip()} {char} {expr[i + 1 :].strip()} = {result}"
            )
            return result
        
    result = int(expr)
    journal.append(f"Действие {deystviye}: {expr} это число, результат: {result}")
    return result

journal.clear()
expression = "(2 + (3 * (4 - 1)))"
final_result = evaluate(expression)
print('Пример:', expression)
print('-'*40)
for i in journal:
    print(i)
print('-'*40)
print('Ответ:', final_result)