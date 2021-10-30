#!/usr/bin/env python3

# pip 10.0 no longer supports pip.main() direct, use pip._internal
# if you have problems installing these packages from the script
# you can install from the prompt easily with 'pip install <package_name>'
#import pip._internal as pip
#package_names=['requests', 'beautifulsoup4'] #packages to install
#pip.main(['install'] + package_names + ['--upgrade'] + ['--quiet'])
import requests
import bs4


def print_list(list_data, list_type):
    print("\nHere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)


# download web page - get response object
resp = requests.get('https://www.gutenberg.org/catalog/',verify=False)
try:
    resp.raise_for_status()
except Exception as exc:
    print('Seems there was a problem: %s' % (exc))
print("\nyou should see '200' for status code:")
print(resp.status_code)
input("\npress Enter to continue...\n")

# create a beautifulsoup object from the text attribute of the response object
gut_soup = bs4.BeautifulSoup(resp.text, "html.parser")

# pull all css elements named <input> that have a name attribute with any value
elems = gut_soup.select('input[name]')
print("\nthere are {} elements of type '<input>[name]'".format(len(elems)))
print("... and here they are:")
for item in elems:
    print(item)
input("\npress Enter to continue...\n")
print("\ncheck the 'class' of one of the elements:")
print(type(elems[2]))
print("\nexamine the elements' attributes:")
for item in elems:
    print(item.attrs)
input("\npress Enter to exit...\n")