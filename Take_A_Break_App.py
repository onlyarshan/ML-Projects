import tkinter
from tkinter import messagebox
from tkinter import *
import webbrowser as wb
import time as t

# creating Main window
window = tkinter.Tk()
window.title("Take A Break App")
window.resizable(860, 600)

# defining required Function


def func():
    foc_out()
    counter()


mins = 30
seconds = 0
time_left = StringVar()
rem_time = StringVar()

def foc_out():
    global mins
    """function that gets called whenever entry is clicked"""

    if time_entry.get() != 'Enter Time in Minute' :
        mins = time_entry.get()

    if time_entry.get() == '':
        mins = 30

    global seconds
    seconds = 60 * int(mins)

# Dereasing Counter


def counter():

    global time_left
    global seconds
    while seconds > 0:
        seconds -= 1
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        time_left.set(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
        count.config(textvariable= time_left)
        # call this function again in 1,000 milliseconds
        window.after(1000, counter)

        if seconds == 600:
            messagebox.showinfo('Message', 'Alert..!! 10 Minutes Remaining For Next Break')
            time_60()
        if seconds == 0:
            messagebox.showinfo('Message', 'Hey Dude..!! Its Time For Break \n Click Ok to Continue')
            time_zero()
        break


def on_entry_click(event):
    if time_entry.get() == 'Enter Time in Minute':
        time_entry.delete(0, "end")  # delete all the text in the entry
        time_entry.insert(0, '')  # Insert blank for user input


# Labelling on Main Window

hello = Label(window, text="Welcome to Take A Break App..!! \n Hello..!!" )
hello.grid(row = 0, column= 1, sticky = E + W)

set_time = Button(window, text = "Start", command = lambda: func(), fg= "Black")
set_time.grid(row = 1, column = 0, padx = 10, pady= 10)

time_entry = tkinter.Entry(window, width=19,)
time_entry.grid(row =1, column =1, sticky = W+E)
time_entry.insert(0,"Enter Time in Minute")
time_entry.bind('<FocusIn>', on_entry_click)

clock = Label(window, fg= "Black", font=("Helvetica", 12))
clock.grid(row = 1, column=2, padx = 10, pady = 10)

count = Label(window, fg= "Black", text = '00:00:00', bd = 3, font=("Helvetica", 30))
count.grid(row = 2, column=1, padx = (10), pady = 10, )

quitbutton = Button(window, text = "Exit", command = lambda: quit(window), fg = "black")
quitbutton.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = E+S)

# Notification At time = 10 mins, Aleart for next break

mi = ''


def time_60():
    import tkinter
    from tkinter import Label, Button, OptionMenu, StringVar, E, W
    global seconds
    global rem_time
    global mins
    notify = tkinter.Tk()
    notify.title("Notification")

    def tabn(x):
        time_entry.delete(0, "end")
        global seconds
        seconds = 0
        notify.destroy()
        func()
        option()

    def snooz(x):

        global seconds
        mi = int(variable.get())
        seconds = seconds + 60 * mi

    msg = Label(notify, text='00:00', fg="Black")
    msg.grid(row=1, column=0)

    alert = Label(notify, text= 'Alert..!!')
    alert.grid(row = 0, column= 1, sticky = E + W)
    msg1 = Label(notify, text= 'Minutes Remaining For Next Break')
    msg1.grid(row = 1, column= 1, sticky = E + W)

    now = Button(notify, text = "Take A Break Now", command = lambda: tabn(seconds), fg= "Black")
    now.grid(row = 2, column = 0)

    snooze = Button(notify, text = "Snooze By", command= lambda: snooz(seconds), fg= "Black")
    snooze.grid(row = 2, column = 1)

    variable = StringVar(notify)
    variable.set('5') # default value

    w = OptionMenu(notify, variable, '5', '10', '15')
    w.grid(row = 2, column = 2)

    lbl = Label(notify, text= 'minutes')
    lbl.grid(row = 2, column= 3, sticky =W)

    ok = Button(notify, text = "Close", command = lambda: notify.destroy(), fg= "Black")
    ok.grid(row = 3, column = 1, padx = 2, pady = 10)

    def time_remaining():
        global rem_time
        global seconds
        if seconds < 600:
            seconds -= 1
            m, s = divmod(seconds, 60)
            rem_time.set(str(m).zfill(2) + ":" + str(s).zfill(2))
            msg.config(textvariable=rem_time)

    notify.after(1000, time_remaining)
    time_remaining()
    notify.mainloop()



