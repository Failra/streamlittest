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
            if playerOneGuess > ranNumber:
                st.write_stream("Number is too high")
                playerOneTurn += 1
                st.write_stream("")
                if currentPlayer == playerOne:
                    currentPlayer = playerTwo
            elif playerOneGuess < ranNumber:
                st.write_stream("Number is too low")
                st.write_stream("")
                playerOneTurn += 1
                if currentPlayer == playerOne:
                    currentPlayer = playerTwo
            else:
                st.write_stream("Congrats", playerOneName +", you guessed the number")
                correctGuess = True
                playerOneWins += 1
                
        if currentPlayer == 2:
            playerTwoGuess = st.text_input(playerTwoName + ", Guess a number: ")
            if playerTwoGuess > ranNumber:
                st.write_stream("Number is too high")
                st.write_stream("")
                playerTwoTurn += 1
                if currentPlayer == playerTwo:
                    currentPlayer = playerOne
            elif playerTwoGuess < ranNumber:
                st.write_stream("Number is too low")
                st.write_stream("")
                playerTwoTurn += 1
                if currentPlayer == playerTwo:
                    currentPlayer = playerOne
            else:
                st.write_stream("Congrats", playerTwoName +", you guessed the number")
                correctGuess = True
                playerTwoWins += 1
    
    if correctGuess == False:
        st.write_stream("You both are LOSERS!")

# Could add function here, triggers after three rounds of games. results() for example. 

if playerOneWins > playerTwoWins:
    st.write_stream("")
    st.write_stream("In total,", playerOneName, "wins! They won the most rounds")
    st.write_stream("")
elif playerTwoWins > playerOneWins:
    st.write_stream("")
    st.write_stream("In total,", playerTwoName, "wins! They won the most rounds")
    st.write_stream("")
else:
    st.write_stream("")
    st.write_stream("In total, players draw!")
    st.write_stream("")

st.write_stream("Done")
