from typing import List
import unittest


def search_for_hashtag(filename: str, hashtag: str) -> List[str]:
  raise NotImplementedError('Your code goes here!')


class TestTwitter(unittest.TestCase):

  def test_simple_hashtags(self):
    self.assertEqual(search_for_hashtag('tweets.txt', '#fatcat'),
                     ['Lua is a #fatcat'])

  def test_weird_hashtags(self):
    self.assertEqual(search_for_hashtag('tweets.txt', '#!@#$'),
                     ['This tweet is bull #!@#$'])

  def test_repeated_hashtags(self):
    self.assertEqual(len(search_for_hashtag('tweets.txt', '#blessed')), 3)

  def test_multiple_hashtags(self):
    self.assertEqual(search_for_hashtag('tweets.txt', '#coffee'),
                     search_for_hashtag('tweets.txt', '#delicious'))


if __name__ == '__main__':
  unittest.main()
