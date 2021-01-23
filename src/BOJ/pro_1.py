def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                basket.append(row[move - 1])
                row[move - 1] = 0

                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 1
                break
    return answer * 2
