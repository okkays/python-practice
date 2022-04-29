# Autocomplete

../shared/chats.txt contains a list of actual IRC messages found on [web.mit.edu](https://web.mit.edu/jgross/zlog/irc/freenode:%23OpenAFS)

Use that list to build an "autocomplete" service, like modern phone keyboards use to suggest the next word a user intends to type.

When provided a word, your autocomplete service should return a number of options for what comes next. In order to determine what comes next, your function should use the list of chats to provide, from most common to least common, words that usually occur following the provided word.

For example, if the chat messages were:

- I like cake
- You like cake
- I like ducks

And you ran:

```python
autocomplete('like', 2)
```

You'd expect the output:

```python
['cake', 'ducks']
```

Each message contains additional metadata (a timestamp, and the user who wrote it) - you'll need to strip those out. Don't worry about doing any other sanitization, though.

With 'cake' first, because it happens twice after 'like', and 'ducks' second, because it happens once. There are of course plenty of edge cases to consider, which are laid out in `problem.py`

Implement `autocomplete` in [problem.py](./problem.py). When it's complete, running `python problem.py` should result in no test failures.
