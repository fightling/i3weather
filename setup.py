from setuptools import setup

setup(name='i3weather',
    version='1.0.0',
    description='Adds OpenWeatherMap data to i3status',
    author='Aaron Rosenfeld',
    author_email='aaron@rosenfeld.io',
    url='https://github.com/arosenfeld/i3weather',
    packages=[
        'i3weather',
    ],
    install_requires=['pyowm'],
    entry_points={
        'console_scripts': [
            'i3weather = i3weather.main:main',
        ]
    }
)
