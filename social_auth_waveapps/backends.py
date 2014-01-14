from django.conf import settings

from social.backends.oauth import BaseOAuth2


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

    def get_redirect_uri(self, state=None):
        uri = super(WaveAppsOauth2, self).get_redirect_uri(state)
        if settings.SOCIAL_AUTH_REDIRECT_IS_HTTPS:
            uri = uri.replace('http://', 'https://')
        return uri

    def get_user_details(self, response):
        email = None
        emails = response.get('emails', [])

        for email_entry in emails:
            if email_entry.get('is_default'):
                email = email_entry.get('email')
                break

        if email is None:
            email = emails[0].get('email')

        user_details = {
            'first_name': response.get('first_name'),
            'last_name': response.get('last_name'),
            'email': email,
        }
        return user_details

    def user_data(self, access_token, *args, **kwargs):
        url = "https://api.waveapps.com/user/"
        return self.get_json(url, params={'access_token': access_token})