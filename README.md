python-social-auth-waveapps
===========================

Authentication backend for python-social-auth. Currently only supports the Django strategy.

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
