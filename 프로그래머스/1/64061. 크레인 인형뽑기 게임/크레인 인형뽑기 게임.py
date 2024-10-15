def solution(board, moves):
    basket = []
    answer = 0

    new_board = []
    for i in range(len(board[0])):
        rotate = [board[j][i] for j in range(len(board)-1, -1, -1) if board[j][i] != 0]
        new_board.append(rotate)

    for move in moves:
        if new_board[move-1]:
            doll = new_board[move-1].pop()

            if not basket:
                basket.append(doll)
            else:
                f = basket.pop()
                if f != doll:
                    basket.append(f)
                    basket.append(doll)
                else:
                    answer += 2

    return answer