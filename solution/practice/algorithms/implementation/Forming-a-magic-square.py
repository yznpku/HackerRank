if __name__ == '__main__':
    square = []
    for i in range(3):
        square.append(list(map(int, input().strip().split(' '))))

    magic_squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                     [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                     [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                     [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                     [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                     [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                     [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                     [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    minimum_cost = sys.maxsize

    for magic_square in magic_squares:
        current_cost = 0
        for i in range(3):
            for j in range(3):
                current_cost += abs(magic_square[i][j] - square[i][j])
        minimum_cost = min(minimum_cost, current_cost)

print(minimum_cost)
