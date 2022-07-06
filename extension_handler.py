import requests
import sys
from pathlib import Path
if getattr(sys, 'frozen', False):
    folder = Path(sys._MEIPASS)
else:
    folder = Path(__file__).parent
def get_extension_details(web_path):
    lines = requests.get("{}".format(web_path), timeout=.3).text.split("\n")
    #Remove first 25 lines 
    lines = lines[25:]
    extension_type = lines[0]
    extension_permissions = lines[1]
    extension_name = lines[2]
    extension_description = lines[3]
    extension_author = lines[4]
    #Everything after the fifth line is the extension code
    extension_code = lines[5:]
    return (extension_type, extension_permissions, extension_name, extension_description, extension_author, extension_code)

def parse_extension_code(extension_code, extension_permissions):
    #Code is split into blocks formated with <keywords></keywords>, <settings></settings>, <color_theme></color_theme> <font></font>
    #<keywords>
    #</keywords>
    #<settings>
    #</settings>
    #<color_theme>
    #</color_theme>
    #<font>
    #</font>
    #Turn extension code into a string
    return_tuple = ()
    if "keywords" in extension_permissions:
        keyword_start = extension_code.index("<keywords>")
        keyword_end = extension_code.index("</keywords>")
        keywords = extension_code[keyword_start+1:keyword_end]
        return_tuple += (keywords,)
    else:
        return_tuple += (None,)
    if "settings" in extension_permissions:
        settings_start = extension_code.index("<settings>")
        settings_end = extension_code.index("</settings>")
        settings = extension_code[settings_start+1:settings_end]
        return_tuple += (settings,)
    else:
        return_tuple += (None,)
    if "color_theme" in extension_permissions:
        color_theme_start = extension_code.index("<color_theme>")
        color_theme_end = extension_code.index("</color_theme>")
        color_theme = extension_code[color_theme_start+1:color_theme_end]
        return_tuple += (color_theme,)
    else:
        return_tuple += (None,)
    if "font" in extension_permissions:
        font_start = extension_code.index("<font>")
        font_end = extension_code.index("</font>")
        font = extension_code[font_start+1:font_end]
        return_tuple += (font,)
    else:
        return_tuple += (None,)
    return return_tuple
def open_extension(web_path):
    details = get_extension_details(web_path)
    extension_type = details[0]
    extension_permissions = details[1]
    extension_name = details[2]
    extension_description = details[3]
    extension_author = details[4]
    extension_code = details[5]
    extension_code = parse_extension_code(extension_code, extension_permissions)
    keywords = extension_code[0]
    settings = extension_code[1]
    color_theme = extension_code[2]
    font = extension_code[3]
    return (extension_type, extension_permissions, extension_name, extension_description, extension_author, keywords, settings, color_theme, font)
def get_list_items():
    r = requests.get("https://jde-org.github.io/extensions.html")
    r = str(r.text)
    r = r.split("<ul>")[-1]
    r = r.split("</ul>")[0]
    r = r.split("<li>")[1:]
    for i in range(len(r)):
        r[i] = r[i].split("\n                        ")[1]
        r[i] = r[i].split("\">")[0]
        r[i] = r[i].split("<a href=\"")[1]
    return r
def get_test_details(filename):
    lines = open(folder / filename, "r").readlines()
    #Remove first 25 lines
    lines = lines[25:]
    extension_type = lines[0]
    extension_permissions = lines[1]
    extension_name = lines[2]
    extension_description = lines[3]
    extension_author = lines[4]
    #Everything after the fifth line is the extension code
    extension_code = lines[5:]
    return (extension_type, extension_permissions, extension_name, extension_description, extension_author, extension_code)
def open_test_extension(filename):
    details = get_test_details(filename)
    extension_type = details[0]
    extension_permissions = details[1]
    extension_name = details[2]
    extension_description = details[3]
    extension_author = details[4]
    extension_code = details[5]
    extension_code = parse_extension_code(extension_code, extension_permissions)
    keywords = extension_code[0]
    settings = extension_code[1]
    color_theme = extension_code[2]
    font = extension_code[3]
    return (extension_type, extension_permissions, extension_name, extension_description, extension_author, keywords, settings, color_theme, font)
if __name__ == "__main__":
    print(open_extension("https://jde-org.github.io/extensions/Default.xt"))