## When Global Time Is Zero Condition


def time_zero():
    import tkinter
    from tkinter import Button, Label, StringVar, OptionMenu, E, W

    notify1 = tkinter.Tk()
    notify1.title("Notification")

    def skip(x):
        time_entry.delete(0, "end")
        notify1.destroy()
        func()

    def snooz(x):
        global mi
        global seconds
        mi = int(variable.get())
        seconds = seconds + 60 * mi

    alert = Label(notify1, text= 'Hey Dude..!! Its Time For Break')
    alert.grid(row = 0, column= 1, sticky = E + W)

    skip1 = Button(notify1, text = "Skip Break", command = lambda: skip(seconds), fg= "Black")
    skip1.grid(row = 2, column = 0)

    snooze = Button(notify1, text = "Snooze By", command= lambda: snooz(seconds), fg= "Black")
    snooze.grid(row = 2, column = 1)

    variable = StringVar(notify1)
    variable.set('5') # default value

    w = OptionMenu(notify1, variable, '5', '10', '15')
    w.grid(row = 2, column = 2)

    lbl = Label(notify1, text= 'minutes')
    lbl.grid(row = 2, column= 3, sticky =W)

    ok = Button(notify1, text = "ok", command = lambda: [notify1.destroy(), option()], fg= "Black")
    ok.grid(row = 3, column = 1, padx = 2, pady = 10)
    notify1.mainloop(0)


# defining Time CLock

time1 = ''


def tick():
    global time1
    # get the current local time from the PC
    time2 = t.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)
tick()
# New Window OPtion


def option():
    import tkinter
    from tkinter import Button
    import webbrowser as wb

    suggest = tkinter.Tk()
    suggest.title("Take A Break App")

    def openfb(x):
        wb.open(x)

    def openinsta(x):
        wb.open(x)

    def opennews(x):
        wb.open(x)

    news = Button(suggest, text = "News", command = lambda: opennews("www.msn.com"), fg= "Black")
    news.grid(row = 2, column = 0, padx = (10), pady = 10)

    fb = Button(suggest, text = "Facebook", command = lambda: openfb("www.facebook.com"), fg= "Black")
    fb.grid(row = 2, column = 1, padx = (10), pady = 10)

    insta = Button(suggest, text = "Instagram", command= lambda: openinsta("www.instagram.com"), fg= "Black")
    insta.grid(row = 2, column = 2, padx = (10), pady = 10)

    game = Button(suggest, text = "Game", fg= "Black", command = lambda : guees_game())
    game.grid(row = 3, column = 0, padx = (10), pady = 10)


    Ytb = Button(suggest, text = "Youtube", fg= "Black", command = lambda : youtubewindow())
    Ytb.grid(row = 3, column = 2, padx = (10), pady = 10)

    cancel = Button(suggest, text = "Cancel", command = lambda: suggest.destroy(), fg = "black")
    cancel.grid(row = 4, column = 2, padx = (10), pady = 10)

    suggest.mainloop(0)
# Defining Gussing Game


