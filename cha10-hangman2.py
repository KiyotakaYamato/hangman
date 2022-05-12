#hangman

import random

"""
hangman関数
引数：　無し
戻り値：　無し
"""

def hangman2() :
    correct_word_lst = ["sea", "fish", "dog", "cat", "sand", "land", "band"] 
    wrong_cnt = 0  #間違えた回数のカウンター

    #ハングマンの描画用 listにすることで1行ずつを表示
    stages = ["",
              "_______       ",
              "|             ",
              "|       |     ",
              "|       O     ",
              "|      /|\    ",
              "|      / \    ",
              "!             "
              ]

    sct_num = random.randint(0,100)%len(correct_word_lst)
    correct_word = correct_word_lst[sct_num]
    
    rletters = list(correct_word)
    board = ["_"] * len(correct_word) #経過表示用
    win = False
    print("Welcome to Hangman! scary...")
    while wrong_cnt < len(stages) -1 :
        print("\n")
        msg = "Think one charactor  "
        inchar = input(msg)
        if inchar in rletters :
            cind = rletters.index(inchar)
            board[cind] = inchar
            rletters[cind] = "$"  #同一文字が2つ以上あった場合の処置
        else :
            wrong_cnt += 1
        print(" ".join(board))
        e = wrong_cnt + 1
        print("\n".join(stages[0:e]))
        if "_" not in board :
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win :
        print("\n".join(stages[0:wrong_cnt+1]))
        print("You lose! answer is {}.".format(correct_word))
