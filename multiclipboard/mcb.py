#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: python mcb.pyw save <clip name> - Saves clipboard as clip name
#        python mcb.pyw <clip name> - Loads clip to clipboard
#        python mcb.pyw list - Loads all keywords to clipboard
#        python mcb.pyw clear - Deletes all saved clips
#        python mcb.pyw del <clip name> - Deletes single clip

import shelve, pyperclip, sys
from termcolor import cprint

mcbShelf = shelve.open('mcb')
command = sys.argv[1]

# Save clipboard content
if len(sys.argv) == 3 and command == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    cprint('Clip ' + sys.argv[2] + ' saved!', 'green', attrs=['bold'])
elif len(sys.argv) == 3 and command == 'del':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if command == 'list':
        if mcbShelf.__len__() > 0:
            cprint(str(list(mcbShelf.keys())), 'green', attrs=['bold'])
        else:
            cprint('No saved clips', 'red')
    elif command == 'clear':
        mcbShelf.clear()
        cprint('All clips deleted', 'green', attrs=['bold'])
    elif command in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        cprint('Clip not found, here\'s a list of saved clips:', 'red')
        cprint(str(list(mcbShelf.keys())), 'green', attrs=['bold'])

mcbShelf.close()
