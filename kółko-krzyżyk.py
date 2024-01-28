def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Sprawdzanie wierszy i kolumn
    for i in range(3):
        if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
            return 'X'
        elif all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
            return 'O'

    # Sprawdzanie przekątnych
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    return None

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Gracz {current_player}, twój ruch!")

        row = int(input("Podaj numer wiersza (0-2): "))
        col = int(input("Podaj numer kolumny (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Gracz {winner} wygrywa!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Remis! Plansza jest pełna.")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("To pole jest już zajęte. Wybierz inne.")

if __name__ == "__main__":
    tic_tac_toe()
