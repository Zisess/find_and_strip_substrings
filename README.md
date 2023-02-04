# Find And Strip Substrings

This code implements a function `find_and_strip_substrings(xstr, ystr, zstr)` which finds all substrings of `xstr` that are enclosed by `ystr` and `zstr` and returns the concatenated result of stripping both `ystr` and `zstr` from these substrings.

## How it works

The function works by using the find method to search for the ystr and zstr markers in xstr. The find method returns the index of the first occurrence of the search string, or -1 if the search string is not found.

If ystr is found in xstr, the function continues to search for zstr starting from the index just after ystr. If zstr is also found, the function extracts the substring between ystr and zstr and removes both ystr and zstr from it.

The process repeats until all occurrences of ystr and zstr in xstr have been processed. The final result is the concatenated result of all stripped substrings.

## Usage

To use the function, simply import it into your project and call the `FindAndStripSubstrings` function with three strings as input: the input string `xstr`, the first substring `ystr`, and the second substring `zstr`.

```python
>>> find_and_strip_substrings("xyz", "x", "z")
>>> output: "y"

>>> find_and_strip_substrings("xyz", "a", "b")
>>> output: "xyz"

Output: "helloworld goodbye moon"
```


## Contributing
Feel free to fork the repository and submit a pull request if you have any improvements or bug fixes.

License
This project is licensed under the MIT License. See LICENSE for details.
