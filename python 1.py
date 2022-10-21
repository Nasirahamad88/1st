Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


=
2-6
-4

========================================================================== RESTART: Shell =========================================================================
h=600
i=500
print(h+i)
1100
10+2*3
16
text="Ice crime"
text
'Ice crime'
text[1,2,3]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    text[1,2,3]
TypeError: string indices must be integers
text[012]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> text[123]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    text[123]
IndexError: string index out of range
>>> text[0,1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    text[0,1]
TypeError: string indices must be integers
>>> text[1 2 3]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> text[1, 2, 3]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    text[1, 2, 3]
TypeError: string indices must be integers
>>> text[1:3]   ;
'ce'
>>> text{0:3]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> text[0:3]
'Ice'
