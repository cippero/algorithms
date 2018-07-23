# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result.

def play_pass(s, n):
    letters, new_s = 'abcdefghijklmnopqrstuvwxyz', ''
    for e in s:
        if e.isalpha() and (len(new_s)+1) % 2 == 0:  new_s += letters[(letters.index(e.lower())+n)%26]
        elif e.isalpha(): new_s += letters[(letters.index(e.lower())+n)%26].upper()
        elif e.isdigit(): new_s += str(9-int(e))
        else: new_s += e
    return new_s[::-1]