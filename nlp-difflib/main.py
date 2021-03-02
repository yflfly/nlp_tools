# coding:utf-8
import difflib

text1 = '''  1. Beautiful is better than ugly.
   2. Explicit is better than implicit.
   3. Simple is better than complex.
   4. Complex is better than complicated.
        '''.splitlines(keepends=False)

text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
    '''.splitlines(keepends=True)
d = difflib.Differ()
print(''.join(d.compare(text1, text2)))
