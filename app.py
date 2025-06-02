# I might come back and do the extra credit. If I don't, just ignore this. 
import streamlit as st
import random

st.write("This program gives you three tries to guess a random number. If the number you guess is too low or too high, you will be prompted to try again. If you guess it right, then the program ends.")

st.write("")

playerOneName = st.text_input("Player 1, enter a name: ")
playerTwoName = st.text_input("Player 2, enter a name: ")
playerOneWins = 0
playerTwoWins = 0
    
st.write("")

for x in range(1,4):
    ranNumber = random.randint(1,10)
    playerOne = 1
    playerTwo = 2
    currentPlayer = 1
    playerOneTurn = 0
    playerOneGuess = 0
    playerTwoTurn = 0
    playerTwoGuess = 0
    correctGuess = False
    
    st.write("")
    st.write("Game", x)
    st.write("")
    
    # Could create function here. playerOneGuess() and playerTwoGuess(). Switching off on turns
    
    while playerOneTurn < 3 and playerTwoTurn < 3 and playerOneGuess != ranNumber and playerTwoGuess != ranNumber:
        if currentPlayer == 1:
            playerOneGuess = st.text_input(playerOneName + ", Guess a number: ")
            if int(playerOneGuess) > int(ranNumber):
                st.write("Number is too high")
                playerOneTurn += 1
                st.write("")
                if currentPlayer == playerOne:
                    currentPlayer = playerTwo
            elif int(playerOneGuess) < int(ranNumber):
                st.write("Number is too low")
                st.write("")
                playerOneTurn += 1
                if currentPlayer == playerOne:
                    currentPlayer = playerTwo
            else:
                st.write("Congrats", playerOneName +", you guessed the number")
                correctGuess = True
                playerOneWins += 1
                
        if currentPlayer == 2:
            playerTwoGuess = st.text_input(playerTwoName + ", Guess a number: ")
            if int(playerTwoGuess) > int(ranNumber):
                st.write("Number is too high")
                st.write("")
                playerTwoTurn += 1
                if currentPlayer == playerTwo:
                    currentPlayer = playerOne
            elif int(playerTwoGuess) < int(ranNumber):
                st.write("Number is too low")
                st.write("")
                playerTwoTurn += 1
                if currentPlayer == playerTwo:
                    currentPlayer = playerOne
            else:
                st.write("Congrats", playerTwoName +", you guessed the number")
                correctGuess = True
                playerTwoWins += 1
    
    if correctGuess == False:
        st.write("You both are LOSERS!")

# Could add function here, triggers after three rounds of games. results() for example. 

if playerOneWins > playerTwoWins:
    st.write("")
    st.write("In total,", playerOneName, "wins! They won the most rounds")
    st.write("")
elif playerTwoWins > playerOneWins:
    st.write("")
    st.write("In total,", playerTwoName, "wins! They won the most rounds")
    st.write("")
else:
    st.write("")
    st.write("In total, players draw!")
    st.write("")

st.write("Done")
