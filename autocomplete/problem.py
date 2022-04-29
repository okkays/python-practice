from typing import List
import unittest

import itertools


def clean_chat(chat: str) -> str:
  return chat[chat.find('>') + 1:].strip()


def pairwise(iterable):
  a, b = itertools.tee(iterable)
  next(b, None)
  return zip(a, b)


def process_chat(words_to_next_words: dict, chat: str) -> str:
  for word, next_word in pairwise(chat.split()):
    next_words = words_to_next_words.get(word, {})
    new_count = next_words.get(next_word, 0) + 1
    next_words[next_word] = new_count
    words_to_next_words[word] = next_words


def autocomplete(filename: str, word: str, num_results: int) -> List[str]:
  with open(filename, 'r') as f:
    chats = [clean_chat(chat) for chat in f.readlines()]
  words_to_next_words = {}
  for chat in chats:
    process_chat(words_to_next_words, chat)
  next_words = words_to_next_words.get(word)
  if not next_words:
    return []
  sorted_tuples = sorted(list(next_words.items()), key=lambda t: -t[1])
  print(sorted_tuples[:num_results])
  return [word for word, count in sorted_tuples[:num_results]]


duck_example = [
    '[Wed Dec  4 16:21:58 2013] <kkays> I like cake\n',
    '[Wed Dec  4 16:21:58 2013] <kkays> You like cake\n',
    '[Wed Dec  4 16:21:58 2013] <kkays> We like cake\n',
    '[Wed Dec  4 16:21:58 2013] <kkays> I like ducks\n',
    '[Wed Dec  4 16:21:58 2013] <kkays> You like ducks\n',
    '[Wed Dec  4 16:21:58 2013] <kkays> I like waffles\n',
]


class TestAutocomplete(unittest.TestCase):

  CHATS = '../shared/chats.txt'

  def test_simple_case(self):
    with open('/tmp/simple-case.txt', 'w') as test_file:
      test_file.writelines(duck_example)
    self.assertEqual(autocomplete('/tmp/simple-case.txt', 'like', 2),
                     ['cake', 'ducks'])

  def test_from_chats_common(self):
    self.assertEqual(
        autocomplete(self.CHATS, 'I', 3),
        ['think', 'don\'t', 'have'],
    )

  def test_from_chats_simple(self):
    self.assertEqual(
        autocomplete(self.CHATS, 'like', 3),
        ['to', 'the', 'a'],
    )

  def test_from_chats_specific(self):
    self.assertSetEqual(
        set(autocomplete(self.CHATS, 'Microsoft', 3)),
        {'to', 'Windows', 'Dfs'},
    )

  def test_from_chats_single(self):
    self.assertEqual(
        autocomplete(self.CHATS, 'gradual', 1),
        ['growth'],
    )

  def test_from_chats_long(self):
    self.assertEqual(
        autocomplete(self.CHATS, 'other', 7),
        ['than', 'stuff', 'cells', 'servers', 'things', 'things,', 'hand,'],
    )


if __name__ == '__main__':
  unittest.main()
