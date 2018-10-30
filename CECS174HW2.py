# import math functions to use sqrt
import math

# define a function to print the menu to be displayed to user
def print_menu():
    # print each menu option from 1-3
    print("1. Check a palindrome")
    print("2. Check a word square")
    print("3. Quit")

# define a function to get a menu choice from the user and validate the choice
def get_menu_choice():
    # ask user for menu choice
    choice = input("Please choose one of the functions from the list above: ")
    # validate user's choice and re ask if input invalid
    while (choice != '1') and (choice != '2') and (choice != '3'):
        choice = input("Please choose one of the functions from the list above: ")
    # return the user's choice
    return choice

# define a function to get input 'phrase' from the user
# validate that at least one char entered
def get_phrase():
    # get user input for phrase
    phrase = input("Please enter an English phrase: ")
    # validate phrase
    while phrase == "":
        phrase = input("Please enter an English phrase: ")
    # return phrase
    return phrase

# define a function to find whether string input is a palindrome
def is_palindrome(phrase):
    # set counters i and j
    i = 0
    j = len(phrase) - 1
    # loop while i is less than j
    while i < j:
        # check that char at index [i] is alpha
        for x in range(0, len(phrase)):
            # if char at index [i] is not alpha, increment i until it is
            if not phrase[i].isalpha():
                # increment i
                i += 1
                if i > j:
                    return True
            # increment counter x for 'for loop'
            x += 1
        # check that char at index [j] is alpha
        for y in range(len(phrase) - 1, 0, -1):
            # if char at index [j] is not alpha, decrement j until it is
            if not phrase[j].isalpha():
                # decrement j
                j -= 1
            # increment counter y for 'for loop'
            y += 1
        # check to see if chars at indexes [i] and [j] match,
        # if not, phrase is not a palindrome, so return false
        if phrase.lower()[i] != phrase.lower()[j]:
            # return False
            return False
        # increment i
        i += 1
        # decrement j
        j -= 1
    # if you have made it this far, phrase is a palindrome, return True
    return True

# define a function to implement menu option 1
def menu_check_palindrome():
    # get user phrase and store it in 'user_phrase'
    user_phrase = get_phrase()

    # if user_phrase is a palindrome, print it and say it is a palindrome
    if is_palindrome(user_phrase):
        # print 'user_phrase is a palindrome'
        print("%s is a palindrome" %user_phrase)
    # else user_phrase is not a palindrome, print it and say not
    else:
        # print 'user_phrase is not a palindrome'
        print("%s is not a palindrome" %user_phrase)

# define a function to get a word square from the user
def get_word_square():
    # declare variable to hold word_square and get first line from user
    word_square = input("Please enter the first line of the word square: ")
    # the order of the word square = to the length of the first line
    order = len(word_square)
    # set up counter i
    i = 1
    # loop while i <= order - 1
    while i <= order - 1:
        # concatenate word_square with the remaining lines of the square
        word_square = word_square + input("Please enter the next line of the word square: ")
        # increment i for while loop
        i += 1
    # once you have received all of the lines, return the word_square
    return word_square

# define a function to check whether input is a word square or not
def is_word_square(square):
    # N is == order of the square
    N = int(math.sqrt(len(square)))
    # m is a counter coefficient
    m = 1
    # i is a counter
    i = 0
    # while i is less than N
    while i < N:
        # set up variable line that temporarily holds the string located at
        # Row i
        # split string square from index (N*i) to (N*m)
        # ex: for the first iteration
        # i = 0, m = 1, N = 4 (order 4 word square)
        # line = square[(4)*(0):(4)*(1)] = square[0:4]
        line = square[N*i:m*N]
        # declare a counter j
        j = 0
        # declare a variable column to temp hold string column
        column = ''
        # for using counter j, from j to N
        for j in range(N):
            # concatenate column with each char at position 'square[j*N+i]
            # ex: for N = 4
            # column = column + square[0*4+0] = column + square[0]
            column = column + square[j*N+i]
            # increment j for 'for loop'
            j += 1
        # increment i for 'while loop'
        i += 1
        # increment m for line function
        m += 1
        # check word square
        # if completed line does not equal completed column, return False
        if line != column:
            # return False
            return False
    # if you've made it here, line == column, it is a word square, return True
    return True

# define a function to implement menu option 2
def menu_check_word_square():
    # get a word square from user and save it to 'user_square'
    user_square = get_word_square()
    # N is order of the word square
    N = int(math.sqrt(len(user_square)))
    # check if user_square is a word square
    if is_word_square(user_square):
        # if it is, print it to the screen
        # declare counters i, m, and j
        # i is for the for loop
        i = 0
        # m is for the end of the split
        m = N
        # j is for the beginning of the split
        j = 0
        # print user_square to screen in shape of a square
        for i in range(N):
            # split user_square from j to m and print the split
            print(user_square[j:m])
            # increment j by N
            j += N
            # increment m by N
            m += N
        # print that it is a word square
        print("is a word square!")
    # else if it is not a word square
    else:
        # print the imposter word square to the screen
        # declare counters i, m, and j
        # i is for the for loop
        i = 0
        # m is the end of the split
        m = N
        # j is the beginning of the split
        j = 0
        # print imposter square to the screen in the shape of a square
        for i in range(N):
            # split imposter square from j to m
            print(user_square[j:m])
            # increment j and m by N
            j += N
            m += N
        # print that it is an imposter
        print("is not a word square!")
        
# define main function to run everything!
def main():
    # prints the menu using 'print_menu()' function
    print_menu()
    print()
    # gets a menu choice from user using 'get_menu_choice()'
    # stores the user's menu choice in 'menu_choice'
    menu_choice = get_menu_choice()
    # loop program while menu_choice isn't 3 which would quit the program
    while menu_choice != '3':
        # if menu_choice is 1 run that program (check palindrome)
        if menu_choice == '1':
            menu_check_palindrome()
        # if menu_choice is 2 run that program (check word square)
        elif menu_choice == '2':
            menu_check_word_square()
        # if menu choice is 3 quit the program
        elif menu_choice == '3':
            quit()
        # reprint the menu with space before
        print()
        print_menu()
        # ask the user for the next menu choice
        print()
        menu_choice = get_menu_choice()

# call main function to execute program
main()


        
    
    
    



