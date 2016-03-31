i3weather
=========

i3weather is a small wrapper around [PyOWM](https://github.com/csparpa/pyowm) to
add weather information to i3status.

Setup
-------------
Before use, you must get an API key from [OpenWeatherMap](http://openweathermap.org/).

Then, create a configuration file at `~/.i3weather` with the following:

    [owm]
    api_key=API_KEY_KERE
    location=Philadelphia,PA

Filling in the API key with your own, and location with your location.

Clone this repository and run `python setup.py install`.

Finally, edit your `.i3/config` and add:

    bar {
      position bottom
      status_command i3status | i3weather
      tray_output primary
    }
