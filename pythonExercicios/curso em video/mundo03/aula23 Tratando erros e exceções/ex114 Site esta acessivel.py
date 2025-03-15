# ======================================================================================================================
# Crie um codigo em Python que teste se o site Pudim esta acessivel pelo computador usado.
# (https://www.pudim.com.br)
# ======================================================================================================================

import urllib.request

try:
    site = urllib.request.FancyURLopener('https://www.pudim.com.br')
except urllib.error.URLError:
    print('no')
else:
    print('ye')