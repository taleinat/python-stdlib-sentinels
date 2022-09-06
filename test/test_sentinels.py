from sentinels import Sentinel

import copy
import pickle
import unittest


sent1 = Sentinel('sent1')
sent2 = Sentinel('sent2', repr='test_sentinels.sent2')


class TestSentinel(unittest.TestCase):
    def setUp(self):
        self.sent_defined_in_function = Sentinel('defined_in_function')

    def test_identity(self):
        for sent in sent1, sent2, self.sent_defined_in_function:
            with self.subTest(sent=sent):
                self.assertIs(sent, sent)
                self.assertEqual(sent, sent)

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

    def test_same_object_in_same_module(self):
        copy1 = Sentinel('sent1')
        self.assertIs(copy1, sent1)
        copy2 = Sentinel('sent1')
        self.assertIs(copy2, copy1)

    def test_same_object_fake_module(self):
        copy1 = Sentinel('FOO', module_name='i.dont.exist')
        copy2 = Sentinel('FOO', module_name='i.dont.exist')
        self.assertIs(copy1, copy2)

    def test_unique_in_different_modules(self):
        other_module_sent1 = Sentinel('sent1', module_name='i.dont.exist')
        self.assertIsNot(other_module_sent1, sent1)

    def test_repr(self):
        self.assertEqual(repr(sent1), '<sent1>')
        self.assertEqual(repr(sent2), 'test_sentinels.sent2')

    def test_type(self):
        self.assertIsInstance(sent1, Sentinel)
        self.assertIsInstance(sent2, Sentinel)

    def test_copy(self):
        self.assertIs(sent1, copy.copy(sent1))
        self.assertIs(sent1, copy.deepcopy(sent1))

    def test_pickle_roundtrip(self):
        self.assertIs(sent1, pickle.loads(pickle.dumps(sent1)))

    def test_bool_value(self):
        self.assertTrue(sent1)
        self.assertTrue(Sentinel('I_AM_FALSY'))

    def test_automatic_module_name(self):
        self.assertIs(
            Sentinel('sent1', module_name=__name__),
            sent1,
        )
        self.assertIs(
            Sentinel('defined_in_function', module_name=__name__),
            self.sent_defined_in_function,
        )

    def test_subclass(self):
        class FalseySentinel(Sentinel):
            def __bool__(self):
                return False
        subclass_sent = FalseySentinel('FOO')
        self.assertIs(subclass_sent, subclass_sent)
        self.assertEqual(subclass_sent, subclass_sent)
        self.assertFalse(subclass_sent)
        non_subclass_sent = Sentinel('FOO')
        self.assertIsNot(subclass_sent, non_subclass_sent)
        self.assertNotEqual(subclass_sent, non_subclass_sent)


if __name__ == '__main__':
    unittest.main()
