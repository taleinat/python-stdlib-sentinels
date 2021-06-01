from sentinels import sentinel

import copy
import pickle
import unittest


sent = sentinel('sent')
sent2 = sentinel('sent2')


class TestSentinel(unittest.TestCase):
    def test_identity(self):
        self.assertIs(sent, sent)
        self.assertEqual(sent, sent)

    def test_uniqueness(self):
        self.assertIsNot(sent, sent2)
        self.assertNotEqual(sent, sent2)
        self.assertIsNot(sent, None)
        self.assertNotEqual(sent, None)
        self.assertIsNot(sent, Ellipsis)
        self.assertNotEqual(sent, Ellipsis)
        self.assertIsNot(sent, 'sent')
        self.assertNotEqual(sent, 'sent')
        self.assertIsNot(sent, '<sent>')
        self.assertNotEqual(sent, '<sent>')

    def test_repr(self):
        self.assertEqual(repr(sent), '<sent>')

    def test_type(self):
        self.assertIsInstance(sent, type(sent))
        self.assertIn('sent', repr(type(sent)))

    def test_copy(self):
        self.assertIs(sent, copy.copy(sent))
        self.assertIs(sent, copy.deepcopy(sent))

    def test_pickle_roundtrip(self):
        self.assertIs(sent, pickle.loads(pickle.dumps(sent)))


if __name__ == '__main__':
    unittest.main()
