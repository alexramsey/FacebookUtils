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


APP_DATA = 'fb_dtsg=AQGNxNSWC_iS&app_id={app_id}&redirect_uri=http%3A%2F%2Ffacebook2.poker.zynga.com%2Fpoker%2F%3Ffb_source%3Dsearch%26ref%3Dbr_tf&display=page&access_token=&sdk=&from_post=1&encoded_state=d42f7ffefbb577361a5221d9abf12562&public_info_nux=1&private=&login=&read=email%2Cuser_friends%2Cpublic_profile%2Cbaseline&write=&readwrite=&extended=&social_confirm=&confirm=&seen_scopes=email%2Cuser_friends%2Cpublic_profile%2Cbaseline&auth_type=&auth_token=&auth_nonce=&default_audience=&ref=Default&return_format=code&domain=&sso_device=&sheet_name=initial&__CONFIRM__=1&__user={user_id}&__a=1&__dyn=7AzkWpaz47pQ9UrBxl0wAwzx6bGexNLHwxBxCbwikq68K5UdoS2O2C4EvFoydxWFEvw&__req=2&ttstamp=265817178120788387679510583&__rev=1774062'

APP_DATA_2 = 'fb_dtsg=AQFMox4FJ5SV&scopes[0]=public_profile&gdpv4_source=page&__user={user_id}&__a=1&__dyn=7AmajEyl35xKt2u6aOGeFxq9ACxO4oKAdy8VFLHwxBx6ubzEeAq8zUK5Uc-dwIxbxjx2cxay28Sq5WBgjyXKi&__req=m&ttstamp=265817077111120527074538386&__rev=1774062'

LOGIN_COOKIES = {
'reg_fb_ref': 'https%3A%2F%2Fwww.facebook.com%2F',
'reg_fb_gate': 'https%3A%2F%2Fwww.facebook.com%2F',
'wd': '683x682'
}

SESSION_COOKIES = {'datr': 'XgZvVZ8thf_bz4AMYxSJj3Cn',}

ADD_APP_COOKIES = {'locale': 'en_US',
                   'p': '-2',
                   'presence':'EM433402077EuserFA21B09829534512A2EstateFDutF1433402077422Et2F_5b_5dElm2FnullEuct2F1433400273BEtrFA2loadA2EtwF2005180339EatF1433402076971Esb2F0CEchFDp_5f1B09829534512F0CC'}

MESSAGES_DATA = 'client=jewel&inbox[offset]=0&inbox[limit]=6&inbox[filter]&__user={user_id}&__a=1&__dyn=7Am8RW8BgNorDgDxyIGzGomyriKbx2mbyaFaayecqrWU8popyujhEeAq8zUK5Uc-dwIxbxb-qp2aCza88zpEnml1ebLp8&__req=o&fb_dtsg=AQEjoI8PPTPx&ttstamp=2658169106111735680808480120&__rev=1774062'
                   
FIDDLER_PROXY = {'http': "http://127.0.0.1:8888", 'https': "https://127.0.0.1:8888"}

def encode_params_no_percent_encoding(params):
    return "&".join("%s=%s" % (k,v) for k,v in params.items())

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
        
        
    def add_app(self, app_id):
        app_data = APP_DATA.format(app_id=app_id, user_id=self.session.cookies['c_user'])
        add_app_request = requests.Request(
                                    'POST', 
                                    'https://www.facebook.com/v2.0/dialog/oauth/read',
                                    headers=APP_HEADERS,
                                    data = app_data,
                                    )
        prepared_add_app = self.session.prepare_request(add_app_request)
        add_app_response = self.session.send(prepared_add_app, 
                          verify=False,
                          proxies=FIDDLER_PROXY if self.fiddler else None)
        
    def add_app2(self, app_id):
        app_data = APP_DATA_2.format(user_id=self.session.cookies['c_user'])
        add_app_request = requests.Request(
                                    'POST', 
                                    'https://www.facebook.com/ajax/appcenter/redirect_to_app?app_id={app_id}&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Ftexas_holdem%2F%3Ffbs%3D-1%26fb_appcenter%3D1&preview=0&fbs=-1'.format(app_id=app_id),
                                    headers=APP_HEADERS,
                                    data = app_data,
                                    )
        prepared_add_app = self.session.prepare_request(add_app_request)
        add_app_response = self.session.send(prepared_add_app, 
                          verify=False,
                          proxies=FIDDLER_PROXY if self.fiddler else None)
        
    def get_messages(self):
        get_messages_url = 'https://www.facebook.com/ajax/mercury/threadlist_info.php'
        get_messages_request = requests.Request(
                                    'POST', 
                                    get_messages_url,
                                    data=MESSAGES_DATA.format(user_id=self.session.cookies['c_user'])
                                    )
        prepared_get_message = self.session.prepare_request(get_messages_request)
        get_message_response = self.session.send(prepared_get_message, 
                          verify=False,
                          proxies=FIDDLER_PROXY if self.fiddler else None)
             
def install_app(username, password, fiddler, app_id, *args, **kwargs):
    facebook = FacebookAccount(username, password, fiddler)
    facebook.login()
    
    facebook.add_app(app_id)
    facebook.add_app2(app_id)
    
def messages(username, password, fiddler, *args, **kwargs):
    facebook = FacebookAccount(username, password, fiddler)
    facebook.login()
    
    messages = facebook.get_messages()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default='alexramsey@mail.com')
    parser.add_argument('--password', default='alexramsey')
    parser.add_argument('--fiddler', default='True')
    
    subparsers = parser.add_subparsers()
    
    install_app_subparser = subparsers.add_parser('install')
    install_app_subparser.set_defaults(func=install_app)
    install_app_subparser.add_argument('--app_id', default='2389801228')
    
    get_messages_parser = subparsers.add_parser('messages')
    get_messages_parser.set_defaults(func=messages)
    
    args = parser.parse_args()
    args.func(**vars(args))
