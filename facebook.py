import argparse
import requests
import copy

HEADERS = {
'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
'Accept-Language': 'en-US',
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'Keep-Alive',
'Cache-Control': 'no-cache'
}

LOGIN_HEADERS = copy.copy(HEADERS)
LOGIN_HEADERS['Referer'] = 'https://www.facebook.com/'

APP_HEADERS = copy.copy(HEADERS)
APP_HEADERS['Referer'] = 'https://www.facebook.com/games/'

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

APP_DATA = {
'app_id': '{app_id}',
'ref': 'appcenter_searchlist',
'redirect_uri':'https%3A%2F%2Fapps.facebook.com%2Fisidewith%2F%3Ffb_source%3Dappcenter%26fbs%3D110%26fb_appcenter%3D1&preview=0&fbs=110&__user={user_id}&__a=1&__dyn=7AmajEyl35xKt2u6aOGeFxq9ACxO4oKAdy8VFLHwxBx6ubzEeAq68K5Uc-dwIxbxjx2cxay28S7GCxebK8w&__req=k&fb_dtsg=AQHgkmz7bQfv&ttstamp=2658172103107109122559881102118&__rev=1769104'
}

LOGIN_COOKIES = {
'reg_fb_ref': 'https%3A%2F%2Fwww.facebook.com%2F',
'reg_fb_gate': 'https%3A%2F%2Fwww.facebook.com%2F',
'wd': '683x682'
}

SESSION_COOKIES = {'datr': 'XgZvVZ8thf_bz4AMYxSJj3Cn',}

ADD_APP_COOKIES = {'locale': 'en_US',
                   'p': '-2',
                   'presence':'EM433402077EuserFA21B09829534512A2EstateFDutF1433402077422Et2F_5b_5dElm2FnullEuct2F1433400273BEtrFA2loadA2EtwF2005180339EatF1433402076971Esb2F0CEchFDp_5f1B09829534512F0CC'}

FIDDLER_PROXY = {'http': "http://127.0.0.1:8888", 'https': "https://127.0.0.1:8888"}

class FacebookAccount(object):
    def __init__(self, username, password, fiddler, *args, **kwargs):
        self.username = username
        self.password = password
        self.fiddler = fiddler
        self.session = requests.Session()
        self.session.cookies.update(SESSION_COOKIES)
    
    def login(self):
        login_data = copy.copy(LOGIN_DATA)
        login_data['email'] = login_data['email'].format(email=self.username)
        login_data['pass'] = login_data['pass'].format(password=self.password)
        login_request = requests.Request('POST', 'https://www.facebook.com/login.php',
                                        params={'login_attempt':'1'},
                                        data=login_data,
                                        headers=LOGIN_HEADERS,
                                        cookies=LOGIN_COOKIES,
                                        )
                                        
        prepared_login = self.session.prepare_request(login_request)
        login_response = self.session.send(prepared_login, 
                          verify=False,
                          proxies=FIDDLER_PROXY if self.fiddler else None)
        
        

      
    # def add_app(self, app_id):
        # self.session.cookies.update(ADD_APP_COOKIES)
        # app_data = copy.copy(APP_DATA)
        # app_data['app_id'] = app_data['app_id'].format(app_id=app_id)
        # app_data['redirect_uri'] = app_data['redirect_uri'].format(user_id=self.session.cookies['c_user'])
        # add_app_request = requests.Request(
                                    # 'POST', 
                                    # 'https://www.facebook.com/ajax/appcenter/redirect_to_app',
                                    # data=app_data,
                                    # headers=APP_HEADERS,
                                    # )
        # prepared_add_app = self.session.prepare_request(add_app_request)
        # add_app_response = self.session.send(prepared_add_app, 
                          # verify=False,
                          # proxies=FIDDLER_PROXY if self.fiddler else None)
        # import pdb; pdb.set_trace()
        
    def add_app(self, app_id):
        self.session.cookies.update(ADD_APP_COOKIES)
        app_data = copy.copy(APP_DATA)
        app_data['app_id'] = app_data['app_id'].format(app_id=app_id)
        app_data['redirect_uri'] = app_data['redirect_uri'].format(user_id=self.session.cookies['c_user'])
        add_app_request = requests.Request(
                                    'GET', 
                                    'https://apps.facebook.com/isidewith/?fb_source=appcenter&fbs=110&fb_appcenter=1',
                                    headers=APP_HEADERS,
                                    )
        prepared_add_app = self.session.prepare_request(add_app_request)
        add_app_response = self.session.send(prepared_add_app, 
                          verify=False,
                          proxies=FIDDLER_PROXY if self.fiddler else None)
        import pdb; pdb.set_trace()
             
    
def install_app(username, password, fiddler, app_id, *args, **kwargs):
    facebook = FacebookAccount(username, password, fiddler)
    facebook.login()
    
    facebook.add_app(app_id)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default='alexramsey@mail.com')
    parser.add_argument('--password', default='alexramsey')
    parser.add_argument('--fiddler', default='True')
    
    subparsers = parser.add_subparsers()
    
    install_app_subparser = subparsers.add_parser('install')
    install_app_subparser.set_defaults(func=install_app)
    install_app_subparser.add_argument('--app_id', default='271262079571861')
    
    args = parser.parse_args()
    args.func(**vars(args))
