from django.conf import settings

from social.backends.oauth import BaseOAuth2
from social.p3 import urlencode


class WaveAppsOauth2(BaseOAuth2):
    """ WaveApps OAuth2 authentication backend."""
    name = "waveapps"
    redirect_uri = ""
    AUTHORIZATION_URL = "https://api.waveapps.com/oauth2/authorize/"
    ACCESS_TOKEN_URL = "https://api.waveapps.com/oauth2/token/"
    ACCESS_TOKEN_METHOD = 'POST'
    REFRESH_TOKEN_URL = "https://api.waveapps.com/oauth2/token/"
    REFRESH_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = " "
    STATE_PARAMETER = True
    REDIRECT_STATE = False  # if this is set to True, we will get this error => "Registered redirect_uri doesn't match provided redirect_uri."
    DEFAULT_SCOPE = getattr(settings, 'SOCIAL_AUTH_WAVEAPPS_DEFAULT_SCOPE', ['user.read', ])
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token'),
        ('expires_in', 'expires'),
        ('token_type', 'token_type')
    ]

    def get_redirect_uri(self, state=None):
        # there is currently a bug in the latest release of python-social-auth
        # where the SOCIAL_AUTH_REDIRECT_IS_HTTPS settings is not respected so
        # this makes sure to replace the http:// with https:// if the settings
        # is True.
        #
        # see: https://github.com/omab/python-social-auth/pull/149
        #
        uri = super(WaveAppsOauth2, self).get_redirect_uri(state)
        if settings.SOCIAL_AUTH_REDIRECT_IS_HTTPS and uri:
            uri = uri.replace('http://', 'https://')
        return uri

    def get_user_details(self, response):
        email = None
        emails = response.get('emails', [])

        # Wave supports multiple emails per user, but only one default email.
        for email_entry in emails:
            if email_entry.get('is_default'):
                email = email_entry.get('email')
                break

        # if we can't select the default email, just use the first email in the list
        # because chances are there was only one email to begin with.
        if email is None:
            email = emails[0].get('email')

        user_details = {
            'username': response.get('id'),  # use Wave's user identifier hash as the username.
            'first_name': response.get('first_name'),
            'last_name': response.get('last_name'),
            'email': email,
        }
        return user_details

    def user_data(self, access_token, *args, **kwargs):
        url = "https://api.waveapps.com/user/"
        return self.get_json(url, params={'access_token': access_token})

    def refresh_token(self, token, *args, **kwargs):
        # python-social-auth doesn't give the right hooks to override just the url when refreshing the token
        # so we need to copy over the whole method.
        scope_params = urlencode(self.get_scope_argument())
        params = self.refresh_token_params(token, *args, **kwargs)

        # Wave's Oauth2 implementation requires that you send the scope as a URL paramater when refreshing the
        # token - this is a bug in their system.
        url = '{url}?{params}'.format(url=self.REFRESH_TOKEN_URL or self.ACCESS_TOKEN_URL, params=scope_params)
        method = self.REFRESH_TOKEN_METHOD
        key = 'params' if method == 'GET' else 'data'
        request_args = {'headers': self.auth_headers(), 'method': method, key: params}
        request = self.request(url, **request_args)
        return self.process_refresh_token_response(request, *args, **kwargs)
