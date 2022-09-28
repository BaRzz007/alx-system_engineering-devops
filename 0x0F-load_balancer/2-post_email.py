#!/usr/bin/python3
'''
Script takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and
displays the nody of the response (decoded in utf-8)
'''

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        body = html.decode()
        print(body)
