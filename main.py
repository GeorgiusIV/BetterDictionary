
    def __init__(self):
        self.contents = list()
        # TODO: self.contents = read in the whole file to a list
        
    def __repr__(self):
        
        # TODO: format self.contents more appropriately
        
        return str(self.contents)
    
    def ofLength(self, rule):
        
        try: 
            length = int(rule)
            self.contents = []
            # TODO: modify self.contents to follow the rule that the length must equal exactly [num]
            
        except:
            condition = str(rule)
            operand, length = condition[0:-lengthofNum], condition[-lengthofNum]
            # TODO: determine the length of the number and the length of the condition submitted by the user
            # TODO: modify self.contents to follow the rule [condition] [num]
            
        return self
    
    def asPhonemes(self):
        
        #TODO: modify self.contents such that all words composed of letters are replaced with their phoneme counterparts
        
        return self
    
words = Words()
words.asPhonemes().ofLength(3)
            
