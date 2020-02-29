import json
from numpy.random import choice
import gdrive_helper as ghelp

class Stringer_Ctrl:
    def __init__(self):
        with open('templates.json','r') as f:
            self.raw_templates = json.load(f)
            self.formats, self.weights, self.vars = zip(*self.raw_templates)
            self.custom_words = list(x['The word'] for x in ghelp.get_all_values())
            
    def pick_pattern(self):
        pick = choice(list(i for i in range(len(self.formats))), p=tuple(x/sum(self.weights) for x in self.weights))
        return self.formats[pick], self.vars[pick]

    def generate(self, base=None):
        picked_format, picked_var = base if base else self.pick_pattern()
        picked_format = picked_format.replace('###WORD###',choice(self.custom_words))
        if picked_var:
            return picked_format.format(*list(self.generate() for _ in range(picked_var)))
        else: return picked_format
    
    def authenticate(self):
        pass


        