#!/usr/bin/env python3
"""Example usage of the columnize library."""

from columnize import __version__, columnize

print("Columnize version: %s\n" % __version__)

# 1. Basic formatting (arrange vertically, default separator '  ')
print("--- 1. Basic Vertical Formatting ---")
data = ["Item-%s" % i for i in range(1, 13)]
result = columnize(data, displaywidth=40)
print(result)

# 2. Horizontal formatting
print("--- 2. Horizontal Formatting ---")
result_horizontal = columnize(data, displaywidth=40, arrange_vertical=False)
print(result_horizontal)

# 3. Custom column separator and custom line prefix
print("--- 3. Custom Column Separator & Line Prefix ---")
result_custom = columnize(
    data,
    displaywidth=45,
    colsep=" | ",
    lineprefix=">> ",
)
print(result_custom)

# 4. Numeric data with right justification (ljust=False)
print("--- 4. Right Justified Numeric Data ---")
numbers = [str(10**i) for i in range(7)]
result_numbers = columnize(numbers, displaywidth=30, ljust=False, colsep="  ")
print(result_numbers)

# 5. Using the arrange_array option
print("--- 5. Formatted as an Array ---")
result_array = columnize(
    list(range(20)),
    opts={"displaywidth": 40, "arrange_array": True},
)
print(result_array)
