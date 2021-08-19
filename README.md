# A Python special characters translator :snake::u6e80::ok:
## Description
This project introduces a simple character translator for Python. Since some libraries do not like some special characters (e.g. á, ñ, þ, ®) it will allow you to replace these characters in your file and, after finishing working with it, undo the traduction.

## Files
### translate_special_characters_to_html.ipynb
It is the Jupyter Notebook where the translator functions are located. There are two functions:
- translate_to_html: Replaces special characters by their html code.
- translate_to_special: Replaces html codes by special characters.

The character replacements are specified in a dictionary like this one:
```
char_to_replace = {'Á' : '&Aacute;',
                   'á' : '&aacute;',
                   'À' : '&Agrave;'}
```
And its opposite would look like this:
```
char_to_replace = {'&Aacute;' : 'Á',
                   '&aacute;' : 'á',
                   '&Agrave;' : 'À'}
```
### example_files folder
It contains some example files with special characters and html codes.

## Usage
The replacement process is easy. The user just needs to specify the paths of the original file and the new file (the one with the character replacements) and call one of the 2 functions. The original file is then read, the characters replaced and the resulting text is written into a new file. An example code of how to use the functions is provided at the bottom of the Jupyter Notebook.

## FEEL FREE TO MODIFY THE TRANSLATOR FUNCTIONS ACCORDING TO YOUR NEEDS!
