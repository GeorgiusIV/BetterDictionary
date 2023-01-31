from random import randint

class Words:
    def __init__(self, contents = None):

        self.contents = contents

        # if no contents are specified, use the default dictionary 
        if contents is None:
            with open('DICTIONARY.txt', 'r', encoding='utf-8') as f: # split words by t/ and remove /n
                self.contents = [l.replace('\n','').split('\t') for l in f.readlines()]


        
    def __repr__(self):
        
        # TODO: format self.contents more appropriately
        
        return str(self.contents)



    def __len__(self):

         return len(self.contents)



    def ofLength(self, length, rule = '=='):
        
        newContents = list()

        # the input of length must be an integer
        # the input of rule must be a string that can be evaluated to a logical operator

        # so first I want to verify the inputs
        # then once the inputs are verified, select a path to follow by the rule provided
        # then once the path is selected, use the length to filter the words appropriately
        
        # TODO: verify the inputs 'length' and 'rule'

        rule = str(rule)
        for word in self.contents:

            if rule == '<': 
                if len(word) < length: 
                    newContents += [word]

            elif rule == '<=':
                if len(word) <= length: 
                    newContents += [word]

            elif rule == '==': 
                if len(word) == length: 
                    newContents += [word]

            elif rule == '>=':
                if len(word) >= length: 
                    newContents += [word]

            elif rule == '>':
                if len(word) > length: 
                    newContents += [word]

            else: 
                print("Rule is unrecognized")
            
        return Words(newContents)


    
    def asPhonemes(self):
        
        newContents = self.contents
        
        #TODO: modify newContents such that all words composed of letters are replaced with their phoneme counterparts
        
        return Words(newContents)


    
    def takeSample(self, size):
        
        length = len(self.contents)
        sample = [self.contents[randint(0,length)] for _ in range(0,size)]
        
        return Words(sample)
    
    
if __name__ == "__main__":
    words = Words()
    words.asPhonemes().ofLength(3)
            
