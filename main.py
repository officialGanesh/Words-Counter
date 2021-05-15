# Import the required module
from pprint import pprint

def Frequency():
    '''Counting the occurance of characters in text file'''


    with open('data.txt') as f:
        data = f.read()
        
        count = {}

        for character in data:

            count.setdefault(character,0)
            count[character] += 1
        pprint(count)

if __name__ == "__main__":

    Frequency()
    print("Code Completed 🔥")