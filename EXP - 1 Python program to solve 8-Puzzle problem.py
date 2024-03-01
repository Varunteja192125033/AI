from queue import Queue

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3

def swap_tiles(board, row1, col1, row2, col2):
    temp = board[row1][col1]
    board[row1][col1] = board[row2][col2]
    board[row2][col2] = temp

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_goal_state(board, goal_state):
    return board == goal_state

def solve_8_puzzle(initial_state, goal_state):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    queue = Queue()
    queue.put((initial_state, []))

    while not queue.empty():
        current_state, path = queue.get()

        if is_goal_state(current_state, goal_state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_board(step)
                print()
            return

        zero_row, zero_col = next((i, j) for i, row in enumerate(current_state) for j, tile in enumerate(row) if tile == 0)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if is_valid_move(current_state, new_row, new_col):
                new_board = [row.copy() for row in current_state]
                swap_tiles(new_board, zero_row, zero_col, new_row, new_col)
                queue.put((new_board, path + [new_board]))

    print("No solution found.")

initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
solve_8_puzzle(initial_state, goal_state)
