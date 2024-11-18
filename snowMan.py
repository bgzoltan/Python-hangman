import turtle
import time
import drawSnowMan

# create a canvas
myScreen = turtle.Screen()

# window size
myScreen.setup(width=800, height=600) 
# initializing turtle windows (layers) in order the specified part of the screen can be clearable
inputsTurtle=turtle.Turtle()
lettersTurtle=turtle.Turtle()
drawingTurtle=turtle.Turtle()
inputsTurtle.hideturtle()
drawingTurtle.hideturtle()
lettersTurtle.hideturtle()

# snowman position
startPosX=0
startPosY=-100

letterWidth=30 # the width of a letter to calculate positions when drawing them

# move turtle to a specified position on different turtles 
def drawMoveTo(x=0,y=0):
    drawingTurtle.penup()
    drawingTurtle.goto(startPosX+x,startPosY+y)
    drawingTurtle.pendown()

def inputsMoveTo(x=0,y=0):
    inputsTurtle.penup()
    inputsTurtle.goto(startPosX+x,startPosY+y)

def lettersMoveTo(x=0,y=0):
    lettersTurtle.penup()
    lettersTurtle.goto(startPosX+x,startPosY+y)

# display errors
def handleError(error):
    inputsMoveTo(0,-100)
    inputsTurtle.write(f'Error - {error}',move='False',align="center", font=("Arial", 16, "bold"))
    time.sleep(3)
    inputsTurtle.clear()

def theLetterInput():
    while (True):
        try:
            wordInputPl2=turtle.textinput("Player 2", "Please enter a letter:")
            if len(wordInputPl2)==1:
                if wordInputPl2 in ['0','1','2','3','4','5','6','7','8','9']:
                    raise ValueError("Please don't enter numbers!")
                else:
                    return wordInputPl2
            else:
                raise ValueError('Please enter only one character!')
        except ValueError as error:
               handleError(error)

def displayLetter(inputLetter):
        # print all same letters
        noOfsameCharacters=0
        while(True):
            try:
                letterPosition=wordLetters.index(inputLetter)
                wordLetters[letterPosition]='0' # in order not to find the letter next
                noOfsameCharacters+=1
                lettersMoveTo(startPosOfLetterPlaces+letterPosition*letterWidth,-150)
                lettersTurtle.penup()
                lettersTurtle.write(inputLetter,move='False',align="center", font=("Arial", 36, "normal"))
            except:
                pass
                break
        return noOfsameCharacters

def displayLetterPositions():
        startPosOfLetterPlaces=-len(wordLetters)*letterWidth/2
        for index in range(len(wordLetters)):
            lettersMoveTo(startPosOfLetterPlaces+index*letterWidth,-150)
            lettersTurtle.penup()
            lettersTurtle.write('_',move='False',align="center", font=("Arial", 36, "normal"))

# main
while (True):
    hits=0
    badHits=0
    turns=0
    wordLetters=[]
    
    # Title
    drawMoveTo(0,320)
    drawingTurtle.write("Snowman Game in Python", align="center", font=("Arial", 26, "bold"))

    # word input for Player1
    wordInputPl1=turtle.textinput("Player 1", "Please enter a word that player2 has to find out:")
    wordLetters=list(wordInputPl1.upper())
    displayLetterPositions()
    startPosOfLetterPlaces=-len(wordLetters)*letterWidth/2

    while(True):
        # input letter for Player2
        inputLetterPl2=theLetterInput()
        turns+=1
        if (inputLetterPl2.upper() in wordLetters)==True:
            hits+=displayLetter(inputLetterPl2.upper())
        else:
            badHits+=1
            drawSnowMan.drawSnowMan(badHits, drawMoveTo,drawingTurtle)

        if (hits==len(wordLetters)):
            winText=f'😀 Congratulations! You won the game in {turns} turns.'
            inputsMoveTo(-len(winText)/2,-100)
            inputsTurtle.write(winText,move='False',align="center", font=("Arial", 24, "bold"))
            break

        if (badHits>10):
            lostText='😥 Unfortunately You lost the game!'
            inputsMoveTo(len(lostText)/2,-100)
            inputsTurtle.write(lostText,move='False',align="center", font=("Arial", 24, "bold"))
            break

    inputYesOrNo=''
    while(True):
        inputYesOrNo=turtle.textinput("Would you like to play a new game?","y/n")
        inputsTurtle.clear()
        lettersTurtle.clear()
        drawingTurtle.clear() 
        if (inputYesOrNo in 'yYnN'):
            break

    if (inputYesOrNo in 'nN'):
        endText='You exited from Snowman game. 👋 See you later!'
        inputsMoveTo(len(endText)/2,100)
        inputsTurtle.write(endText,move='False',align="center", font=("Arial", 24, "bold"))
        time.sleep(5)
        break
    else:
        drawingTurtle.reset()
        drawingTurtle.hideturtle()


