import random
import re

class Markov(object):
	
    def __init__(self, order=1):
        self.cache = {}
        self.order = order
	
    def learn(self, txt):
        words = re.findall(r"[\w']+|[.,!?;:]", txt)
        for n in range(len(words)-self.order):
            key = tuple(words[n:n+self.order])
            if key in self.cache:
                self.cache[key].append(words[n+self.order])
            else:
                self.cache[key] = [words[n+self.order]]
	
    def generate(self, length, seed):
        if tuple(seed) not in self.cache.keys():
            state = list(random.choice(self.cache.keys()))
            print("Seed randomly set!\n")
        else:
            state = seed
        out = [state[0].title()]
        for i in range(1,len(state)):
            out.append(state[i])
        n = 0
        while n<length-self.order or state[self.order-1] not in ".?!":
            w,n = random.choice(self.cache[tuple(state)]),n+1
            out.append(w)
            state[0:self.order-1] = state[1:self.order]
            state[self.order-1] = w
        out = " ".join(out)
        for w in ".,!?;:'": 
            out = out.replace(" "+w, w)
        return out

