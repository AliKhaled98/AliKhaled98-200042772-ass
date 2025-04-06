
# representing the token codes & token types 
LETTER = 0   
DIGIT = 1
UNKNOWN = 99


INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

# The Global Variables to use in the analyzer
charClass = None
lexeme = ""
nextChar = ''
lexLen = 0
nextToken = None
in_fp = None
line = ""
lineIndex = 0

# addChar is a function that add the next character to the lexeme
def addChar():
    global lexeme, lexLen, nextChar  # identify the lexeme, lexlen and nextChar as global variables
    if lexLen <= 98: # Checks if the lenglth of the lexeme is less than  or equal 98
        lexeme += nextChar # adds the next character to current lexeme
        lexLen += 1 # increase the lexeme length by 1
    else:
        print("Error - lexeme is too long")  # prints error message if the length of the lexeme is greater thatn 98

# getChar is a function that gets the next input character and identifies its class
def getChar():
    global nextChar, charClass, lineIndex, line  # identify the nextChar, charClass, lineIndex and line as global variables
    if lineIndex < len(line): # Checks if the lineIndex is lesss than the length of the line 
        nextChar = line[lineIndex] # Assigns the value of the line at the lineIndex to nextChar
        lineIndex += 1 # increase the lineIndex by 1
        if nextChar.isalpha(): # Checks if teh nextChar is an alphabetic
            charClass = LETTER  # Assign charClass as letter
        elif nextChar.isdigit(): # Checks if the nextChar is a digit
            charClass = DIGIT # Assign charClas as digit
        else: # checks if the case is not one of the above 
            charClass = UNKNOWN # Assigns the charclass as unknown
    else: # If the lineIndex is not less than the line length
        nextChar = ''  # Sets the nexchar as an empty space or string
        charClass = EOF # Sets the charclass as EOF

# getNonnBlank funciton is a function to get the white space characters and skip it or ignore it
def getNonBlank(): 
    while nextChar.isspace():  # Checks While the next character is a space
        getChar() # call the getChar function to get the next character and skip the white space characters

# lookup is a function that is used to 'lookup' for if the character is operators or paranthesis to return its token    
def lookup(ch):
    global nextToken # identify the nextToken as a global variable
    if ch == '(': # Checks if the character is a left paranthesis
        addChar() # Adds this character to the lexeme
        nextToken = LEFT_PAREN # assigns the next token type as a left parantheses
    elif ch == ')':  # Checks if the character is a right paranthesis
        addChar() # Add this character to the lexeme
        nextToken = RIGHT_PAREN # assigns the next token type as a right paranthesis
    elif ch == '+': # checks if the character is a plus sign or a plus operator
        addChar()  # adds this character to the lexeme
        nextToken = ADD_OP # assigns the next token type as a plus operator
    elif ch == '-': # checks if the character is a minus sign or a minus operator 
        addChar() # adds this character to the lexeme
        nextToken = SUB_OP # assigns the next token type as a minus operator
    elif ch == '*': # checks if the character is a multiplication sign or a multiplication operator
        addChar() # add this character to the lexeme
        nextToken = MULT_OP # assigns the next token type as a multiplication operator
    elif ch == '/': # checks if the character is a division sign or a division operator
        addChar() # adds this character to the lexeme
        nextToken = DIV_OP # assigns the next token type as a division operator
    elif ch == '=': # checks if the character is an assignment operator
        addChar() # adds this character to the lexeme
        nextToken = ASSIGN_OP # assigns the next token type as an assignment operator
    else: # if the character is none of the cases above
        addChar() #adds this character to the lexeme
        nextToken = EOF # assigns the next token type as EOF (End of file) token
    return nextToken # returns the token type

# lex ia the function in the code the does the lexical analysis
def lex():
    global lexeme, lexLen, nextToken # identify lexeme, lexLen and nextToken as global variables
    lexeme = "" # sets the lexeme as an empty string or space
    lexLen = 0 # sets the length of the lexeme to 0
    getNonBlank() # skips any space or white space characters

    if charClass == LETTER: #checks if the charclass is a letter
        addChar() # adds this letter to the lexeme
        getChar() # gets the next character 
        while charClass in (LETTER, DIGIT):  # while the class of the character is a letter or digit
            addChar() # adds this character to the lexeme
            getChar() # gets the next character 
        nextToken = IDENT # sets the token type as an identifier

    elif charClass == DIGIT: # checks if the class of the character is a digit
        addChar() # adds this character to digit to the lexeme
        getChar() # gets the next character or digit
        while charClass == DIGIT: # while the class of the character is a digit
            addChar() # adds this character to the lexem
            getChar() # gets the next character
        nextToken = INT_LIT  # set the token type as int_lit (integer literal)

    elif charClass == UNKNOWN: # if the class of the character is unknown
        lookup(nextChar) # calls the lookup function for the character 

    elif charClass == EOF: # if the character class is EOF
        nextToken = EOF # sets the token type as EOF
        return EOF # returns EOF

    print(f"Next token is: {nextToken}, Next lexeme is {lexeme}") # prints the lexeme and its token
    return nextToken # returns the token type


def main(): # The main function
    global in_fp, line, lineIndex # identify the in_fp, line and lineIndex as global variables
    try: # try is used to handle the errors or exceptions using the except 
        with open("front.in", "r") as in_fp: # open the file front.in
            for line in in_fp: # iterate in each line in the file
                line = line.strip() # removes the white space character in the line
                lineIndex = 0 # sets the line index to 0
                if not line: # checks if the line is empty
                    continue # skip
                getChar() # gets the first character in the line
                while nextToken != EOF: # continue iterating until the token type is EOF
                    lex() # calls the lex function to perform the lexical analysis
    except FileNotFoundError: # if there is no file or not found
        print("ERROR - cannot open front.in") # prints error message


if __name__ == "__main__": # to run the main function or the program
    main()
