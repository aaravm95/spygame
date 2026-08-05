import random


def phase2():
    print("------------------------------------------------------------------")
    print("You finally get to the control room...")
    print("You scan the room for threats...")
    print("You encounter the evil mastermind!")
    print("He says You want to stop me from launching that bomb?!")
    print("Then you have to stop me!!!")

    playerHealth = 100
    mastermindHealth = 100

    print("Playerhealth", playerHealth)
    print("evilMastermind health:", mastermindHealth)
    print("The evil mastermind attacks")
    playerHealth -= random.randint(5, 20)

    while playerHealth > 0 and mastermindHealth > 0:
        attack = input("press a to attack:")

        if attack == "a":
            mastermindHealth -= random.randint(10, 20)
            print("You have attacked")
            print("Playerhealth", playerHealth)
            print("evilMastermind health:", mastermindHealth)

            if mastermindHealth <= 0:
                print("Winner: Player!!!")
                break

            if random.randint(1, 2) == 1:
                print("the evil mastermind has attacked!!!")
                playerHealth -= random.randint(20, 30)
                print("Playerhealth", playerHealth)

                if playerHealth <= 0:
                    print("Winner: evil mastermind!!!")
                    print("You lose")
                    break


def entrance():
    print("You arrived at the entrance.")
    entrancePathways = input("You see two pathways: right or left: ").lower()
    if entrancePathways == "right" or entrancePathways == "r":
        print("You go right")
        print("you see lots of lazers ahead you")
        print("You also see a keypad")
        keypad_or_lasers = input("What do you do use the keypad or dodge the lasers?")
        if keypad_or_lasers == "laser" or keypad_or_lasers == "l" or keypad_or_lasers == "d" or keypad_or_lasers == "dodge":
            print("You accidentally touch a laser and alarm goes off. ")
            print("You run out of the building.")
            lasercon = input("you see a trapdoor and a door that says EXIT. Which one do you go through???")
            if lasercon == "d" or lasercon == "door":
                print("You go through the door. You see 25 guards waiting to kill you on the other side.")
                print("you DIED.")

            elif lasercon == "trapdoor" or lasercon == "t":
                print(
                    "You go through the trapdoor after an hour of walking, you finally walk up and start back at the entrance")
                entrance()
        elif keypad_or_lasers == "k" or keypad_or_lasers == "keypad":
            password = input("ENTER THE PASSWORD")
            if password == "510":
                phase2()

    elif entrancePathways == "left" or entrancePathways == "l":
        print("You go left...")
        print("You encounter a robot with a gun")
        FightRun = input("Fight or run???")

        if FightRun == "f" or FightRun == "fight":
            print("You rapidly punch the robot")
            print("It eventually breaks")
            dimoansteal = input("you see a diamond do you take it???")

            if dimoansteal == "y" or dimoansteal == "yes":
                print("It was a trap!!! You fall into an endless room.")

            elif dimoansteal == "n" or dimoansteal == "no":
                print("You go on without it...")
                print("You see a door with a keypad you decide to use it...")
                password1 = input("ENTER THE PASSWORD")

                if password1 == "510":
                    print("Door is unlocked")
                    phase2()

        elif FightRun == "r" or FightRun == "run":
            print("You run as fast as you can.The robot follows closely")
            keypad1 = input("You see a keypad.Do you use it???")

            if keypad1 == "y" or keypad1 == "yes":
                password2 = input("ENTER THE PASSWORD")

                if password2 == "510":
                    print("Door is unlocked")
                    lat2 = input("You see two last doors right or left")

                    if lat2 == "r" or lat2 == "right":
                        print("You escaped the robot You come closer to the villain...")
                        phase2()

                    elif lat2 == "l" or lat2 == "left":
                        print("you come to a dead end and the robot kills you GAMEOVER!!!")

                elif password2 != "510":
                    print("the robot corners you and kills you gameover!!!!!")

            elif keypad1 == "n" or keypad1 == "no":
                print("the robot corners you and kills you gameover!!!!!")


def intro():
    print("===========================")
    print("•-----------•☆☆☆☆☆•----------•")
    print(" -☆☆☆|SPY MISSION 1549|☆☆☆- ")
    print("•-----------•☆☆☆☆☆•----------•")
    print("===========================")

    print("You are a spy trying to stop an evil mastermind from launching a powerful nuclear bomb.")
    print("You must deactivate the bomb before the countdown reaches zero.")

    Choice1 = input(
        "Guards are protecting the entrance.\n"
        "Do you sneak past them or fight? "
    ).lower()

    if Choice1 == "s" or Choice1 == "sneak":
        Choice2 = input(
            "You sneak past the guards, but one gets alerted. "
            "Fight or run? "
        ).lower()

        if Choice2 == "f" or Choice2 == "fight":
            print("You knock the guard out cold. Luckily, none of the other guards noticed.")
            print("one of the drops a paper with the code 510 you might want to remember that...")
            entrance()
            return

        elif Choice2 == "r" or Choice2 == "run":
            print("All the guards are alerted! You run as fast as you can.")
            Choice3 = input(
                "You see two doors one on the right and one on the left: "
            ).lower()

            if Choice3 == "left" or Choice3 == "left door" or Choice3 == "l":
                print("You smash the left door open just before the guards catch you!")
                print("as you go through the hallway you see the code 510")
                entrance()

            elif Choice3 == "right" or Choice3 == "right door" or Choice3 == "r":
                print("You fall into a hidden trap. Game over!")

    elif Choice1 == "f" or Choice1 == "fight":
        print("You try to fight, but they lock you in a cell.")
        print("You see a vent and a rock.")

        Choice4 = input(
            "A guard with a key walks by. Do you throw the rock or climb through the vent? "
        ).lower()

        if Choice4 == "climb" or Choice4 == "c" or Choice4 == "v" or Choice4 == "vent":
            print("You climb through the vent.")
            print("You forgot an oxygen mask and faint from the toxic fumes.")
            print("Game over!")

        elif Choice4 == "throw rock" or Choice4 == "t" or Choice4 == "r":
            print("You throw the rock.")
            print("The guard gets knocked out. You grab the keys, open the cell, and run!")
            print("The guard drops a paper with the code 510 you might want to remember that...")
            entrance()


def main():
    intro()


main()