from hyphen import Hyphenator
h_en = Hyphenator('en_US')

output = h_en.syllables('longer')
print(output)


def get_syllables(word):
    """
    using hypenator return syllables of an input word
    """
    syllables = h_en.syllables(word)
    if syllables == []:
        return [word]
    else:
        return syllables

def get_coloured_para(para):
    """
    for each word in a para
    get the sylleblyes of that word
    create a coloured version of the word
    patch these together into a new vibrant paragraph
    """
    coloured_para = []
    for word in para:
        colored_word = color_word(word)
        coloured_para.append(colored_word)
    return coloured_para


# the palette of colours that we will use
colours = ["red", "green", "blue"]


def colour_syllable(syllable, colour_index):
    coloured_syllable = '<span style="color:'+colours[colour_index] +';">'+syllable+ "</span>"
    return coloured_syllable



def color_word(word):
    """
    for each syllable in a word
    colour that syllable in
    """
    word_syllables = get_syllables(word)
    coloured_word = []
    for ws in word_syllables:
        colour_index = word_syllables.index(ws) % len(colours) 
        cs = colour_syllable(ws, colour_index)
        coloured_word.append(cs)
    coloured_word.append(" ")
    #TODO: think about putting in a fix for missing spaces here. 
    return "".join(coloured_word)


test_para = """this is a longer and challenging example of the kind of words and 
adventures that we might expect or hope to find in the future. Furthermore, looking 
and here are some exceptionally extravagant words to look at beyond simple constructions, could this be used to create a wizzard or a dragon in the country of magic?"""

para_list = test_para.split()
print(para_list)
coloured_para = get_coloured_para(para_list)
print(coloured_para)

with open('example.html', 'w') as f:
    for item in coloured_para:
        f.write(item)

