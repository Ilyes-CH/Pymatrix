import time
import keyboard
import random
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def rain():
    columns = 200  
    rows = 100  

    # Initialize an empty matrix
    
    matrix = [[''] * columns for _ in range(rows)]

    while True:
        characters = []
        lettter =['1,2,3,4,5,6,7,8,9,0azertyuiiopù!:ml;,knjbhgvcfxdws<q&é(-è_çà)=²&&&&']
        for i in lettter[0]:
            characters.append(i)
            
        char = random.choice(characters)

        col = random.randint(0, columns - 1)

       
        matrix[0][col] = char

        # Print the matrix
        for row in matrix:
            print(Fore.GREEN + ''.join(row) + Style.RESET_ALL)

        time.sleep(0.01)

        # Shift all the characters downwards
        for r in range(rows - 1, 0, -1):
            matrix[r] = matrix[r - 1][:]

        # Clear the top row
        matrix[0] = [' '] * columns

        if keyboard.is_pressed('c'):
          
            break

def exit_code(key_stroke):
    if key_stroke.name == "c":
        print(Fore.GREEN + "Terminating the program...")
        raise SystemExit

keyboard.on_press(exit_code)

def main():
    while True:
        rain()
        if keyboard.is_pressed('c'):
            break

if __name__ == '__main__':
    main()
