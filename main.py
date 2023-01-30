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

    


    def ofLength(self, rule):
        
        newContents = self.contents
        
        try: 
            length = int(rule)
            self.contents = []
            # TODO: modify self.contents to follow the rule that the length must equal exactly [num]
            
        except:
            condition = str(rule)
            operand, length = condition[0:-lengthofNum], condition[-lengthofNum]
            # TODO: determine the length of the number and the length of the condition submitted by the user
            # TODO: modify self.contents to follow the rule [condition] [num]
            
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
            
