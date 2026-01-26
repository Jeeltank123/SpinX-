from tkinter import *
from tkinter import messagebox
from random import *

screen = Tk()
screen.title(" Roulette ")
roulette = Label(screen,text="Roulette",bg="#0B3D2E",width=22,height=1,font=('arial',23,'bold'),fg='white')
roulette.pack()
screen.configure(background="#0B3D2E")
screen.geometry("1500x700")

bet = []
bets = {}
ballance = 5000
red = [3,9,12,18,21,27,30,36,5,14,23,32,1,7,16,19,25,34]

    
def press(btn):
    global ballance
    if len(bet) < 5:
        ballance -= 100
        bet.append(btn)
        print("user press :",bet)
    account_info()
    bet_info()

def press_2(btn):
    global bet,ballance,winby
    ballance -= 100
    if btn == 'FIRST 12':
        bet = [1,2,3,4,5,6,7,8,9,10,12]
        winby = 'FIRST 12'
    elif btn == 'SECOND 12':
        bet = [13,14,15,16,17,18,19,20,21,22,23,24]
        winby = 'SECOND 12'
    elif btn == 'THIRD 12':
        bet = [25,26,27,28,29,30,31,32,33,34,35,36]
        winby = 'THIRD 12'
    elif btn == 'Odd':
        winby = 'odd'
    elif btn == 'Even':
        winby = 'even'
    elif btn == '1-18':
        bet = [n for n in range(1,19)]
        winby = '1-18'
    elif btn == '19-36':
        bet = [n for n in range(20,37)]
        winby = '19-36'
    elif btn == 'black':
        winby = 'black'
    elif btn == 'red':
        winby = 'red'
    account_info()
    bet_info()
    
def first_row():
    x=200
    y=55
    global red
    for n in range(3,37,3):
        color_var = 'red' if n in red else 'black'
        creat_btn = Button(screen,text= n ,bg=color_var,width=5,height=2,font=('arial',19,"bold"),fg='white',command= lambda num = n :press(num))
        creat_btn.place(x = x,y = y)
        x+=85
    last_row_box(x,y)
    
def second_row():
    x=200
    y=139
    global red
    for n in range(2,36,3):
        color_var = 'red' if n in red else 'black'

        creat_btn = Button(screen,text= n ,bg=color_var,width=5,height=2,font=('arial',19,"bold"),fg='white',command= lambda num = n :press(num))
        creat_btn.place(x = x,y = y)
        x+=85
    last_row_box(x,y)

def third_row():
    x=200
    y=223
    global red
    for n in range(1,35,3):
        color_var = 'red' if n in red else 'black'

        creat_btn = Button(screen,text= n ,bg=color_var,width=5,height=2,font=('arial',19,"bold"),fg='white',command= lambda num = n :press(num))
        creat_btn.place(x = x,y = y)
        x+=85
    last_row_box(x,y)

def forth_row_lbl(a,b,c):
    if c == 'FIRST 12':
        lbl = Button(screen,text=c,bg="green",width=22,height=2,font=('arial',19,'bold'),fg='white',command= lambda txt = c :press_2(txt))
        lbl.place(x = a,y = b)
    elif c == 'SECOND 12':
        lbl = Button(screen,text=c,bg="green",width=22,height=2,font=('arial',19,'bold'),fg='white',command= lambda txt = c :press_2(txt))
        lbl.place(x = a,y = b)
    elif c == 'THIRD 12':
        lbl = Button(screen,text=c,bg="green",width=22,height=2,font=('arial',19,'bold'),fg='white',command= lambda txt = c :press_2(txt))
        lbl.place(x = a,y = b)

def last_row_box(x,y):
    last_btn = Button(screen,text="2/1",bg="green",width=5,height=2,font=('arial',19,'bold'),fg='white')
    last_btn.place(x = x,y = y)

def last_row_lbl(x,y,s):
    if s == 'Odd':
        lbl = Button(screen,text=s,bg="green",width=10,height=1,font=('arial',19,'bold'),fg='white',command= lambda txt = s :press_2(txt))
        lbl.place(x = x,y = y)
    elif s == 'Even':
        lbl = Button(screen,text=s,bg="green",width=10,height=1,font=('arial',19,'bold'),fg='white',command= lambda txt = s :press_2(txt))
        lbl.place(x = x,y = y)
    elif s == 'red' or s == 'black':
        lbl = Button(screen,text=s,bg=s,width=10,height=1,font=('arial',19,'bold'),fg='white',command= lambda txt = s :press_2(txt))
        lbl.place(x = x,y = y)
    else:
        lbl = Button(screen,text=s,bg="green",width=10,height=1,font=('arial',19,'bold'),fg='white',command= lambda txt = s :press_2(txt))
        lbl.place(x = x,y = y)

def design():

    first_row()
    second_row()
    third_row()

    forth_row_lbl(200,310,'FIRST 12')
    forth_row_lbl(542,310,'SECOND 12')
    forth_row_lbl(884,310,'THIRD 12')
    last_row_lbl(200,395,"Odd")
    last_row_lbl(378,395,"Even")
    last_row_lbl(541,395,"red")
    last_row_lbl(719,395,"black")
    last_row_lbl(885,395,"1-18")
    last_row_lbl(1063,395,"19-36")

#__________________________________>User Logic<__________________________________

winning_num = randint(0,36)
bet_ammount = 100
winning_ammount = 0
submit_status_var = False
winby = ''

def account_info():
    lbl = Label(screen,bg="#034F03",width=27,height=7,font=('arial',19,'bold'),fg='white')
    lbl.place(x = 200,y = 450)

    account = Label(screen,text=f"Ballance ={ballance}",bg="#293A29",width=26,height=1,font=('arial',19,'bold'),fg='white')
    account.place(x=207 ,y = 455 )

