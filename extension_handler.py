def get_extension_details(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
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
    extension_code = "".join(extension_code)
    #Split the string into individual lines
    extension_code = extension_code.split("\n")
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

def open_extension(file_path):
    details = get_extension_details(file_path)
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
    open_extension("extensions/Default.xt")