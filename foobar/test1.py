import string

def char2inversed_id(char):
    """ Converts char to id (int) with one-hot encoding handling of unexpected characters"""
    if char in string.ascii_lowercase:
        return 97 + (122 - ord(char))
    elif char in string.ascii_lowercase:
        return 65 + (90 - ord(char))
    else: # pass other characters normally
        return ord(char)

def id2char(dictid):
    """ Converts single id (int) to character"""
    if dictid > 0:
        return chr(dictid)
    else:
        return ' '

def answer(s):
    """ Decyphers the sentence character by characted"""
    return ''.join([id2char(char2inversed_id(ch)) for ch in s])
    

if __name__ == "__main__":
    #print(ix_to_char[char_to_ix['a']])
    #print(id2char(char2inversed_id('a')), id2char(char2inversed_id('A')))
    
    #print([ord(ch) for ch in "abcdefghijklmnopqrstuvwxyz"])
    #print([id2char (id) for id in [1, 2, 3, 4]])
    #print([ord(ch) for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
    print(answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
    print(answer("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
    

