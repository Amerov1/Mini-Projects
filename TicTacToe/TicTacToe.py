# Tic Tac Toe

boarder=[]
index_list=[]

for i in range(9):
    boarder.append(' ')
def get_players_name():
    player1=input("Enter player one name: ")
    player2=input("Enter player two name: ")
    return player1, player2

def give_instructrions():
   
    instructions= """
    this will be our tic tac toe board
                   1 | 2 | 3
                  ---|---|---
                   4 | 5 | 6
                  ---|---|---
                   7 | 8 | 9
    *instructions:
    1. Insert the spot number between (1-9) to put a X or O.
    2. All spots must be filed in order to get the final result.
    3. Player 1 always will go first. """
    return instructions

def calculate_result(p1, p2):
    if (boarder[0] == boarder[1] == boarder[2] == 'X' or 
        boarder[0] == boarder[3] == boarder[6] == 'X' or
        boarder[0] == boarder[4] == boarder[8] == 'X' or
        boarder[1] == boarder[4] == boarder[7] == 'X' or
        boarder[2] == boarder[5] == boarder[8] == 'X' or
        boarder[3] == boarder[4] == boarder[5] == 'X' or
        boarder[6] == boarder[7] == boarder[8] == 'X' or
        boarder[2] == boarder[4] == boarder[6] == 'X'):
        print(f"Congrants {p1} ! you won the game")
        quit("Thank you for joining !")
    elif (boarder[0] == boarder[1] == boarder[2] == 'O' or
        boarder[0] == boarder[3] == boarder[6] =='O' or
        boarder[0] == boarder[4] == boarder[8] =='O' or
        boarder[1] == boarder[4] == boarder[7] =='O' or
        boarder[2] == boarder[5] == boarder[8] =='O' or
        boarder[3] == boarder[4] == boarder[5] =='O' or
        boarder[6] == boarder[7] == boarder[8] =='O' or
        boarder[2] == boarder[4] == boarder[6] =='O'):
        print(f"Congrants {p2} ! you won the game")
        quit("Thank you for joining !")



def take_input(player_name):
    while True:
        x= int(input(f"{player_name} :"))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print("This spot is taken..")
                continue
            index_list.append(x)
            return x
        print("please enter number between 1-9")

def print_board():
    b=f"""
        {boarder[0]} | {boarder[1]} | {boarder[2]}
       ---|---|---
        {boarder[3]} | {boarder[4]} | {boarder[5]}
       ---|---|---
        {boarder[6]} | {boarder[7]} | {boarder[8]}
        """
    print(b)

          

def main():

    instructions = give_instructrions()
    print(instructions)
    player_one, player_two= get_players_name()
    print(f"{player_one}'s sign will be -> X")
    print(f"{player_two}'s sign will be -> O")
    input("Press any key to start the game")
    print_board()
    for i in range(9):
        if i % 2==0:
            index= take_input(player_one)
            boarder[index]='X'
        else:
            index= take_input(player_two)  
            boarder[index]='O'
        print_board()
        calculate_result(player_one,player_two)
    print("We have a tie")

main()
