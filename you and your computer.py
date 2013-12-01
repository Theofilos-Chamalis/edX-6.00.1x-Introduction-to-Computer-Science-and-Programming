def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    def displayHand2(hand):
      displayed = ''
      for letter in hand.keys():
            for j in range(hand[letter]):
                 displayed += letter + ' '
      return displayed
    hand = False
    while True:
      ans = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
      if ans == "n":
        hand = dealHand(HAND_SIZE)

        tester1 = True
        while tester1:
          ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
          if ans2 == "u":
            playHand(hand, wordList, HAND_SIZE)
            tester1 = False
          elif ans2 == "c":
            compPlayHand(hand, wordList, HAND_SIZE)
            tester1 = False
          else:
            print "Invalid command."
      elif ans == "r":
        if hand:
          ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
          if ans2 == "u":
            playHand(hand, wordList, HAND_SIZE)
          elif ans2 == "c":

            compPlayHand(hand, wordList, HAND_SIZE)
          else:
            print "Invalid command."
        else:
          print "You have not played a hand yet. Please play a new hand first!"
      elif ans == "e":
        break
      else:
        print "Invalid command."
