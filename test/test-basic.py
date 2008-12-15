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
        self.assertEqual("<empty>\n", columnize([]))
        self.assertEqual("oneitem\n", columnize(["oneitem"]))
        self.assertEqual(
            "one    6hree  11o    16e    21ree  26o    31e    36ree  41o    46e    three\n" +
            "two    7ne    12ree  17o    22e    27ree  32o    37e    42ree  47o  \n" +
            "three  8wo    13e    18ree  23o    28e    33ree  38o    43e    48ree\n" +
            "4ne    9hree  14o    19e    24ree  29o    34e    39ree  44o    one  \n" +
            "5wo    10e    15ree  20o    25e    30ree  35o    40e    45ree  two  \n",
            columnize([
                    "one", "two", "three",
                    "4ne", "5wo", "6hree",
                    "7ne", "8wo", "9hree",
                    "10e", "11o", "12ree",
                    "13e", "14o", "15ree",
                    "16e", "17o", "18ree",
                    "19e", "20o", "21ree",
                    "22e", "23o", "24ree",
                    "25e", "26o", "27ree",
                    "28e", "29o", "30ree",
                    "31e", "32o", "33ree",
                    "34e", "35o", "36ree",
                    "37e", "38o", "39ree",
                    "40e", "41o", "42ree",
                    "43e", "44o", "45ree",
                    "46e", "47o", "48ree",
                    "one", "two", "three"]))
#         data = (
#             "one",       "two",         "three",
#             "for",       "five",        "six",
#             "seven",     "eight",       "nine",
#             "ten",       "eleven",      "twelve",
#             "thirteen",  "fourteen",    "fifteen",
#             "sixteen",   "seventeen",   "eightteen",
#             "nineteen",  "twenty",      "twentyone",
#             "twentytwo", "twentythree", "twentyfour",
#             "twentyfive","twentysix",   "twentyseven",)

#         self.assertEqual(
# "one    five   nine    thirteen  seventeen  twentyone    twentyfive \n" +
# "two    six    ten     fourteen  eightteen  twentytwo    twentysix  \n" +
# "three  seven  eleven  fifteen   nineteen   twentythree  twentyseven\n" +
# "for    eight  twelve  sixteen   twenty     twentyfour ", columnize(data))

#         self.assertEqual(
# "one    two    three  for    five    six     seven     eight     nine   "
# "for    five   six    seven  eight   nine    ten       eleven    twelve "
# "seven  eight  nine   ten    eleven  twelve  thirteen  fourteen  fifteen"
# "one    five   nine    thirteen  seventeen  twentyone    twentyfive \n" a+
# "two    six    ten     fourteen  eightteen  twentytwo    twentysix  \n" +
# "three  seven  eleven  fifteen   nineteen   twentythree  twentyseven\n" +
# "for    eight  twelve  sixteen   twenty     twentyfour ", columnize(data),)
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
