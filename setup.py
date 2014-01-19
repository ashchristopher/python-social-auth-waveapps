from setuptools import setup, find_packages


setup(
    name='python-social-auth-waveapps',
    version='0.2.0',
    packages=find_packages(),
    author='Ash Christopher',
    author_email='ash.christopher@gmail.com',
    description='Waveapps backend for python-social-auth.',
    long_description=open('README.md').read(),
    license='LICENSE',
    url='https://github.com/ashchristopher/python-social-auth-waveapps',
    keywords='django social auth oauth2 social-auth waveapps',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    install_requires=[
        'Django>=1.4',
        'python-social-auth',
    ]
)
