#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def translate_to_html(original_file, new_file):
    #original_file: Path to the file to be translated.
    #new_file: Path where the translated file will be saved.
    
    #Open the file in read mode.
    print("TRANSLATING TO HTML")
    text_file = open(original_file, "r", encoding = 'latin-1')
 
    #We read the whole file and save its content in a string.
    data = text_file.read()
 
    #We close the file.
    text_file.close()

    #We show all the different characters found in the text.
    print("\nThese characters have been found:")
    print(sorted(set(data)))

    #We also show the first 100 characters.
    print("\nOriginal text:")
    print(data[0:100])
    
    #These are the replacements to be made. Based on: http://people.fas.harvard.edu/~kcampbel/diacrit.html        
    char_to_replace = {'Á' : '&Aacute;',
                       'á' : '&aacute;',
                       'À' : '&Agrave;',
                       'à' : '&agrave;',
                       'Â' : '&Acirc;',
                       'â' : '&acirc;',
                       'Ä' : '&Auml;',
                       'ä' : '&auml;',
                       'Ã' : '&Atilde;',
                       'ã' : '&atilde;',
                       'Å' : '&Aring;',
                       'å' : '&aring;',
                       'Æ' : '&Aelig;',
                       'æ' : '&aelig;',
                       'Ç' : '&Ccedil;',
                       'ç' : '&ccedil;', 
                       'Ð' : '&Eth;',
                       'ð' : '&eth;',
                       'É' : '&Eacute;',
                       'é' : '&eacute;',
                       'È' : '&Egrave;',
                       'è' : '&egrave;',
                       'Ê' : '&Ecirc;',
                       'ê' : '&ecirc;',
                       'Ë' : '&Euml;',
                       'ë' : '&euml;',
                       'Í' : '&Iacute;',
                       'í' : '&iacute;',
                       'Ì' : '&Igrave;',
                       'ì' : '&igrave;',
                       'Î' : '&Icirc;',
                       'î' : '&icirc;',
                       'Ï' : '&Iuml;',
                       'ï' : '&iuml;',
                       'Ñ' : '&Ntilde;',
                       'ñ' : '&ntilde;',
                       'Ó' : '&Oacute;',
                       'ó' : '&oacute;',
                       'Ò' :' &Ograve;',
                       'ò' : '&ograve;',
                       'Ô' : '&Ocirc;',
                       'ô' : '&ocirc;',
                       'Ö' : '&Ouml;',
                       'ö' : '&ouml;',
                       'Õ' : '&Otilde;',
                       'õ' : '&otilde',
                       'Ø' : '&Oslash;',
                       'ø' : '&osalsh;',
                       'ß' : '&szlig;',
                       'Þ' : '&Thorn;',
                       'þ' : '&thorn;',
                       'Ú' :  '&Uacute;',                       
                       'ú' : '&uacute:', 
                       'Ù' : '&Ugrave;',
                       'ù' : '&ugrave;',
                       'Û' : '&Ucirc;',
                       'û' : '&ucirc;',
                       'Ü' : '&Uuml;',
                       'ü' : '&uuml;',
                       'Ý' : '&Yacute;',
                       'ý' : '&yacute;',
                       'ÿ' : '&yuml;',
                       '©' : '&copy;', 
                       '®' : '&reg;', 
                       '™' : '&reg;',  
                       '<' : '&lt;', 
                       '>' : '&gt;', 
                       '€' : '&euro;', 
                       '¢' : '&cent;',
                       '£' : '&pound;',
                       #'"' : '&quot;',
                       '‘' : '&lsquo;',
                       '’' : '&rsquo;',
                       '“' : '&ldquo;',
                       '”' : '&rdquo;',
                       '«' : '&laquo;',
                       '»' : '&raquo;',
                       '—' : '&mdash;',
                       '–' : '&ndash;',
                       '°' : '&deg;',
                       '±' : '&plusmn;',
                       '¼' : '&frac14;',
                       '½' : '&frac12;',
                       '¾' : '&frac34',
                       '×' : '&times;',
                       '÷' : '&divide;',
                       'α' : '&alpha;',
                       'β' : '&beta;',
                       '∞' : '&infin;',
                       '@' : '&#64;',
                       '~' : '&#126;',
                       '¡' : '&#161;',
                       '¤' : '&#164;',
                       '¥' : '&#165;',
                       '¿' : '&#191;',
                       'º' : '&#186;',
                       'ª' : '&#170;',
                       '´' : '&#39;'}

    #We apply these replacements.
    for key, value in char_to_replace.items():
        # Replace key character with value character in string.
        data = data.replace(key, value)

    #We show the first 100 characters of the modified text.
    print("\nModified text:")
    print(data[0:100])

    #We saved the modified text in the new file.
    text_file = open(new_file, "w",encoding = 'utf-8-sig')
    n = text_file.write(data)
    text_file.close()

    print("\nBye ;)\n")


# In[ ]:


