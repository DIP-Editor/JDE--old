import requests
def get_version():
    url = 'https://jde-org.github.io/'
    r = requests.get(url)
    r = r.text
    r = r.split("\n")
    #  find line that contains "version =" and set as version_line_location
    version_line_location = 9
    # version_line_location = version_line_location.split('\"')
    # for x in version_line_location:
    #     if 'version = ' in x:
    #         location_of_version = version_line_location.index(x)
    version = r[version_line_location]
    version = version.split('>')
    version = version[0]
    version = version.split('<')
    version = version[1]
    version = version.split('\"')
    version = version[1]
    return version

if __name__ == '__main__':
    print(get_version())