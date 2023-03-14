import webbrowser
import sys
import argparse
import searcher_defs

version_num = 1.0
program_name = sys.argv[0]

parser = argparse.ArgumentParser(
                    prog=program_name,
                    usage=program_name + ' <options> -q <search query>',
                    description='A script for running google searches through cli'
                    )

parser.add_argument('--version',action='version', version=(program_name + ' ' + str(version_num)))
parser.add_argument('-a', '--all', action='store_true', 
                    help='search all sites, not just filtered sites')
parser.add_argument('-c','--custom', type=str, nargs='+', action='append', 
                    help='search a set of custom websites separated by a space. ex: example.com example2.com')
parser.add_argument('-q','--query', required=True, nargs='+', action='append',
                    help='required argument, the search you want to make')
args = parser.parse_args(sys.argv[1:])


# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
chrome_path = '/usr/bin/google-chrome %s'
firefox_path = '/usr/bin/firefox-esr %s'

# print(create_url())
webbrowser.get(firefox_path).open(create_url(args))