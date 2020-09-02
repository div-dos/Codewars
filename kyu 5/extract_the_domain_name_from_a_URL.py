def domain_name(url):
    if '//' in url:
        i = url.find('//')
        print(i)
        url = url[i+2:]
    if 'www.' in url:
        j = url.find('www.')
        url = url[j+4:]
        print(url)
    print(url.split('.'))
    return url.split('.')[0]