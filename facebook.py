import argparse
import requests

LOGIN_HEADERS = {
'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
'Referer': 'https://www.facebook.com/',
'Accept-Language': 'en-US',
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'Keep-Alive',
'Cache-Control': 'no-cache'
}

LOGIN_DATA = {
'lsd': 'AVpx0-qJ',
'email': '{email}',
'pass': '{password}',
'default_persistent': '0',
'timezone': '420',
'lgndim':'',
'lgnrnd': '065326_7IbY',
'lgnjs': '1433339605',
'locale': 'en_US',
'qsstamp':'W1tbMjIsODIsODcsOTIsMTEzLDEyNiwxNDcsMTYxLDE3MCwxODAsMTgyLDE4MywxOTUsMjAzLDIwNCwyMjEsMjI4LDI0OCwyNTEsMjYyLDMxNCwzMjAsMzIyLDMzNCwzNDgsMzQ5LDM1MSwzNTMsMzU2LDM2MiwzNzgsNDE4LDQ3OSw0ODEsNDg4LDUxNiw1MjksNTMwLDYyOSw2NTQsNjkxLDczMF1dLCJBWm14ZXE2RzY1cFJJU1owSW5MRUhzX2tJX2dmT25TQWpBbTdyMVRJbGsyR3kxZm9vaGJVTmNueTFrbFVtaG9RZllGWElqbGRjMjBNdjR5MEwzN1ppTEpQVkJfb0Z3SXo1Wm93aVVtRnhwTk15TzNQMXo2X2ZQWmpiV1JCMC1QYUt0LVlCVXlGVXNuVmJuc3IwcEpJekF6SHllTDBiOUFzZHlhR2ZEYi1WaVJSNi1OanZIbUVPa2x4aG9jVEpDeHNXd1FvaEd0NnpvYURIcXhYOTVHZHRXREVxZEc1cVNjV2dVRjdpak81d0s0MFVjZlA2Rms0WHN0YVhJWmd4NGplN240Il0%3D'
}

LOGIN_COOKIES = {
'reg_fb_ref': 'https%3A%2F%2Fwww.facebook.com%2F',
'reg_fb_gate': 'https%3A%2F%2Fwww.facebook.com%2F',
'datr': 'XgZvVZ8thf_bz4AMYxSJj3Cn',
'wd': '683x682'
}

FIDDLER_PROXY = {'http': "http://127.0.0.1:8888", 'https': "https://127.0.0.1:8888"}

class FacebookAccount(object):
    def __init__(self, username, password, fiddler, *args, **kwargs):
        self.username = username
        self.password = password
        self.fiddler = fiddler
    
    def login(self):
        LOGIN_DATA['email'] = LOGIN_DATA['email'].format(email=self.username)
        LOGIN_DATA['pass'] = LOGIN_DATA['pass'].format(password=self.password)
        login_request = requests.request('POST', 'https://www.facebook.com/login.php',
                                        params={'login_attempt':'1'},
                                        data=LOGIN_DATA,
                                        headers=LOGIN_HEADERS,
                                        cookies=LOGIN_COOKIES,
                                        verify=False,
                                        proxies=FIDDLER_PROXY if self.fiddler else None)
        import pdb; pdb.set_trace()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default='alexramsey@mail.com')
    parser.add_argument('--password', default='alexramsey')
    parser.add_argument('--fiddler', default='True')
    
    args = parser.parse_args()
    
    facebook = FacebookAccount(**vars(args))
    facebook.login()