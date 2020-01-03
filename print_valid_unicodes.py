import sys
import unicodedata

MAX = sys.maxunicode
# MAX = 1000
EXCLUDES = ['IDEOGRAPH', 'VARIATION SELECTOR', ]

def filtered_by_exclude(name):
    excluded = False
    for exclude in EXCLUDES:
        if exclude in name:
            excluded = True
            break
    return excluded


for i in range(0, MAX):
    try:
        if unicodedata.category(chr(i)) == 'Cc':
            print('Cc', i, '** CONTROL CHARACTER **')
            pass
        name = unicodedata.name(chr(i))
        if name is None:
            pass
        if filtered_by_exclude(name):
            pass
        else:
            print(chr(i), i, name)
    except UnicodeEncodeError:
        pass
    except ValueError:
        pass
