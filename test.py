from markovgen import Markov
import textwrap

fname = "./datatxt/sherlock_holmes.txt"
txt = open(fname, "r").read()
m = Markov(2)
m.learn(txt)
print textwrap.fill(m.generate(100,["Sherlock","Holmes"]), width=72)

