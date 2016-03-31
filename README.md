i3weather
=========

i3weather is a small wrapper around [PyOWM](https://github.com/csparpa/pyowm) to
add weather information to i3status.

Setup
-------------
Before use, you must get an API key from [OpenWeatherMap](http://openweathermap.org/).

Then, create a configuration file at `~/.i3weather`, filling in the appropriate information:

    [owm]
    api_key=API_KEY_KERE
    location=Philadelphia,PA
    
Get `i3weather` with:

    pip install i3weather

Finally, modify your `.i3/config` to have the following and then restart i3:

    bar {
      position bottom
      status_command i3status | i3weather
      tray_output primary
    }
