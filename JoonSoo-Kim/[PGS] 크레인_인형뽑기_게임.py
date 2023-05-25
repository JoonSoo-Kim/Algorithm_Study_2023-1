def make_board_stack(board: list):
    n = len(board)
    board_stack = []
    for i in range(n):
        stack = []

        for j in range(n - 1, -1, -1):
            if board[j][i] == 0:
                continue
            stack.append(board[j][i])

        board_stack.append(stack)
    return board_stack


def solution(board, moves):
    answer = 0
    board_stack = make_board_stack(board)
    print(board_stack)
    basket_stack = []

    for move in moves:
        if len(board_stack[move - 1]) == 0:
            continue

        basket_stack.append(board_stack[move - 1].pop())
        if len(basket_stack) > 1:
            if basket_stack[-1] == basket_stack[-2]:
                basket_stack.pop()
                basket_stack.pop()
                answer += 2

    return answer