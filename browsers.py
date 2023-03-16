import platform

OS = platform.system()

Websites = [
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
    safari_path = 'open -a /Applications/Safari.app %s'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    firefox_path = 'open -a /Applications/Firefox.app %s'
    opera_path = 'open -a /Applications/Opera.app %s'
    operagx = 'open -a /Applications/Opera\ GX.app %s'
    vivaldi_path = 'open -a /Applications/Vivaldi.app %s'
    brave_path = 'open -a /Applications/Brave\ Browser.app %s'
    edge_path = 'open -a /Applications/Microsoft\ Edge %s'
elif OS == 'Windows':
    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
    brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
    opera_path = 'C:/Program Files/opera/launcher.exe %s'
    operagx_path = 'C:/Program Files/opera GX/launcher.exe %s'
    vivaldi_path = 'C:/Program Files/Vivaldi/Application/vivaldi.exe %s'
    edge_path = 'C:/Windows/SystemApps/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/MicrosoftEdge.exe %s'
else:
    # Linux
    chrome_path = '/usr/bin/google-chrome %s'
    firefox_path = '/usr/bin/firefox %s'
    chromium_path = '/usr/bin/chromium %s'
    firefoxesr_path = '/usr/bin/firefox-esr %s'
    brave_path = '/usr/bin/brave-bin %s'

def get_browser_path(arg):
    if arg[0] == 'chrome':
        return chrome_path
    elif arg[0] == 'firefox':
        return firefox_path
    elif arg[0] == 'safari':
        return safari_path
    elif arg[0] == 'brave':
        return brave_path
    elif arg[0] == 'opera':
        return opera_path
    elif arg[0] == 'operagx':
        return operagx_path
    elif arg[0] == 'chromium':
        return chromium_path
    elif arg[0] == 'vivaldi':
        return vivaldi_path
    elif arg[0] == 'edge':
        return edge_path
    elif arg[0] == 'firefox-esr':
        return firefoxesr_path
    else:
        raise ValueError('error: invalid browser option: %s'%(arg[0]))