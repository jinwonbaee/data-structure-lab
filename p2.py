# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.
    # 입력 힌트
    open_brackets = 0
    close_brackets = 0
    for char in input:
        print(char)
        if char == '(':
            open_brackets += 1
        elif char == ')':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                close_brackets += 1

    result = 0
    result = open_brackets + close_brackets
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
