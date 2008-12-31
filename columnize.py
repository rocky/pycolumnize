# -*- coding: utf-8 -*-
"""Return compact set of columns as a string with newlines for an
array of strings.

Adapted from the routine of the same name inside cmd.py"""
import types

def columnize(array, displaywidth=80, colsep = '  ', arrange_vertical=True):
    """Return a list of strings as a compact set of columns arranged 
    horizontally or vertically.

    For example, for a line width of 4 characters (arranged vertically):
        ['1', '2,', '3', '4'] => '1  3\n2  4\n'
   
    or arranged horizontally:
        ['1', '2,', '3', '4'] => '1  2\n3  4\n'
        
    Each column is only as wide as necessary.  By default, columns are
    separated by two spaces - one was not legible enough. Set "colsep"
    to adjust the string separate columns. Set `displaywidth' to set
    the line width. """
    if not isinstance(array, list) and not isinstance(array, tuple): 
        raise TypeError, (
            'array needs to be an instance of a list or a tuple')

    nonstrings = [i for i in range(len(array))
                    if not isinstance(array[i], str)]
    if nonstrings:
        raise TypeError, ("array[i] not a string for i in %s" %
                          ", ".join(map(str, nonstrings)))

    # Some degenerate cases
    size = len(array)
    if 0 == size: 
        return "<empty>\n"
    elif size == 1:
        return '%s\n' % str(array[0])
    
    if arrange_vertical:
        array_index = lambda nrows, row, col: nrows*col + row
    else:
        array_index = lambda nrows, row, col: nrows*row + col
        pass

    # Try every row count from 1 upwards
    ncols = size
    for nrows in range(1, len(array)):
        colwidths = []
        totwidth = -len(colsep)
        for col in range(ncols):
            # get max column width for column "col"
            colwidth = 0
            for row in range(nrows):
                i = array_index(nrows, row, col)
                if i >= size:
                    break
                x = array[i]
                colwidth = max(colwidth, len(x))
                pass
            colwidths.append(colwidth)
            totwidth += colwidth + len(colsep)
            if totwidth > displaywidth:
                ncols = col
                break
            pass
        if totwidth <= displaywidth:
            break
        pass
    else:
        nrows = len(array)
        ncols = 1
        colwidths = [0]
        pass

    # The smallest number of rows computed and the
    # max widths for each column has been obtained.
    # Now we just have to format each of the
    # rows.
    s = ''
    for row in range(nrows):
        texts = []
        for col in range(ncols):
            i = array_index(nrows, row, col)
            if i >= size:
                x = ""
            else:
                x = array[i]
                pass
            texts.append(x)
        while texts and not texts[-1]:
            del texts[-1]
        for col in range(len(texts)):
            texts[col] = texts[col].ljust(colwidths[col])
            pass
        s += "%s\n" % str(colsep.join(texts))
        pass
    return s

# Demo it
if __name__=='__main__':
  #
#   print columnize([])
    print columnize(['1', '2', '3', '4'], 4)
    print columnize(["a", '2', "c"], 10, ', ')
#   print columnize(["oneitem"])
#   print columnize(("one", "two", "three",))
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
    print columnize(data)
    print columnize(data, arrange_vertical=False)
    
    try:
        print columnize(5)
    except TypeError, e:
        print e
        pass
    
    try:
        # We don't str the array, probably in the future we should
        print columnize(range(4))
    except TypeError, e:
        print e
        pass
    pass