def bet_info():
    global bets,bet,winby
    bets = {}
    for b in bet:
        if b not in bets.keys():
            bets[b] = 1
        else:
            bets[b] += 1
    if  len(bet) > 0 and len(bet) <= 5 :
        text = " | ".join([f"{k} x {v}" for k,v in bets.items()])
    else:
        text = winby
    bet_num =Label(screen,text=f"Bets: {text}",bg="#293A29",width=33,height=2,font=('arial',15,'bold'),fg='white')
    bet_num.place(x=205 ,y = 520 )
    btn = Button(screen,text="SUBMIT BET",bg="#FF0022",width=20,height=1,font=('arial',15,'bold'),fg='white',command= lambda:win())
    btn.place(x = 280 ,y=580)


def win_by_colour():
    red = [3,9,12,18,21,27,30,36,5,14,23,32,1,7,16,19,25,34]
    win_color = 'red' if winning_num in red else 'black'

    bet_color = ''
    for bet_num in bet:
        bet_color = 'red' if bet_num in red else 'black'
        if win_color == bet_color:
            win_count +=1

    return win_count,win_color

def even_odd_win(winning_ammount):
    calculation_lbl = Label(screen,text=f"2 * 100",bg="#00FF4C",width=18,height=2,font=('arial',19,'bold'),fg='white')
    calculation_lbl.place(x = 705,y = 530)
    win_lbl = Label(screen,text=f"Win :{winning_ammount}",bg="#D9B84A",width=10,height=2,font=('arial',19,'bold'),fg='white')
    win_lbl.place(x = 990,y = 530)

def full_no_win(win_color,winby,winning_num):
    winning_ammount = 0
    global ballance
    if len(bet) > 0 and len(bet) < 5 :
        if winning_num in bets.keys():
            winning_ammount = 36 * bets[winning_num] * 100
            win_label("Win by Number")
            ballance += winning_ammount
            calculation_lbl = Label(screen,text=f"36 * {bets[winning_num] * 100}",bg="#00FF4C",width=18,height=2,font=('arial',19,'bold'),fg='white')
            calculation_lbl.place(x = 705,y = 530)
            win_lbl = Label(screen,text=f"Win :{winning_ammount}",bg="#D9B84A",width=10,height=2,font=('arial',19,'bold'),fg='white')
            win_lbl.place(x = 990,y = 530)
        else:
            win_label("Batter luck next time")
            win_lbl = Label(screen,text=f"Win :{winning_ammount}",bg="#D94A4A",width=20,height=2,font=('arial',19,'bold'),fg='white')
            win_lbl.place(x = 770,y = 530)
   
    elif winby == 'FIRST 12' and winning_num in [1,2,3,4,5,6,7,8,9,10,11,12]:
        winning_ammount = 2 * 100
        win_label("Number in First 12")
        ballance += winning_ammount
        even_odd_win(winning_ammount)
    
    elif winby == 'SECOND 12' and winning_num in [13,14,15,16,17,18,19,20,21,22,23,24]:
        winning_ammount = 2 * 100
        win_label("Number in second 12")
        ballance += winning_ammount
        even_odd_win(winning_ammount)
        
    elif winby == 'THIRD 12' and winning_num in [25,26,27,28,29,30,31,32,33,34,35,36]:
        winning_ammount = 2 * 100
        win_label("Number in third 12")
        ballance += winning_ammount
        even_odd_win(winning_ammount)
    
    elif winby == 'odd' and winning_num % 2 != 0:
        winning_amount = 2 * 100
        win_label("Number is odd")
        ballance += winning_amount
        even_odd_win(winning_amount)
    elif winby == 'even' and winning_num % 2 == 0:
        winning_amount = 2 * 100
        win_label("Number is even")
        ballance += winning_amount
        even_odd_win(winning_amount)
    
    elif winby == win_color:
        winning_amount = 2 * 100
        win_label(f"{winby} color win")
        ballance += winning_amount
        even_odd_win(winning_amount)
    elif winby == '1-18' and winning_num in bet:
        winning_amount = 2 * 100
        win_label("Number in 1-18")
        ballance += winning_amount
        even_odd_win(winning_amount)
    elif winby == '19-36' and winning_num in bet:
        winning_amount = 2 * 100
        win_label("Number in 19-36")
        ballance += winning_amount
        even_odd_win(winning_amount)
    else:
        win_label("Batter luck next time")
        win_lbl = Label(screen,text=f"Win :{winning_ammount}",bg="#D94A4A",width=20,height=2,font=('arial',19,'bold'),fg='white')
        win_lbl.place(x = 770,y = 530)
    account_info()
    bet.clear()
    bets.clear()

def win_label(text):
    win_lbl = Label(screen,text=text,bg="#000000",width=18,height=2,font=('arial',19,'bold'),fg='white')
    win_lbl.place(x = 875,y = 455)

def win():
    global ballance,winning_num,winby,red
    win_color = 'red' if winning_num in red else 'black'
    main_lbl = Label(screen,bg="#034F03",width=30,height=7,font=('arial',19,'bold'),fg='white')
    main_lbl.place(x = 700,y = 450)

    main_lbl = Label(screen,text=f"winning {winning_num}",bg=win_color,width=10,height=2,font=('arial',19,'bold'),fg='white')
    main_lbl.place(x = 705,y = 455)
    last_bet()
    full_no_win(win_color,winby,winning_num)
    winning_num = randint(1,36)

def last_bet():
    last_bets = bet
    last_bet_lbl = Label(screen,text=f"last Bet :{last_bets}",bg="#006735",width=29,height=1,font=('arial',19,'bold'),fg='white')
    last_bet_lbl.place(x = 705,y = 605)