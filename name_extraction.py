import nltk
from nameparser.parser import HumanName

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    
    for subtree in sentt.subtrees():
        if subtree.label()  == 'PERSON':
            for leaf in subtree.leaves():
                person.append(leaf[0])
            if len(person) > 1: #avoid grabbing lone surnames
                for part in person:
                    name += part + ' '
                if name[:-1] not in person_list:
                    person_list.append(name[:-1])
                name = ''
            
            person = []
           

    return (person_list)

text = """
What Donald Trump said to Mr Obama"
"""

names = get_human_names(text)
print(names)
print ("LAST, FIRST")
for name in names: 
    last_first = HumanName(name).last + ', ' + HumanName(name).first
    print(last_first)