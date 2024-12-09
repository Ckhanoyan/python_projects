print('''
*******************************************************************************
      .======================================.
      | ___ ___ ___               _   _   _  |
      | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
      | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
      '===================================== ,sSSSs
                BOB'S FEAR HOLE             SSSS "(
           .:.                              SSS@ =/  \~/
          C|||'                             SSSS_(_  _Y_
        ___|||______________________________SS/ _)_) /.-
       [____________________________________] \   /\//
        |   ____    ____    ____    ____   | \|==(\_/
        |  (____)  (____)  (____)  (____)  | (/   ;
        |  |    |  |    |  |    |  |    |  | |____|
        |  |    |  |    |  |    |  |    |  |  \  |\
        |  |    |  |    |  |    |  |    |  |   ) ) )
        |  |____|  |____|  |____|  |____|  |  (  |/
        |  I====I  I====I  I====I  I====I  |  /\ |
       jgs |    |  |    |  |    |  |    |  | /.(=\
                                               Y\_\

*******************************************************************************
''')

print("Welcome to Town Center Market!")
print("Your mission is to find the Great Bob. You do not want to fall into Bob's hole first before you find him!")
choice1 = (input('You are approaching the bartender and see a bathroom. Which do you want to do first? Type "order" for ordering a beer first or "open" to open the bathroom door.')).lower()

if choice1 == "open":
  choice2 = (input('Bob is not in there! Keep looking, and where do you want to go next? Type "counter" to go the counter and ask for Bob or type "outside" to go outside and look for him.')).lower()
  if choice2 == "outside":
    choice3 = input('You are outside in the smoking area and see the Great Bob smoking a cigarette. He asks you if you want a cigarette. Type "yes" to join him or "no" to go back inside.').lower()
    if choice3 == "yes":
      print("You win! You found the Great Bob and he is happy to see you!")
    else:
      print("You fall into Bob's hole and die. Game over.")
  else:
    print("You got attacked by the Great Bob at the counter! Game over.")
else:
  print("Oh no! You decided to order a beer first so you will fall into Bob's drunk hole and Bob will place his hand on you. Game over.")
  
  
