from markovgen import Markov
import textwrap
import sys

if __name__ == '__main__':
    fname = "./datatxt/sherlock_holmes.txt"
    if(sys.version_info[0] < 3):
        with open(fname, "r") as f:
            txt = f.read().decode("UTF-8")
    else:
        with open(fname, "r", encoding="utf-8") as f:
            txt = f.read()
    m = Markov(2)
    m.learn(txt)
    print(textwrap.fill(m.generate(100,["Sherlock","Holmes"]), width=72))