def translate_to_special(original_file, new_file):
    #original_file: Path to the file to be translated.
    #new_file: Path where the translated file will be saved.
    
    #Open the file in read mode. Based on: http://people.fas.harvard.edu/~kcampbel/diacrit.html
    print("TRANSLATING TO SPECIAL CHARACTERS")
    text_file = open(original_file, "r", encoding = 'utf-8-sig')
 
    #We read the whole file and save its content in a string.
    data = text_file.read()
 
    #We close the file.
    text_file.close()

    #We show all the different characters found in the text.
    print("\nThese characters have been found:")
    print(sorted(set(data)))

    #We also show the first 100 characters.
    print("\nOriginal text:")
    print(data[0:100])
    
    #These are the replacements to be made.        
    char_to_replace = {'&Aacute;' : 'Á',
                       '&aacute;' : 'á',
                       '&Agrave;' : 'À',
                       '&agrave;' : 'à',
                       '&Acirc;' : 'Â',
                       '&acirc;' : 'â',
                       '&Auml;' : 'Ä',
                       '&auml;' : 'ä',
                       '&Atilde;' : 'Ã',
                       '&atilde;' : 'ã',
                       '&Aring;' : 'Å',
                       '&aring;' : 'å',
                       '&Aelig;' : 'Æ',
                       '&aelig;' : 'æ',   
                       '&Ccedil;' : 'Ç',
                       '&ccedil;' : 'ç', 
                       '&Eth;' : 'Ð',
                       '&eth;' : 'ð',
                       '&Eacute;' : 'É',
                       '&eacute;' : 'é',
                       '&Egrave;' : 'È',
                       '&egrave;' : 'è',
                       '&Ecirc;' : 'Ê',
                       '&ecirc;' : 'ê',
                       '&Euml;' : 'Ë',
                       '&euml;' : 'ë',
                       '&Iacute;' : 'Í',
                       '&iacute;' : 'í',
                       '&Igrave;' : 'Ì',
                       '&igrave;' : 'ì',
                       '&Icirc;' : 'Î',
                       '&icirc;' : 'î',
                       '&Iuml;' : 'Ï',
                       '&iuml;' : 'ï',
                       '&Ntilde;':'Ñ',
                       '&ntilde;':'ñ',                      
                       '&Oacute;':'Ó',                      
                       '&oacute;':'ó',
                       '&Ograve;':'Ò',
                       '&ograve;': 'ò',
                       '&Ocirc;' : 'Ô',
                       '&ocirc;' : 'ô',
                       '&Ouml;' : 'Ö',
                       '&ouml;' : 'ö',
                       '&Otilde;' : 'Õ',
                       '&otilde;' : 'õ',
                       '&Oslash;' : 'Ø',
                       '&oslash;' : 'ø',
                       '&szlig;' : 'ß',
                       '&Thorn;' : 'Þ',
                       '&thorn;' : 'þ',
                       '&Uacute;' : 'Ú',                       
                       '&uacute:' : 'ú', 
                       '&Ugrave;' : 'Ù',
                       '&ugrave;' : 'ù',
                       '&Ucirc;' : 'Û',
                       '&ucirc;' : 'û',
                       '&Uuml;' : 'Ü',
                       '&uuml;': 'ü',
                       '&Yacute;' : 'Ý',
                       '&yacute;' : 'ý',
                       '&yuml;' : 'ÿ',
                       '&copy;' : '©', 
                       '&reg;' : '®', 
                       '&reg;' : '™',  
                       '&lt;' : '<', 
                       '&gt;' : '>', 
                       '&euro;' : '€', 
                       '&cent;' : '¢',
                       '&pound;' : '£',
                       '&quot;' : '"',
                       '&lsquo;' : '‘',
                       '&rsquo;' : '’',
                       '&ldquo;' : '“',
                       '&rdquo;' : '”',
                       '&laquo;' : '«',
                       '&raquo;' : '»',
                       '&mdash;' : '—',
                       '&ndash;' : '–',
                       '&deg;' : '°',
                       '&plusmn;' : '±',
                       '&frac14;' : '¼',
                       '&frac12;' : '½',
                       '&frac34' : '¾',
                       '&times;' : '×',
                       '&divide;' : '÷',
                       '&alpha;' : 'α',
                       '&beta;' : 'β',
                       '&infin;' : '∞',
                       '&#64;' : '@',
                       '&#126;' : '~',
                       '&#161;' : '¡',
                       '&#164;' : '¤',
                       '&#165;' : '¥',
                       '&#191;' : '¿',
                       '&#170;' : 'ª',
                       '&#186;' : 'º',
                       '&#39;' : '´'}

    #We apply these replacements.
    for key, value in char_to_replace.items():
        # Replace key character with value character in string.
        data = data.replace(key, value)

    #We show the first 100 characters of the modified text.
    print("\nModified text:")
    print(data[0:100])

    #We saved the modified text in the new file.
    text_file = open(new_file, "w",encoding = 'latin-1')
    text_file = open(new_file, "w",encoding = 'utf-8-sig')

    n = text_file.write(data)
    text_file.close()

    print("\nAdiós ;)\n")

