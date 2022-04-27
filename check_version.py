import requests
def get_version():
    url = 'https://joshuayacktman.wixsite.com/-jde'
    r = requests.get(url)
    r = r.text
    r = r.split("\n")
    version_line_location = str([x for x in r if 'Beta Version' in x])
    version_line_location = version_line_location.split('\"')
    for x in version_line_location:
        if 'Beta Version' in x:
            location_of_version = version_line_location.index(x)
    version = version_line_location[location_of_version]
    version = version.split('>')
    version = version[1]
    version = version.split('<')
    version = version[0]
    version = version.split(' ')
    version = version[2]
    return version