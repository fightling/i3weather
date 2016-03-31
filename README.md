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
    temp_unit=F
    [i3weather]
    format={short_status} - {temp} {temp_unit} - {wind_speed} Mph
    
Get `i3weather` with:

    pip install i3weather

Finally, modify your `.i3/config` to have the following and then restart i3:

    bar {
      position bottom
      status_command i3status | i3weather
      tray_output primary
    }

Formatting
----------
The following format fields are provided:
- `temp`: The current temperate
- `temp_unit`: The units of temperature (C or F)
- `pressure`: The current pressure in millibars
- `status`: A long status string (e.g. Broken Clouds)
- `short_status`: A short status string (e.g. Clouds)
- `wind_dir`: The direction of the wind in degrees
- `wind_speed`: The speed of the wind in miles per hour
- `location`: The name of the currently configured location
