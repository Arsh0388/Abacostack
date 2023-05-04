# collaborated with charan,sanket,viraj, Harsh Patel.
import AbacoStack
def main():
    game = True
    string_size,string_depth= input(" enter the size and depth of the stack ").split(' ')
    size = int(string_size)
    depth = int(string_depth)
    assert  2<= size <= 5 and 2 <= depth <= 4 , " incorrect dimensions for stack "

    stack_moves = 'udlr'
    valid_moves = ['0r']
    game_play = AbacoStack.AbacoStack(size,depth)

    for i in range(size) :
        for j in range(len(stack_moves)) :
            stack_move = f"{i+1}{stack_moves[j]}"
            valid_moves.append(stack_move)

    last = f"{size + 1}l"
    valid_moves.append(last)
    target = AbacoStack.Card(size,depth)
    print(valid_moves)

    while game == True :
        gamecontinue = input(" P for play, Q for Quit and R for reset ")
        if gamecontinue.upper() == 'P':
            game_play.show()
            moves = input(" enter a move ").split(' ')
            for i in range(len(moves)) :
                if i <= 4 :
                    if moves[i] in valid_moves :
                        game_play.movebead(moves[i])
                    else :
                        print(" invalid move")
            game_play.show()

            if game_play.isSolved() :
                print(" Congrats you won thakns for playing ")
                answer = input(" if you want to play or not ")
                if answer == "yes" or "Y" :
                    game_play.reset()
                else :
                    game = False


        elif gamecontinue.upper() == 'Q' :
            print(" thank you, have a good day ")
            game = False

        elif gamecontinue.upper() == 'R' :
            game_play.reset()


main()
