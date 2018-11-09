"""
Author: Nathan Petrangelo

Just for fun, I added command '*' that draws a star shape.
Its inputs are the same as command 'P'.

Dictionaries would have made this so much simpler.
"""

import turtle as t

# Returns number at the start of a string
def number(st):
    if st == '' or not st[0].isdigit():
        print("Error: String does not start with number")
        return None

    for i in range(len(st)):
        if not st[i].isdigit():
            return st[:i]

    # If there are no non-digit characters, the whole string is a number
    return st

# Parses all commands that don't take and parameters
def parse_no_parameters(command):
    if command == 'U':
        t.up()
    elif command == 'D':
        t.down()
    else:
        print('Error: How the heck did you end up here?')

# Sets the color of the turtle according to a number
def set_color(number):
    if number == 0:
        t.color('red')
    elif number == 1:
        t.color('blue')
    elif number == 2:
        t.color('green')
    elif number == 3:
        t.color('yellow')
    elif number == 4:
        t.color('brown')
    else:
        t.color('black')

# Parses all commands that only take one parameter
def parse_one_parameter(command, number):
    if command == 'F':
        t.fd(number)
    elif command == 'B':
        t.back(number)
    elif command == '<':
        t.left(number)
    elif command == '>':
        t.right(number)
    elif command == 'S':
        process_polygon(4, number)
    elif command == 'T':
        process_polygon(3, number)
    elif command == 'C':
        t.circle(number)
    elif command == 'Z':
        set_color(number)
    else:
        print('Error: How the heck did you end up here?')

def process_rectangle(length, height):
    # Bootstrapping, hell yeah!
    parse(2 * ('F' + str(length) + '<90F' + str(height) + '<90'))

def process_polygon(sides, length):
    angle = str(int(360/sides)) # The parser can only parse integers
    parse(sides * ('F' + str(length) + '<' + angle))

def process_star(sides, length):
    angle = str(int(720/sides)) # The parser can only parse integers
    parse(sides * ('F' + str(length) + '<' + angle))

# Parses all commands that take two parameters
def parse_two_parameters(command, number, number2):
    if command == 'G':
        t.goto(number, number2)
    elif command == 'R':
        process_rectangle(number, number2)
    elif command == 'P':
        process_polygon(number, number2)
    elif command == '*':
        process_star(number, number2)

"""
Parses a string of commands and parameters.
Process summary is as follows:
1. If the command takes no parameters, run it and start over
2. Grab the first parameter
3. If the command takes one parameter, run it and start over
4. Grab the second parameter
5. If the command takes two parameters, run it and start over
6. If the program gets this far, then break because the command is invalid
"""
def parse(st):
    while True:
        # Never parse an empty string
        if st == '':
            t.done()
            print("Done Parsing")
            break

        # Get command and remove it from the string
        command = st[0]
        st = st[1:]

        # Parse commands with no parameters and start the loop over
        if command in 'UD':
            parse_no_parameters(command)
            continue

        # Get first parameter and remove it from the string
        number1 = number(st)
        if number1 == None:
            break
        st = st[len(number1):]
        number1 = int(number1)

        # Parse commands with one parameter and start the loop over
        if command in 'FB<>STCZ':
            parse_one_parameter(command, number1)
            continue

        # If the program gets here, the next character must be a comma.
        # If it isn't, throw an error and break, otherwise remove the comma
        if st == '' or st[0] != ',':
            print('Error: Command', command, 'requires 2 parameters')
            break
        st = st[1:]

        # Get second parameter and remove it from the string
        number2 = number(st)
        if number2 == None:
            break
        st = st[len(number2):]
        number2 = int(number2)

        # Parse commands with two parameters and start the loop over
        if command in 'GRP*':
            parse_two_parameters(command, number1, number2)
            continue

        # If this point is ever reached, the user has entered an invalid command
        print('Invalid command:' + command)
        break

def main():
    print('Enter command:')
    parse(input())

if __name__ == '__main__':
    main()
