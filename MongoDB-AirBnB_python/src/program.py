from colorama import Fore
import program_guests
import program_hosts
import data.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()

    print_header()

    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()
            else:
                program_hosts.run()
    except KeyboardInterrupt:
        return


def print_header():
    snake = \
        """
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:**..++++++..**:,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::.+SSSS...........S+.,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.SSSSSSSS..............SS:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.SSSSSSSS..............SS:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+SSSSSSSSS................S:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:SSSS+*:+SS.................+,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.SS++,@@,+S.................S*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.SS++@@@@*S...................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@,+SS++,@@@.S..................+,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@,+SSSSSSSSSS..................+,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.............++.............+,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,...............+,@,,,,@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,...............+,@,,,,@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@,*..++++++++++++++++++++SS.............+,,:::::::,,@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@*+SSSSSSSSSSSSSSSSSSSS..................+,::::::::::,@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@,*SSSSSSSSSSSSSSSSSSSSSS..................+,:::::::::::,@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@*SSSSSSSSSSSSSSSSSSSSSSS..................+,::::::::::::@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@,+SSSSSSSSSSSSSSSSSSSSSSSS...................,:::::::::::*:@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@,SSSSSSSSSSSSSSSSSSSSSSSSS..................*,:::::::::::*:,@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@:SSSSSSSSSSSSSSSSSSSSSSSSS.................S:,:::::::::::**,@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@*SSSSSSSSSSSSSSSSSSSSSSSSS..................@::::::::::::**,@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@*SSSSSSSSSSSSSSSSSSSSSSSSS..................@::::::::::::**,@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@.SSSSSSSSSSSSSSSSSSSSSSSSS................+,,::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@+SSSSSSSSSSSSSSSSSSSSSSSSS.............S..,,:::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@+SSSSSSSSSSSSSSSSSSSS+................:,@@,::::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@+SSSSSSSSSSSSSSSSS**,,@@@@@@@@@@@@@@@@,,:::::::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@+SSSSSSSSSSSSSSS+:@@,,:::::::::::::::::::::::::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@.SSSSSSSSSSSSSS+,,:::::::::::::::::::::::::::::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@.SSSSSSSSSSSSSS:,::::::::::::::::::::::::::::::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@*SSSSSSSSSSSSS*@,::::::::::::::::::::::::::::::::::::::::**:@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@:SSSSSSSSSSSSS,,:::::::::::::::::::::::::::::::::::::::::**,@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@,SSSSSSSSSSSS+,,:::::::::::::::::::::::::::::::::::::::::*:,@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@*SSSSSSSSSSS+,:::::::::::::::::::::::::::::::::::::::::::,@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@,SSSSSSSSSSS+,:::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@*SSSSSSSSSS+,::::::::::::::::::::::::::::::::::::::::::,@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@,.SSSSSSSSS+,::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@*SSSSSSSS+,:::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@,:**....*,::::::::::::::::::::::::::::::::::::::,,@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::::::::::,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::,@@,:::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:::::::::::::::::::,@@@@:::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:::::::::::::::::::,@@@@::::,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,::::::::::::::::::::,@@,::::,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,::::::::::::::::::::,,::::,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,::::::::::::::::::::,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,::::::::::::::::,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,:::::::,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        """

    print(Fore.WHITE + '****************  SNAKE BnB  ****************')
    print(Fore.GREEN + snake)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Snake BnB!")
    print("Why are you here?")
    print()


def find_user_intent():
    print("[g] Book a cage for your snake")
    print("[h] Offer extra cage space")
    print()
    choice = input("Are you a [g]uest or [h]ost? ")
    if choice == 'h':
        return 'offer'

    return 'book'


if __name__ == '__main__':
    main()