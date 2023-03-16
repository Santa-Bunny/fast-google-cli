import platform

OS = platform.system()

WEBSITES = [
    'chrome', 
    'firefox', 
    'safari', 
    'firefox-esr', 
    'brave', 
    'opera', 
    'operagx', 
    'chromium', 
    'vivaldi', 
    'edge',
]


if OS == 'Darwin':
    # MacOS
    SAFARI_PATH = 'open -a /Applications/Safari.app %s'
    CHROME_PATH = 'open -a /Applications/Google\ Chrome.app %s'
    FIREFOX_PATH = 'open -a /Applications/Firefox.app %s'
    OPERA_PATH = 'open -a /Applications/Opera.app %s'
    OPERAGX_PATH = 'open -a /Applications/Opera\ GX.app %s'
    VIVALDI_PATH = 'open -a /Applications/Vivaldi.app %s'
    BRAVE_PATH = 'open -a /Applications/Brave\ Browser.app %s'
    EDGE_PATH = 'open -a /Applications/Microsoft\ Edge %s'
elif OS == 'Windows':
    # Windows
    CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    FIREFOX_PATH = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
    BRAVE_PATH = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
    OPERA_PATH = 'C:/Program Files/opera/launcher.exe %s'
    OPERAGX_PATH = 'C:/Program Files/opera GX/launcher.exe %s'
    VIVALDI_PATH = 'C:/Program Files/Vivaldi/Application/vivaldi.exe %s'
    EDGE_PATH = 'C:/Windows/SystemApps/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/MicrosoftEdge.exe %s'
else:
    # Linux
    CHROME_PATH = '/usr/bin/google-chrome %s'
    FIREFOX_PATH = '/usr/bin/firefox %s'
    CHROMIUM_PATH = '/usr/bin/chromium %s'
    FIREFOXESR_PATH = '/usr/bin/firefox-esr %s'
    BRAVE_PATH = '/usr/bin/brave-bin %s'

def get_browser_path(arg):
    if arg[0] == 'chrome':
        return CHROME_PATH
    elif arg[0] == 'firefox':
        return FIREFOX_PATH
    elif arg[0] == 'safari':
        return SAFARI_PATH
    elif arg[0] == 'brave':
        return BRAVE_PATH
    elif arg[0] == 'opera':
        return OPERA_PATH
    elif arg[0] == 'operagx':
        return OPERAGX_PATH
    elif arg[0] == 'chromium':
        return CHROMIUM_PATH
    elif arg[0] == 'vivaldi':
        return VIVALDI_PATH
    elif arg[0] == 'edge':
        return EDGE_PATH
    elif arg[0] == 'firefox-esr':
        return FIREFOXESR_PATH
    else:
        raise ValueError('error: invalid browser option: %s'%(arg[0]))