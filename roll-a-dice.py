import random

response = "y"

while  response == "y":    
    no =  random.randint(1,6)

    if no ==1:
        print("[-----]")
        print("[  1  ]")
        print("[-----]")

    if no ==2:
        print("[-----]")
        print("[  2  ]")
        print("[-----]")

    if no ==3:
        print("[-----]")
        print("[  3  ]")
        print("[-----]")

    if no ==4:
        print("[-----]")
        print("[  4  ]")
        print("[-----]")

    if no ==5:
        print("[-----]")
        print("[  5  ]")
        print("[-----]")

    if no ==6:
        print("[-----]")
        print("[  6  ]")
        print("[-----]")

    response=input("Pressione y para jogar novemente e n para sair:")
    print("\n")