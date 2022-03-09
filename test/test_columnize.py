#!/usr/bin/env python
# -*- Python -*-
"Unit test for Columnize"
import pytest
import sys

from unittest import mock

from columnize import columnize


def test_basic():
    """Basic sanity and status testing."""
    assert "1, 2, 3\n" == columnize(["1", "2", "3"], 10, ", ")
    assert "1  3\n2  4\n" == columnize(["1", "2", "3", "4"], 4)

    assert "1  3\n2  4\n" == columnize(["1", "2", "3", "4"], 7)

    assert "0  1  2\n3\n" == columnize(["0", "1", "2", "3"], 7, arrange_vertical=False)

    assert "<empty>\n" == columnize([])
    assert "oneitem\n" == columnize(["oneitem"])

    data = [str(i) for i in range(55)]
    assert (
        "0,  6, 12, 18, 24, 30, 36, 42, 48, 54\n"
        + "1,  7, 13, 19, 25, 31, 37, 43, 49\n"
        + "2,  8, 14, 20, 26, 32, 38, 44, 50\n"
        + "3,  9, 15, 21, 27, 33, 39, 45, 51\n"
        + "4, 10, 16, 22, 28, 34, 40, 46, 52\n"
        + "5, 11, 17, 23, 29, 35, 41, 47, 53\n"
        == columnize(
            data, displaywidth=39, ljust=False, arrange_vertical=True, colsep=", "
        )
    )

    assert (
        "    0,  7, 14, 21, 28, 35, 42, 49\n"
        + "    1,  8, 15, 22, 29, 36, 43, 50\n"
        + "    2,  9, 16, 23, 30, 37, 44, 51\n"
        + "    3, 10, 17, 24, 31, 38, 45, 52\n"
        + "    4, 11, 18, 25, 32, 39, 46, 53\n"
        + "    5, 12, 19, 26, 33, 40, 47, 54\n"
        + "    6, 13, 20, 27, 34, 41, 48\n"
        == columnize(
            data,
            displaywidth=39,
            ljust=False,
            arrange_vertical=True,
            colsep=", ",
            lineprefix="    ",
        )
    )

    assert (
        " 0,  1,  2,  3,  4,  5,  6,  7,  8,  9\n"
        + "10, 11, 12, 13, 14, 15, 16, 17, 18, 19\n"
        + "20, 21, 22, 23, 24, 25, 26, 27, 28, 29\n"
        + "30, 31, 32, 33, 34, 35, 36, 37, 38, 39\n"
        + "40, 41, 42, 43, 44, 45, 46, 47, 48, 49\n"
        + "50, 51, 52, 53, 54\n"
        == columnize(
            data, displaywidth=39, ljust=False, arrange_vertical=False, colsep=", "
        )
    )

    assert (
        "     0,  1,  2,  3,  4,  5,  6,  7\n"
        + "     8,  9, 10, 11, 12, 13, 14, 15\n"
        + "    16, 17, 18, 19, 20, 21, 22, 23\n"
        + "    24, 25, 26, 27, 28, 29, 30, 31\n"
        + "    32, 33, 34, 35, 36, 37, 38, 39\n"
        + "    40, 41, 42, 43, 44, 45, 46, 47\n"
        + "    48, 49, 50, 51, 52, 53, 54\n"
        == columnize(
            data,
            displaywidth=34,
            ljust=False,
            arrange_vertical=False,
            colsep=", ",
            lineprefix="    ",
        )
    )

    data = (
        "one",
        "two",
        "three",
        "for",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eightteen",
        "nineteen",
        "twenty",
        "twentyone",
        "twentytwo",
        "twentythree",
        "twentyfour",
        "twentyfive",
        "twentysix",
        "twentyseven",
    )

    assert (
        "one         two        three        for        five         six       \n"
        + "seven       eight      nine         ten        eleven       twelve    \n"
        + "thirteen    fourteen   fifteen      sixteen    seventeen    eightteen \n"
        + "nineteen    twenty     twentyone    twentytwo  twentythree  twentyfour\n"
        + "twentyfive  twentysix  twentyseven\n"
        == columnize(data, arrange_vertical=False)
    )

    assert (
        "one    five   nine    thirteen  seventeen  twentyone    twentyfive \n"
        + "two    six    ten     fourteen  eightteen  twentytwo    twentysix  \n"
        + "three  seven  eleven  fifteen   nineteen   twentythree  twentyseven\n"
        + "for    eight  twelve  sixteen   twenty     twentyfour \n"
        == columnize(data)
    )

    assert "0  1  2  3\n" == columnize(list(range(4)))

    assert (
        "[ 0,  1,  2,  3,  4,  5,  6,  7,  8,\n"
        + "  9, 10, 11, 12, 13, 14, 15, 16, 17,\n"
        + " 18, 19, 20, 21, 22, 23, 24, 25, 26,\n"
        + " 27, 28, 29, 30, 31, 32, 33, 34, 35,\n"
        + " 36, 37, 38, 39, 40, 41, 42, 43, 44,\n"
        + " 45, 46, 47, 48, 49, 50, 51, 52, 53,\n"
        + " 54]\n\n"
        == columnize(list(range(55)), opts={"displaywidth": 38, "arrange_array": True})
    )

    assert (
        "[ 0,\n  1,\n  2,\n  3,\n  4,\n  5,\n  6,\n  7,\n  8,\n  9,\n 10,\n 11]\n\n"
        == columnize(list(range(12)), opts={"displaywidth": 6, "arrange_array": True})
    )

    assert (
        "[ 0,  1,\n  2,  3,\n  4,  5,\n  6,  7,\n  8,  9,\n 10, 11]\n\n"
        == columnize(list(range(12)), opts={"displaywidth": 9, "arrange_array": True})
    )
    return


def test_colfmt():
    assert "    0      1      2      3\n" == columnize(
        [0, 1, 2, 3], 7, arrange_vertical=False, opts={"colfmt": "%5d"}
    )


def test_lineprefix():
    assert ">>>       0\n>>>       1\n>>>       2\n>>>       3\n" == columnize(
        [0, 1, 2, 3],
        7,
        arrange_vertical=False,
        opts={"colfmt": "%5d", "displaywidth": 16, "lineprefix": ">>>   "},
    )


def test_lineprefix_just_wide_enough():
    assert ">>>10  12\n>>>11  13\n" == columnize(
        [10, 11, 12, 13], opts={"lineprefix": ">>>", "displaywidth": 9}
    )


if sys.version_info[:2] >= (3, 6):

    @mock.patch.dict('os.environ', {'COLUMNS': '87'}, clear=True)
    def test_computed_displaywidth_environ_COLUMNS_set():
        from columnize import computed_displaywidth
        width = computed_displaywidth()
        assert width == 87

def test_errors():
    """Test various error conditions."""
    with pytest.raises(TypeError):
         columnize(5)
    return

if __name__ == "__main__":
    test_basic()
