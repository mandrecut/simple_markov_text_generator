# Markov text generator

Simple and fast Markov chain text generator using `cache`.

Main usage: building Markov models from text files, and generating random text. 

Markov chain Python class:

- `Markov(order)`

The `order` parameter corresponds to the Markov chain order `(>=1)`. 

Methods:

- `learn(txt)` creates a model given a string `txt`.

- `generate(length, seed)` generates a random text starting from `seed`, with a minimum `length`, until the last sentence ends in `".?!"`, 

The `seed` is a list of words with the length `order`, for example: ["Sherlock","Holmes"]. 
If the `seed` is not in the model then it is randomly set.

## Basic usage

```python
from markovgen import Markov
import textwrap

fname = "./datatxt/sherlock_holmes.txt"
txt = open(fname, "r").read()
m = Markov(2)
m.learn(txt)
print(textwrap.fill(m.generate(100,["Sherlock","Holmes"]), width=72))
```
```
Sherlock Holmes sprang from his smokes of the facts. You can understand,
a gash seemed to think, Watson, he has done a considerable share in
clearing the matter? It appeared in all the clues which I have had the
real name, answered our visitor of the road. He had set in, and how they
could get the address. Yes. And yet even here we may take it that the
pavement with his head? Why, you will have the goodness to sit, and in
spite of the most beautiful of women, and it could bear.
```

