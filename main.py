import random

name = []

while True:
    nama = input("Enter participant Name or enter 'spin' to start the lucky draw : ")
    nama = nama.upper()

    if nama == "SPIN":
        if name:
            while True:
                print("-------------------------------------")
                AskUser = input("Press Q to quit or any key to spin: ")
                print("-------------------------------------")
                AskUser = AskUser.upper()

                if AskUser == 'Q':
                    break
                else:
                    if name:
                        random_name = random.choice(name)
                        name.remove(random_name)
                        print("You rolled:", random_name)
                        if not name:
                            print("No more names to roll.")
                            break
                    else:
                        print("No names available to spin.")
                        break
        else:
            print("No names available to spin.")
            break
        break
    else:
        name.append(nama)
