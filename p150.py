def eval_rpn(tokens: list[str]) -> int:
    stack = list[int]()
    for token in tokens:
        match token:
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            case "*":
                stack.append(stack.pop() * stack.pop())
            case "/":
                b, a = stack.pop(), stack.pop()
                sign = 1 if (a * b) > 0 else -1
                stack.append(sign * (abs(a) // abs(b)))
            case _:
                stack.append(int(token))
    return stack[0]


def test_example1() -> None:
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_example2() -> None:
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_case15() -> None:
    assert (
        eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        == 22
    )
