from sentinels import sentinel

import copy
import pickle
import unittest


sent1 = sentinel('sent1')
sent2 = sentinel('sent2', repr='test_sentinels.sent2')


class TestSentinel(unittest.TestCase):
    def test_identity(self):
        self.assertIs(sent1, sent1)
        self.assertEqual(sent1, sent1)

    def test_uniqueness(self):
        self.assertIsNot(sent1, sent2)
        self.assertNotEqual(sent1, sent2)
        self.assertIsNot(sent1, None)
        self.assertNotEqual(sent1, None)
        self.assertIsNot(sent1, Ellipsis)
        self.assertNotEqual(sent1, Ellipsis)
        self.assertIsNot(sent1, 'sent1')
        self.assertNotEqual(sent1, 'sent1')
        self.assertIsNot(sent1, '<sent1>')
        self.assertNotEqual(sent1, '<sent1>')

    def test_repr(self):
        self.assertEqual(repr(sent1), '<sent1>')
        self.assertEqual(repr(sent2), 'test_sentinels.sent2')

    def test_type(self):
        self.assertIsInstance(sent1, type(sent1))
        self.assertIsInstance(sent2, type(sent2))
        self.assertIsNot(type(sent1), type(sent2))

    def test_copy(self):
        self.assertIs(sent1, copy.copy(sent1))
        self.assertIs(sent1, copy.deepcopy(sent1))

    def test_pickle_roundtrip(self):
        self.assertIs(sent1, pickle.loads(pickle.dumps(sent1)))

    def test_truthiness(self):
        self.assertTrue(sent1)
        self.assertTrue(sentinel('I_AM_TRUTHY'))
        self.assertFalse(sentinel('I_AM_FALSY', is_truthy=False))


if __name__ == '__main__':
    unittest.main()
