python-social-auth-waveapps
===========================

Pluggable authentication backend for python-social-auth, that allows authentication via WaveApps.

*Currently only supports the Django strategy.*

## Installation instructions

From pypi

    $ pip install python-social-auth-waveapps

or clone from Github

    $ git clone git@github.com:ashchristopher/python-social-auth-waveapps.git
    $ cd python-social-auth-waveapps && sudo python setup.py install

## Pre-requisites

`python-social-auth` must be installed and configured first. Please visit the
[python-social-auth documentation](http://psa.matiasaguirre.net/docs/) for instructions.


## Configuration instructions

1. Add Waveapps backend to AUTHENTICATION_BACKENDS:

        AUTHENTICATION_BACKENDS = (
            'social_auth_waveapps.backends.WaveAppsOauth2',
            ...
            'django.contrib.auth.backends.ModelBackend',
        )

2. Add your Waveapps settings to your django `settings.py` file.

        SOCIAL_AUTH_WAVEAPPS_KEY = "..."
        SOCIAL_AUTH_WAVEAPPS_SECRET = "..."
        SOCIAL_AUTH_WAVEAPPS_DEFAULT_SCOPE = ['user.read', ]


## Changelog

### 0.2.0
* Adds the ability to refresh the access_token using the `refresh_token` method on the backend.

### 0.1.0
* Fixes install problem.

### 0.0.3
* Adds the `refresh_token`, `expires_in`, and `token_type` to the `extra_data` the **UserSocialAuth** instance.

### 0.0.1
* Initial release
