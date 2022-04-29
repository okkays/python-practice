import unittest


def autocomplete(filename: str, word: str, num_results: int) -> List[str]:
  raise NotImplementedError('Your code goes here!')


duck_example = [
    '[Wed Dec  4 16:21:58 2013] <kkays> I like cake',
    '[Wed Dec  4 16:21:58 2013] <kkays> You like cake',
    '[Wed Dec  4 16:21:58 2013] <kkays> I like ducks',
]


class TestAutocomplete(unittest.TestCase):

  def test_simple_case(self):
    with open('/tmp/simple-case.txt', 'w') as test_file:
      test_file.writelines(duck_example)
    self.assertEqual(autocomplete('tmp/simple-case.txt', 'like', 2),
                     ['cake', 'ducks'])


if __name__ == '__main__':
  unittest.main()
