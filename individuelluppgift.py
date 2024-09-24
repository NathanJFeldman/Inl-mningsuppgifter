import random, sys, time

class Blackjack:
    def __init__(self, deck:dict, rules:str, exit:str):
        #Kortspelet
        self.deck = {1: "Hearts : A",
                    2 : "Hearts : 2",
                    3 : "Hearts : 3",
                    4 : "Hearts : 4",
                    5 : "Hearts : 5",
                    6 : "Hearts : 6",
                    7 : "Hearts : 7",
                    8 : "Hearts : 8",
                    9 : "Hearts : 9",
                    10 : "Hearts : 10",
                    10 : "Hearts : Jack",
                    10 : "Hearts : Queen",
                    10 : "Hearts : King", 
                    1: "Spade : A",
                    2 : "Spade : 2",
                    3 : "Spade : 3",
                    4 : "Spade : 4",
                    5 : "Spade : 5",
                    6 : "Spade : 6",
                    7 : "Spade : 7",
                    8 : "Spade : 8",
                    9 : "Spade : 9",
                    10 : "Spade : 10",
                    10 : "Spade : Jack",
                    10 : "Spade : Queen",
                    10 : "Spade : King",
                    1: "Clubs : A",
                    2 : "Clubs : 2",
                    3 : "Clubs : 3",
                    4 : "Clubs : 4",
                    5 : "Clubs : 5",
                    6 : "Clubs : 6",
                    7 : "Clubs : 7",
                    8 : "Clubs : 8",
                    9 : "Clubs : 9",
                    10 : "Clubs : 10",
                    10 : "Clubs : Jack",
                    10 : "Clubs : Queen",
                    10 : "Clubs : King",
                    1: "Diamonds : A",
                    2 : "Diamonds : 2",
                    3 : "Diamonds : 3",
                    4 : "Diamonds : 4",
                    5 : "Diamonds : 5",
                    6 : "Diamonds : 6",
                    7 : "Diamonds : 7",
                    8 : "Diamonds : 8",
                    9 : "Diamonds : 9",
                    10 : "Diamonds : 10",
                    10 : "Diamonds : Jack",
                    10 : "Diamonds : Queen",
                    10 : "Diamonds : King"}
    def UI(self):
        print("-~-~-~Menu-~-~-~")
        Chosen = input("Decide what to do:\n1. Start game\n2. Rules\n3. Exit game\n\nChoose: ") #Här kan spelaren välja vad hen ska göra
        if Chosen == 1: #Börjar spelet
            #game()
            pass
        elif Chosen == 2: #Visar regler för blackjack
            #rules()
            pass
        elif Chosen == 3: #Stänger av spelet
            #exit
            pass
        else: #Spelar om spelet om man inte har angett ett korrekt svar
            #rerun function
            pass

    def game(self):
        #Funktionen game är självaste spelet där spelaren väljer kort
        player_turn = 0
        dealer_turn = 0
        turn = 0
        while player_turn or dealer_turn > 21:
            if turn == 0:
                player_turn + random.choice(list(self.deck.items))
                turn += 1
            elif turn == 1:
                dealer_turn + random.choice(list(self.deck.items))
                turn -= 1

    def game_rules(self):
        #I denna funktion visas reglerna för spelaren
        self.rules = print("~-~-~-REGLER-~-~-~\n-Meningen med spelet är att komma så nära 21 som möjligt.\n\n-Du kommer börja med att få två kort ifrån kortleken\n\n-När du fått dina kort får du bestämma om du ska stanna eller hitta\n\n-hitta betyder att du tar ett till kort\n\n-Om du stannar är du nöjd med ditt nummer\n\n-Om dealern får lägre en dig eller högre än 21 vinner du (samma gäller för dig)\n~-~-~-~-~-~-~-~-")

    def exit_game(self):
        print("Are you sure you want to exit the game?")
        self.exit = input("yes/no: ")
        if self.exit == "yes":
            sys.exit()
        elif self.exit == "no":
            print("Rerunning the program...")
            time.sleep(3)
            #game()
            pass
        else:
            pass

        

#Blackjack.game(self)