def guees_game():
    import tkinter
    import random

    computer_guess = random.randint(1, 10)

    def check():
        # Get the value from txt_guess
        user_guess = int(txt_guess.get())

        # Determine higher, lower, or just right
        if user_guess < computer_guess:
            msg = "Higher!"
        elif user_guess > computer_guess:
            msg = "Lower!"
        elif user_guess == computer_guess:
            msg = "Correct! press reset to play again or close window"
        else:
            msg = "Something went wrong..."

        # Show the result
        lbl_result["text"] = msg

        # Clear txt_guess
        txt_guess.delete(0, 5)

    def reset():
        # Declare the global variable
        global computer_guess
        # Get a random number
        computer_guess = random.randint(1, 10)
        # Change the lbl_result text
        lbl_result["text"] = "Game reset. Guess again!"

    # Create root window
    root = tkinter.Tk()

    # Change root window background color
    root.configure(bg="white")

    # Change the title
    root.title("Guess the number!")

    # Change the window size
    #root.geometry("280x100")

    # Create Widgets
    lbl_title = tkinter.Label(root, text="Welcome to the Guessing Game!", bg="white")
    lbl_title.pack()

    lbl_title = tkinter.Label(root, text="please guess a number between 1 to 9!", bg="white")
    lbl_title.pack()

    lbl_result = tkinter.Label(root, text="Good Luck!", bg="white")
    lbl_result.pack()

    btn_check = tkinter.Button(root, text="Check", fg="green", bg="white", command=check)
    btn_check.pack(side="left")

    btn_reset = tkinter.Button(root, text="Play Again", fg="red", bg="white", command=reset)
    btn_reset.pack(side="right")

    txt_guess = tkinter.Entry(root, width=5)
    txt_guess.pack()

    cancel = tkinter.Button(root, text="Back", command=lambda: root.destroy(), bg="red", fg="black")
    cancel.pack(side = 'bottom', padx=(10), pady=10)


# Start the main events loop
    root.mainloop()


# Defining YouTube Customs

def youtubewindow():
    window = tkinter.Tk()

    def opensub(x):
        new = 1
        wb.open(x, new=new)

    def openhome(x):
        new = 1
        wb.open(x, new=new)

    def openoriginal(x):
        new = 1
        wb.open(x, new=new)

    def openhist(x):
        new = 1
        wb.open(x, new=new)

    def openlib(x):
        new = 1
        wb.open(x, new=new)

    def opengaming(x):
        new = 1
        wb.open(x, new=new)

    def openwatchlater(x):
        new = 1
        wb.open(x, new=new)

    def openymovies(x):
        new = 1
        wb.open(x, new=new)

    def openfash(x):
        new = 1
        wb.open(x, new=new)

    def opentrend(x):
        new = 1
        wb.open(x, new=new)

    Home = Button(window, text="Home", command=lambda: openhome("https://www.youtube.com/"), fg="Black")
    Home.grid(row=1, column=0, padx = 10, pady = 10)

    subscriptions = Button(window, text="subscriptions",
                           command=lambda: opensub("https://www.youtube.com/feed/subscriptions"),
                           fg="Black")
    subscriptions.grid(row=1, column=3, padx = 10, pady = 10)

    Originals = Button(window, text="Originals", command=lambda: openoriginal("https://www.youtube.com/originals"),
                       fg="Black")
    Originals.grid(row=3, column=0, padx = 10, pady = 10)

    game = Button(window, text="Gaming", fg="Black",
                  command=lambda: opengaming("https://www.youtube.com/gaming"))
    game.grid(row=3, column=3, padx = 10, pady = 10)

    Trending = Button(window, text="Trending", fg="Black",
                      command=lambda: opentrend("https://www.youtube.com/feed/trending"))
    Trending.grid(row=5, column=0, padx = 10, pady = 10)

    Movies = Button(window, text="YouTube Movies", fg="Black",
                    command=lambda: openymovies('https://www.youtube.com/feed/storefront?bp=ogUCKAI%3D'))
    Movies.grid(row=5, column=3, padx = 10, pady = 10)

    Fashion = Button(window, text="Fashion and Beauty", fg="Black",
                     command=lambda: openfash('https://www.youtube.com/channel/UCrpQ4p1Ql_hG8rKXIKM1MOQ'))
    Fashion.grid(row=7, column=0, padx = 10, pady = 10)

    Library = Button(window, text="Library", fg="Black",
                     command=lambda: openlib('https://www.youtube.com/feed/library'))
    Library.grid(row=7, column=3, padx = 10, pady = 10)

    History = Button(window, text="History", fg="Black",
                     command=lambda: openhist('https://www.youtube.com/feed/history'))
    History.grid(row=9, column=0, padx = 10, pady = 10)

    watchlaer = Button(window, text="watchlater", fg="Black",
                       command=lambda: openwatchlater('https://www.youtube.com/feed/history'))
    watchlaer.grid(row=9, column=3, padx = 10, pady = 10)


window.mainloop()



