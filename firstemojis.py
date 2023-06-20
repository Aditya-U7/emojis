# Printing the modern day emojis of some of the first released emojis.

import unicodedata

def print_emojis(emojis):
    
    print("\nEmoji | Unicode Point | Name\n")

    for emoji in emojis:
      
        print(chr(emoji).ljust(4), end=" ")
    
        print(f'U+{emoji:05x}'.center(17), end=" ")
    
        print(unicodedata.name(chr(emoji)), end="\n\n")

    
emojis = [0x1F61E, 0x2615, 0x1f30b, 0x1F494, 0x1F4A9, 0x1f427]     # Unicode code points of emojis in hexadecimal.

print_emojis(emojis)
    

