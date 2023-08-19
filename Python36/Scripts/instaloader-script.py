#!c:\users\99450\appdata\local\programs\python\python36\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'instaloader==4.9.5','console_scripts','instaloader'
__requires__ = 'instaloader==4.9.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('instaloader==4.9.5', 'console_scripts', 'instaloader')()
    )
