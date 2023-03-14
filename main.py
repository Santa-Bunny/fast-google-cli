# Created by Santa-Bunny
import webbrowser
import sys
import argparse
import browsers as b
import searcher_defs as s

version_num = 1.1
program_name = sys.argv[0]
browser_path = ''



def browser_choice():
    if args.browser_path == None:
        if args.browser == None:
            return b.chrome_path
        else:
            try:
                return b.get_browser_path(args.browser)
            except ValueError as e:
                print(e)
                sys.exit()
    else:
        return args.browser_path



parser = argparse.ArgumentParser(
                    prog=program_name,
                    usage=program_name + ' <options> -q <search query>',
                    description='A script for running google searches through cli',
                    epilog='browser-path takes priority over browser'
                    )

parser.add_argument('--version',action='version', version=(program_name + ' ' + str(version_num)))
parser.add_argument('-a', '--all', action='store_true', 
                    help='search all sites, not just filtered sites')
parser.add_argument('-c','--custom', type=str, nargs='+', action='append', 
                    help='search a set of custom websites separated by a space', metavar='example.com example2.com')
parser.add_argument('-q','--query', required=True, nargs='+', action='append',
                    help='required argument, the search you want to make', metavar='search query')
parser.add_argument('-p', '--browser-path', nargs=1, dest='browser_path')
parser.add_argument('-b', '--browser', nargs=1, 
                    help='What browser to use | default: chrome | Choices: chrome, firefox, firefox-esr, brave, opera, operagx, chromium, vivaldi, edge')
args = parser.parse_args(sys.argv[1:])


webbrowser.get(browser_choice()).open(s.create_url(args))