#!/usr/bin/env python
# -*- Python -*-
"Unit test for Tracer"
import operator, os, sys, unittest

top_builddir = os.path.join(os.path.dirname(__file__), '..')
if top_builddir[-1] != os.path.sep:
    top_builddir += os.path.sep
sys.path.insert(0, top_builddir)

from columnize import columnize

class TestColumize(unittest.TestCase):

    def test_basic(self):
        """Basic sanity and status testing."""
        self.assertEqual("1, 2, 3\n", 
                         columnize(['1', '2', '3'], 10, ', '))
        self.assertEqual("1  3\n2  4\n", 
                         columnize(['1', '2', '3', '4'], 4))
        self.assertEqual("1  2\n3  4\n", 
                         columnize(['1', '2', '3', '4'], 4, 
                                   arrange_vertical=False))
        self.assertEqual("<empty>\n", columnize([]))
        self.assertEqual("oneitem\n", columnize(["oneitem"]))
        data = (
            "one",       "two",         "three",
            "for",       "five",        "six",
            "seven",     "eight",       "nine",
            "ten",       "eleven",      "twelve",
            "thirteen",  "fourteen",    "fifteen",
            "sixteen",   "seventeen",   "eightteen",
            "nineteen",  "twenty",      "twentyone",
            "twentytwo", "twentythree", "twentyfour",
            "twentyfive","twentysix",   "twentyseven",)

        self.assertEqual(
"one         two        three        for        five         six       \n" +
"seven       eight      nine         ten        eleven       twelve    \n" +
"thirteen    fourteen   fifteen      sixteen    seventeen    eightteen \n" +
"nineteen    twenty     twentyone    twentytwo  twentythree  twentyfour\n" +
"twentyfive  twentysix  twentyseven\n\n", columnize(data, arrange_vertical=False))

        self.assertEqual(
"one    five   nine    thirteen  seventeen  twentyone    twentyfive \n" +
"two    six    ten     fourteen  eightteen  twentytwo    twentysix  \n" +
"three  seven  eleven  fifteen   nineteen   twentythree  twentyseven\n" +
"for    eight  twelve  sixteen   twenty     twentyfour \n", columnize(data))
        return


    def test_errors(self):
        """Test various error conditions."""
        # Don't know why assertRaises fails...
        # self.assertRaises(TypeError, tracer.add_hook(5))
        try:
            print columnize(5)
            self.assertFalse(True, 'reject input - not array')
        except TypeError, e:
            self.assertTrue(True, 'reject input - not array')
            pass
        
        try:
            # We don't str the array, probably in the future we should
            print columnize(range(4))
            self.assertFalse(True, 'reject input - array items not string')
        except TypeError, e:
            self.assertTrue(True, 'reject input - array item not string')
            pass
        return
    pass

if __name__ == '__main__':
    unittest.main()
