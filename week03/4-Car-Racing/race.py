import sys
from json_operator import JsonOperator
from car import Car
from driver import Driver
from championship import Championship
from ranking import Race


class CLI:
    def __init__(self):
        self._commands = sys.argv[:]
        self._valid_commands = ['start', 'standings']
        self._wrong_input = 'Hello PyRacer!\n\
        Please, call command with the proper argument:\n\
        $ python3 race.py start <name> <races_count> -> This will start a new \n\
        championship with the given name, races count and drivers from cars.json\n\
        $ python3 race.py standings -> This will print the standings for \n\
        each championship that has ever taken place.'

    def validate_commands(self):
        print(self._commands)
        if len(self._commands) == 1:
            print(self._wrong_input)
        elif self._commands[1] == self._valid_commands[1] and len(self._commands) == 2:
            data = JsonOperator()
            data.json_result_input()

        elif self._commands[1] == self._valid_commands[0] and len(self._commands) == 4:
            try:
                int(self._commands[3])
                if isinstance(self._commands[2], str):
                    print('succeed')
            except:
                print(self._wrong_input)
        else:
            print(self._wrong_input)


def main():
    a = CLI()
    a.validate_commands()


if __name__ == '__main__':
    main()
