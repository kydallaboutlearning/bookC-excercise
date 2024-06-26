def challenge2():
    ans1 = 12*(8+3)
    que = "12*(8+3)"
    print(ans1)

    print(f"You are to predict the answers \n predict the value of this expression: {que} ")

    trial_check = True
    while trial_check:
        
        try:
            ans = int(input((("What's your answer: "))))
        except ValueError:
            print('input only numerals')
        else:
            pass


        if ans == ans1 :
            print('Correct Prediction')
            trial_check = False
        else:
            print("wrong try again")

if __name__ == '__main__':
    challenge2()
