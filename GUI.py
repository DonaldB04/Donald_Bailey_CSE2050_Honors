import tkinter as tk
import random

#establishes the name if the tinker window
window = tk.Tk()

#creates labels for each name input
for i in range(16):
    tk.Label(window, text = 'Enter a name').grid(row = i)

#Creates text boxes to type names in
name1 = tk.Entry(window)
name2 = tk.Entry(window)
name3 = tk.Entry(window)
name4 = tk.Entry(window)
name5 = tk.Entry(window)
name6 = tk.Entry(window)
name7 = tk.Entry(window)
name8 = tk.Entry(window)
name9 = tk.Entry(window)
name10 = tk.Entry(window)
name11 = tk.Entry(window)
name12 = tk.Entry(window)
name13 = tk.Entry(window)
name14 = tk.Entry(window)
name15 = tk.Entry(window)
name16 = tk.Entry(window)

#places each entry box on the window
name1.grid(row = 0, column= 1)
name2.grid(row = 1, column= 1)
name3.grid(row = 2, column= 1)
name4.grid(row = 3, column= 1)
name5.grid(row = 4, column= 1)
name6.grid(row = 5, column= 1)
name7.grid(row = 6, column= 1)
name8.grid(row = 7, column= 1)
name9.grid(row = 8, column= 1)
name10.grid(row = 9, column= 1)
name11.grid(row = 10, column= 1)
name12.grid(row = 11, column= 1)
name13.grid(row = 12, column= 1)
name14.grid(row = 13, column= 1)
name15.grid(row = 14, column= 1)
name16.grid(row = 15, column= 1)

def getGuess():
    '''
    collects guesses and checks if they're wrong or right
    '''
    
    #guess one and two are collected
    one = guess1.get()
    two = guess2.get()

    #checks to see if the list containing the tuples of pairs has the guesses the user entered
    if (one, two) in list_pair:
        
        #correct
        list_pair.remove((one, two))
        tk.Label(text = 'Correct!').grid(row = 9, column = 5)
    
    elif (two, one) in list_pair:
        
        #correct
        list_pair.remove((two, one))
        tk.Label(text = 'Correct!').grid(row = 9, column = 5)
    
    else:
        
        #wrong
        tk.Label(text = 'Wrong! Guess Again').grid(row = 9, column = 5)

    if len(list_pair) == 0:
        
        #win
        tk.Label(text = 'Congratulations You Found All Pairs!').grid(row = 9, column = 5)

def getNames():
    '''
    collects names and puts them into a list to be randomized
    '''
    
    #globalizes variables for use outside of the function
    global names, list_pair, guess1, guess2, name_wid
    
    #collects all names
    a = name1.get()
    b = name2.get()
    c = name3.get()
    d = name4.get()
    e = name5.get()
    f = name6.get()
    g = name7.get()
    h = name8.get()
    i = name9.get()
    j = name10.get()
    k = name11.get()
    l = name12.get()
    m = name13.get()
    n = name14.get()
    o = name15.get()
    p = name16.get()

    #puts names into a list               
    names = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
    
    #shows a label with all the entered names for easier guessing
    name_wid = tk.Label(text= f' Your Options {names}')
    name_wid.grid(row = 0, column = 5)

    #randomize the list of names into tuple pairs
    list_pair = []
    for i in range(8):
        person1 = names.pop(random.randrange(len(names)))
        person2 = names.pop(random.randrange(len(names)))
        pair = (person1, person2)
        list_pair.append(pair)

    #creates label tleling he user to guess
    guess_wid = tk.Label(text = 'Guess A Pair')
    guess_wid.grid(row = 6, column = 5)
    
    #creates boxes to enter guesses
    guess1 = tk.Entry(window)
    guess2 = tk.Entry(window)

    #places the boxes to enter guesses in the window
    guess1.grid(row = 7, column = 4)
    guess2.grid(row = 7, column = 6)

    #gives a button to submit guesses
    guess_button = tk.Button(window, text = 'Submit Guess', command = getGuess)
    guess_button.grid(row = 8, column = 5)

#gives a button to submit names
button = tk.Button(window, text = 'Enter', command = getNames)
button.grid(row = 16)

#runs the apps
window.mainloop()