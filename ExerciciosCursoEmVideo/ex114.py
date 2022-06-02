import urllib.request

try:
    site = urllib.request.urlopen('https://www.jw.org/pt/')
except urllib.error.URLError:
    print('Site indisponivel')
else:
    print('Tudo ok!')
