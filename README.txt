Return a list of strings as a compact set of columns arranged 
horizontally or vertically.

For example, for a line width of 4 characters (arranged vertically):
    ['1', '2,', '3', '4'] => '1  3\n2  4\n'
   
or arranged horizontally:
    ['1', '2,', '3', '4'] => '1  2\n3  4\n'
        
Each column is only as wide as necessary.  By default, columns are
separated by two spaces - one was not legible enough. Set "colsep"
to adjust the string separate columns. Set `displaywidth' to set
the line width. 

Normally, consecutive items go down from the top to bottom from
the left-most column to the right-most. If +arrange_vertical+ is
set false, consecutive items will go across, left to right, top to
bottom.

Adapted from the routine of the same name inside cmd.py
