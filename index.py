import random

def initBoard():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def logBoard(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def checkWinner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def playGame():
    board = initBoard()
    current_player = 'X'
    game_over = False

    players = int(input("Виберіть режим гри:\n1.Грати проти комп'ютера\n2.Грати проти іншого гравця\n"))

    while players not in [1, 2]:
        players = int(input("Введіть правильний номер режиму (1 або 2): "))

    while not game_over:
        logBoard(board)

        if current_player == 'X':
            print(f"Гравець {current_player}, ваш хід.")
            row = int(input("Введіть номер рядка (1-3): ")) - 1
            col = int(input("Введіть номер стовпця (1-3): ")) - 1

            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("Ця клітинка вже зайнята. Спробуйте ще раз.")
                continue
        else:
            if players == 1:
                print("Хід комп'ютера...")
                available_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
                row, col = random.choice(available_cells)
                board[row][col] = 'O'
            else:
                print(f"Гравець {current_player}, ваш хід.")
                row = int(input("Введіть номер рядка (1-3): ")) - 1
                col = int(input("Введіть номер стовпця (1-3): ")) - 1

                if board[row][col] == ' ':
                    board[row][col] = current_player
                else:
                    print("Ця клітинка вже зайнята. Спробуйте ще раз.")
                    continue

        winner = checkWinner(board)
        if winner:
            logBoard(board)
            if winner == 'X':
                print("Вітаємо! Гравець X переміг!")
            else:
                print("Вітаємо! Гравець O переміг!")
            game_over = True
        elif ' ' not in [cell for row in board for cell in row]:
            logBoard(board)
            print("Нічия!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

playGame()
