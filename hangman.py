from turtle import *
from random import randint
import time

wordList = ['Adequate', 'Adversarial', 'Ambiguous', 'Benevolent', 'Clout', 'Coincide', \
            'Counterproductive', 'Disdain', 'Disparage', 'Egregious', 'Endow', 'Envy', \
            'Foment', 'Foreseeable', 'Ignominious', 'Irreconcilable', 'Melodramatic', \
            'Predecessor', 'Promulgate', 'Quirk', 'Unilateral', 'Ubiquitous']


sw = 600
sh = 800
s=getscreen()
s.setup(600, 800)
s.bgcolor('#012e77')
t=getturtle()
t.color('#ff0a33')
t.width(8)
t.hideturtle()
t.speed(9)

#second turtle
tWriter = Turtle()
tWriter.hideturtle()

tBadLetters = Turtle()
tBadLetters.hideturtle()

#things we need to play the game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayWord=""
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
fails = 6 #the number of guesses before you fail
fontS = 20
gameDone = False 

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto( -int(sw*0.4), -int(sh*0.375) )
    tWriter.write( newText, font=('Arial', fontS, 'bold') )

def displayBadLetters(newText):
    fontS = 30
    tBadLetters.color('white')
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto( -int(sw*0.4), int(sh*0.375) )
    tBadLetters.write( newText, font=('Arial', fontS, 'bold') )
    

def chooseWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("the secret word is:" + secretWord)

def makeDisplay():
    global displayWord, secretWord, lettersCorrect
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayText += letter + " "

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawLLeg()
    if fails == 2:
        drawRLeg()
    if fails == 1:
        drawArms()
    if fails == 0:
        drawHat()
    
    
def checkWordGuess():
    global gameDone
    boxTitle = "Guess the word Chief.."
    guess =  s.textinput(boxTitle, "Enter your guess for the word... ")
    if guess == secretWord:
        displayText("Chief good work ... This is it -> " + secretWord)
        gameDone = True
    else:
        displayText("Unfortunately..." + guess + " is indeed not it Chief..")
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangmanPerson()
        

def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:

        theGuess = getGuess()

        if theGuess == "$$":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("No.. " + theGuess + "Chief only guess 1 letter or guess the word...")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("I am sincerely sorry but..." + theGuess + " is not it chief")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess not in lettersWrong:
            displayText("Unfortunately..." + theGuess + " is indeed not it Chief..")
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("Not in word: {" + lettersWrong + "}") 
            time.sleep(1)
            displayText(displayWord)
            fails -= 1
            updateHangmanPerson()
        else:
            displayText("Sorry Chief you already guessed.. " + theGuess )
            time.sleep(1)
            displayText(displayWord)
        if fails <= 0:
            displayBadLetters("No more guesses Chief")
            displayText("Sorry Chief... You took the L... The Word is " + secretWord)
            gameDone = True
        if "_" not in displayWord:
            displayBadLetters("You got it Chief")
            gameDone = True 

def drawGallows():
    t.penup()
    t.setheading(0)
    t.goto(-int(sw*0.2), -int(sh*0.2) )
    t.pendown()
    t.forward(int(sw*0.6) )
    t.backward(int(sw*0.1) )
    t.left(90)
    t.forward(int(sw*0.7) )
    t.left(90)
    t.forward(int(sw*0.3) )
    t.left(90)
    t.forward(int(sw*0.1) )




def drawHead():
    hr = int(sw*0.07)
    t.penup()
    t.goto(t.xcor()-hr, t.ycor()-hr)
    t.pendown()
    t.circle(hr)
    t.penup()
    t.goto(t.xcor() + hr, t.ycor() -hr)
    
def drawTorso():
    t.pendown()
    t.forward(int(sw*0.19) )

def drawLLeg():
    t.pendown()
    t.left(45)
    t.forward(int(sw*0.17) )
    t.backward(int(sw*0.17) )

def drawRLeg():
    t.pendown()
    t.right(90)
    t.forward(int(sw*0.17) )
    t.backward(int(sw*0.17) )

def drawArms():
    t.pendown()
    t.right(135)
    t.forward(int(sw*0.09) )
    t.left(60)
    t.forward(int(sw*0.12) )
    t.backward(int(sw*0.12) )
    t.right(120)
    t.forward(int(sw*0.12) )
    t.backward(int(sw*0.12) )

def drawHat():
    t.left(60)
    t.penup()
    t.forward(int(sw*0.25) )
    t.pendown()
    t.left(90)
    t.forward(int(sw*0.15) )
    t.backward(int(sw*0.30) )
    t.forward(int(sw*0.09) )
    t.right(90)
    t.circle(36,180)
    
    
    



#Program begins here...

drawGallows()
drawHead()
drawTorso()
drawLLeg()
drawRLeg()
drawArms()
drawHat()

#start playing game
time.sleep(1)
t.clear()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Certainly Not It Chief: {" + lettersWrong + "}")
playGame()

