def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue

        first = stack.pop()
        second = i

        if first == second:
            pass
        else:
            stack.append(first)
            stack.append(second)

    return 1 if len(stack) == 0 else 0