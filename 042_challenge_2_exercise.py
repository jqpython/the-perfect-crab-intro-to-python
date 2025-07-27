# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but actually isn't very
# realistic. Most software engineers spend their time modifying and maintaining
# existing programs, not writing entirely new ones.

# Below is the same program as in the example. Your challenge is to implement
# some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely optional. Don't
# forget about your assessment!

# def play_game():
#   board = [
#     [".", ".", "."],
#     [".", ".", "."],
#     [".", ".", "."]
#   ]
#   player = "X"
#   while not is_game_over(board):
#     print(print_board(board))
#     print("It's " + player + "'s turn.")
#     # `input` asks the user to type in a string
#     # We then need to convert it to a number using `int`
#     row = int(input("Enter a row: "))
#     column = int(input("Enter a column: "))
#     board = make_move(board, row, column, player)
#     if player == "X":
#       player = "O"
#     else:
#       player = "X"
#   print(print_board(board))
#   print("Game over!")

# def print_board(board):
#   formatted_rows = []
#   for row in board:
#     formatted_rows.append(" ".join(row))
#   grid = "\n".join(formatted_rows)
#   return grid

# def make_move(board, row, column, player):
#   board[row][column] = player
#   return board


# # This function will extract three cells from the board
# def get_cells(board, coord_1, coord_2, coord_3):
#   return [
#     board[coord_1[0]][coord_1[1]],
#     board[coord_2[0]][coord_2[1]],
#     board[coord_3[0]][coord_3[1]]
#   ]

# # This function will check if the group is fully placed with player marks, no
# # empty spaces.
# def is_group_complete(board, coord_1, coord_2, coord_3):
#   cells = get_cells(board, coord_1, coord_2, coord_3)
#   return "." not in cells

# # This function will check if the group is all the same
# # player mark: X X X or O O O
# def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
#   cells = get_cells(board, coord_1, coord_2, coord_3)
#   return cells[0] == cells[1] and cells[1] == cells[2]

# # We'll make a list of groups to check:

# groups_to_check = [
#   # Rows
#   [(0, 0), (0, 1), (0, 2)],
#   [(1, 0), (1, 1), (1, 2)],
#   [(2, 0), (2, 1), (2, 2)],
#   # Columns
#   [(0, 0), (1, 0), (2, 0)],
#   [(0, 1), (1, 1), (2, 1)],
#   [(0, 2), (1, 2), (2, 2)],
#   # Diagonals
#   [(0, 0), (1, 1), (2, 2)],
#   [(0, 2), (1, 1), (2, 0)]
# ]

# def is_game_over(board):
#   # We go through our groups
#   for group in groups_to_check:
#     # If any of them are empty, they're clearly not a winning row, so we skip
#     # them.
#     if is_group_complete(board, group[0], group[1], group[2]):
#       if are_all_cells_the_same(board, group[0], group[1], group[2]):
#         return True # We found a winning row!
#         # Note that return also stops the function
#   return False # If we get here, we didn't find a winning row

# # And test it out:

# print("Game time!")
# play_game()

# different solution to achieve the same result with complete error handlings

def play_game(board_size):
    board = []
    for _ in range(board_size):
        row = ["."] * board_size
        board.append(row)

    player = "X"
    groups_to_check = generate_groups_to_check(board_size)

    while not is_game_over(board, groups_to_check):
        print(print_board(board))
        print("It's " + player + "'s turn.")
        # Get valid move from player
        while True:
            try:
                
                row = int(input("Enter a row (0-{}): ".format(board_size - 1)))
                column = int(input("Enter a column (0-{}): ".format(board_size-1)))

                # Check if row and column are within bounds
                if row < 0 or row >=board_size or column < 0 or column >= board_size:
                    print("Row and column must be within the board dimensions.")
                    continue

                # Check if the cell is empty
                if board[row][column] != ".":
                    print("That cell is already occupied. Choose another. ")
                    continue

                break

            except ValueError:
                print("Please enter valid integers for row and column.")
            except IndexError:
                print("Row and coulumn must be within the board dimensions.")
            except KeyboardInterrupt:
                print("\nGame interrupted by user. Exiting...")
                exit()  # Exit the game entirely

        board = make_move(board, row, column, player)

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    print(print_board(board))
    # Check if there is a winner
    winner_found = False
    for group in groups_to_check:
        if is_group_complete(board,group) and are_all_cells_the_same(board, group):
            winner_found = True
            break

    if is_board_full(board) and not winner_found:
        print("Game over! it's a draw")
    else:
        winner = "O" if player == "X" else "X"
        print("Gamer over! Player " + winner + " wins!")

def is_board_full(board):
    for row in board:
        if "." in row:
            return False
    return True

def print_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid

def make_move(board,row, column, player):
    board[row][column] = player
    return board

def generate_groups_to_check(n):
    groups = [] # [[(0,0), (0,1), (0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)]

    # add rows
    for row in range(n): # 0
        group = []
        for col in range(n): # 0
            group.append((row,col))
        groups.append(group)

    # add columns
    for col in range(n):
        group = []
        for row in range(n):
            group.append((row,col))
        groups.append(group)

    diagonal1 = []
    for i in range(n):
        diagonal1.append((i,i))
    groups.append(diagonal1)

    diagonal2 = []
    for i in range(n):
        diagonal2.append((i, n-1-i))
    groups.append(diagonal2)

    return groups

def get_cells(board, coords):
    return [board[coord[0]][coord[1]] for coord in coords]

def is_group_complete(board, coords):
    cells = get_cells(board, coords)
    return "." not in cells

def are_all_cells_the_same(board, coords):
    cells = get_cells(board, coords)
    if len(cells) == 0:
        return False
    first = cells[0]
    if first == ".":
        return False
    return all(cell == first for cell in cells)

def is_game_over(board, groups_to_check):
    for group in groups_to_check:
        if is_group_complete(board,group):
            if are_all_cells_the_same(board, group):
                return True
    if is_board_full(board):
        return True

    return False

# handling user input using clean and modular approaches.

def get_board_size_from_user():
    """
    Prompt the user for a board size and return it as an integer.
    Handles invalid inputs and ensures the size is within valid bounds.
    """
    MIN_BOARD_SIZE = 3
    MAX_BOARD_SIZE = 10

    while True:
        try:
            user_input = input("Enter the Board Size: ")
            board_size = int(user_input)

            if board_size <= 0:
                print("Board size must be a positive integer. Please try again.")
                continue

            if board_size < MIN_BOARD_SIZE:
                print(f"Board size must be at least {MIN_BOARD_SIZE}. Please try again.")
                continue

            if board_size > MAX_BOARD_SIZE:
                print(f"Board size must be at most {MAX_BOARD_SIZE}. Please try again.")
                continue

            return board_size

        except ValueError:
            if user_input.strip() == "":
                print("No input provided. Please enter a valid integer for the board size.")
            else:
                print(f"'{user_input}' is not a valid integer. Please enter a positive integer for the board size.")
        except KeyboardInterrupt:
            print("\nInterrupted by the user!")
            exit()

def main():
    """Main function to run the game."""
    # Get and validate board size
    board_size = get_board_size_from_user()

    # Display board size and start the game
    print(f"Board Size: {board_size} x {board_size}")
    play_game(board_size)

if __name__ == "__main__":
    main()
