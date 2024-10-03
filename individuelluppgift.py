import random, sys, time
import pyinputplus # type: ignore

class Blackjack:
    def __init__(self, deck:list):
        #Kortspelet
        self.deck = deck

    def UI(self):
        print("-~-~-~Menu-~-~-~")
        print("Decide what to do:\n1. Start game\n2. Rules\n3. Exit game\n\nChoose: ")
        Chosen = pyinputplus.inputInt() #Här kan spelaren välja vad hen ska göra
        if Chosen == 1: #Börjar spelet
            self.game()
        elif Chosen == 2: #Visar regler för blackjack
            self.game_rules()
        elif Chosen == 3: #Stänger av spelet
            self.exit_game()

    def game(self): #Funktionen game är självaste spelet där spelaren väljer kort
        global dealer_hand
        dealer_hand = 0
        def A_changer1():
            while 1 in self.deck:
                self.deck[self.deck.index(1)] = 11
        def A_changer2():
            while 11 in self.deck:
                self.deck[self.deck.index(11)] = 1
        def player_turn(dealer_hand): #funktion som gör att spelaren tar kort och kan sluta ta kort.
            player_hand = 0 #spelarens hand står för vilken summa du har beroende på korten i handen
            player_hand += random.choice(self.deck) + random.choice(self.deck) #spelaren får två random kort i början
            print("TOTAL:",player_hand)
            while player_hand != 21 or take_card == "yes":
                card_hit = random.choice(self.deck) #random kort från kortleken
                print("Do you want to hit? ") #fråga om du vill ta kort eller standa alltså inte ta
                take_card = pyinputplus.inputYesNo()
                if take_card == "yes":
                    player_hand = player_hand + int(card_hit)
                    print(player_hand)
                    if player_hand > 21:
                        print("You bust")
                        summary(player_hand, dealer_hand)
                    elif player_hand == 21:
                        print("You got blackjack!")
                        dealer_turn(player_hand)
                    elif player_hand < 10:
                        A_changer1()
                    elif player_hand > 11:
                        A_changer2()
                elif take_card == "no":
                    print("You stand at: ", player_hand)
                    dealer_turn(player_hand)
        def end_game(): #Denna funktion är gjord för att fråga spelaren om man vill spela om
            print("Game ended, do you want to play again? ")
            replay = pyinputplus.inputYesNo() #yes no fråga om man vill stänga av eller köra om
            if replay.lower() == "yes" or "y":
                print("Replaying game...")
                time.sleep(3)
                self.game()
            elif replay.lower() == "no" or "n":
                print("Exiting game...")
                time.sleep(3)
                sys.exit()
        def dealer_turn(player_hand): #funktion för dealerns turn vilket är när hen tar kort och vinner eller får över
            dealer_hand = 0
            dealer_hand += random.choice(self.deck) #dealern får ett kort i början
            print("Dealer get his first card TOTAL:", dealer_hand)
            while dealer_hand < 21 or dealer_hand != 21:
                dealer_card_hit = random.choice(self.deck) #random kort från kortleken
                if dealer_card_hit == 1:
                    if dealer_hand <= 10:
                        A_changer1()
                    elif dealer_hand >= 11 and dealer_hand < 21:
                        A_changer2()
                dealer_hand = dealer_hand + int(dealer_card_hit)
                time.sleep(2)
                print("Dealer hits!")
                print("Dealer got: ", int(dealer_card_hit), "TOTAL:", dealer_hand)
                if dealer_hand > 21:
                    print("Dealer bust")
                    summary(player_hand, dealer_hand)
                elif dealer_hand == 21:
                    print("Dealer got blackjack!")
                    summary()
                elif dealer_hand >= 17 or dealer_hand < 21:
                    summary(player_hand, dealer_hand)
                elif dealer_hand == player_hand:
                    summary()
        def summary(player_hand, dealer_hand):
            print("---------Summary---------\n")
            if player_hand == dealer_hand:
                print("DRAW\n")
                print("-------------------------\n")
                end_game()
            elif player_hand > dealer_hand and player_hand <= 21:
                print("You won!\n")
                print("-------------------------\n")
                end_game()
            elif dealer_hand > player_hand and dealer_hand <= 21:
                print("Dealer won!\n")
                print("-------------------------\n")
                end_game()
            elif player_hand > 21:
                print("You lost do to being over 21")
                print("-------------------------\n")
                end_game()
            elif dealer_hand > 21:
                print("Dealer lost do to being over 21")
                print("-------------------------\n")
                end_game()
        player_turn(dealer_hand=dealer_hand)
    def game_rules(self):
        #I denna funktion visas reglerna för spelaren
        print("~-~-~-REGLER-~-~-~\n-Meningen med spelet är att komma så nära 21 som möjligt.\n\n-Du kommer börja med att få två kort ifrån kortleken\n\n-När du fått dina kort får du bestämma om du ska stanna eller hitta\n\n-hitta betyder att du tar ett till kort\n\n-Om du stannar är du nöjd med ditt nummer\n\n-Om dealern får lägre en dig eller högre än 21 vinner du (samma gäller för dig)\n~-~-~-~-~-~-~-~-")
        time.sleep(10)
        self.UI()
    def exit_game(self): #exit game funktion gör att är en del av menyn om det är så att man vill starta om spelet
        while True:
            print("Are you sure you want to exit the game?")
            self.exit = input("yes/no: ") #yes no fråga om man verkligen vill stänga av
            if self.exit == "yes":
                sys.exit()
            elif self.exit == "no":
                print("Rerunning the program...")
                time.sleep(3)
                self.game()

#folk är bara en variabel för att starta spelet och deck listan är så stor för att anpassa till ett helt kortspel samt typerna
folk = Blackjack(deck=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10])

folk.UI()