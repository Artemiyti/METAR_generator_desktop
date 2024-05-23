import tkinter as tk
from datetime import datetime
import math

CLOUDS = {
    '  ': '', 'SKC: 0/8': 'SKC', 'FEW: 1-2/8': 'FEW', 'SCT: 3-4/8': 'SCT',
    'BKN: 5-7/8': 'BKN', 'OVC: 8/8': 'OVC'
}
DESCRIPTION = {
    '  ': '', 'MI shallow': 'MI', 'BC patches / broken': 'BC', 'PR partial': 'PR',
    'DR drifting': 'DR', 'BL blowing': 'BL', 'SH shower': 'SH', 'TS thunderstorm': 'TS',
    'FZ freezing': 'FZ'
}
PRECIPITATION = {
    '  ': '', 'DZ drizzle': 'DZ', 'RA rain': 'RA', 'SN snow': 'SN', 'SG snow grains': 'SG',
    'IC ice crystals': 'IC', 'PL ice pellets': 'PL', 'GR hail': 'GR', 'GS small hail or snow pellets (< 5mm)': 'GS'
}
VISIBILITY = {
    '  ': '', 'BR mist': 'BR', 'FG fog': 'FG', 'FU smoke': 'FU', 'VA volcanic ash': 'VA',
    'DU dust': 'DU', 'SA sand': 'SA', 'HZ haze': 'HZ'
}

def validate_cloud_height(height):
    try:
        height = int(height)
        return height // 100 if 100 < height < 99999 else 99999
    except ValueError:
        return '!!! ERROR in CLOUDS !!!'

def format_temperature(temp):
    try:
        temp = int(temp)
        return f'M{abs(temp)}' if temp < 0 else str(temp)
    except ValueError:
        return '!!! ERROR in TEMPERATURE !!!'

def format_pressure(pressure):
    try:
        pressure = int(pressure)
        return f'0{pressure}' if pressure < 1000 else str(pressure)
    except ValueError:
        return '!!! ERROR in PRESSURE !!!'

def format_wind_direction(direction):
    try:
        direction = int(direction)
        rounded_direction = round(direction / 10) * 10
        return f'{rounded_direction:03d}'
    except ValueError:
        return '!!! ERROR in WIND DIRECTION !!!'

def calculate_dew_point(temp, humidity):
    try:
        temp = int(temp)
        humidity = int(humidity)
        a, b = 17.27, 237.7
        es = 6.112 * math.exp((a * temp) / (temp + b))
        ea = (humidity / 100) * es
        dew_point = (b * math.log(ea / 6.112)) / (a - math.log(ea / 6.112))
        dew_point = round(dew_point)
        return f'M{abs(dew_point)}' if dew_point < 0 else str(dew_point)
    except ValueError:
        return '!!! ERROR in DEW POINT !!!'

def generate_metar():
    airport = airport_var.get()
    timestamp = datetime.utcnow().strftime("%d%H%MZ")
    wind_direction = format_wind_direction(wind_direction_entry.get())
    wind_speed = f'{wind_speed_entry.get()}KT'
    visibility = visibility_entry.get()
    min_visibility = f'{min_visibility_entry.get()}{min_visibility_dir_var.get()}'
    present_weather = f'{intensity_options[intensity_var.get()]}' \
                      f'{DESCRIPTION[description_var.get()]}' \
                      f'{PRECIPITATION[precipitation_var.get()]}' \
                      f'{VISIBILITY[visibility_var.get()]}'
    clouds = ' '.join(
        f'{CLOUDS[cloud_amount.get()]}{validate_cloud_height(cloud_entry.get())}' for cloud_amount, cloud_entry in
        [(cloud1_amount_var, cloud1_entry), (cloud2_amount_var, cloud2_entry), (cloud3_amount_var, cloud3_entry)]
    )
    temp = format_temperature(temperature_entry.get())
    dew_point = calculate_dew_point(temperature_entry.get(), humidity_entry.get())
    pressure = format_pressure(pressure_entry.get())

    metar = f'{airport} {timestamp} {wind_direction}{wind_speed} {visibility} {min_visibility} ' \
            f'{present_weather} {clouds} {temp}/{dew_point} Q{pressure}'

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, " ".join(metar.split()))

window = tk.Tk()
window.title('White Desert METAR Generator')

date = datetime.today().strftime("%d/%m/%Y")
tk.Label(window, text=f'Date: {date}').grid(row=1, column=0, sticky="e")
time = datetime.now().strftime("%H:%M")
tk.Label(window, text=f'Time: {time}').grid(row=1, column=6, sticky="w")

tk.Label(window, text='Airport').grid(row=2, column=1, sticky="w")
airport_options = ['WFR', 'WWA', 'ATKA', 'DIXIE']
airport_var = tk.StringVar(value=airport_options[0])
tk.OptionMenu(window, airport_var, *airport_options).grid(row=2, column=2, sticky="w")

tk.Label(window, text='Wind direction (º)').grid(row=3, column=1, sticky="w")
wind_direction_entry = tk.Entry(window, width=14)
wind_direction_entry.grid(row=3, column=2, sticky="w")

tk.Label(window, text='Wind speed (knot)').grid(row=4, column=1, sticky="w")
wind_speed_entry = tk.Entry(window, width=14)
wind_speed_entry.grid(row=4, column=2, sticky="w")

tk.Label(window, text='Visibility Prevailing').grid(row=5, column=1, sticky="w")
visibility_entry = tk.Entry(window, width=14)
visibility_entry.grid(row=5, column=2, sticky="w")

tk.Label(window, text='Visibility Minimum').grid(row=6, column=1, sticky="w")
min_visibility_entry = tk.Entry(window, width=14)
min_visibility_entry.grid(row=6, column=2, sticky="w")

min_visibility_directions = [' ', 'N', 'NE', 'NW', 'S', 'SE', 'SW', 'E', 'W']
min_visibility_dir_var = tk.StringVar(value=min_visibility_directions[0])
tk.OptionMenu(window, min_visibility_dir_var, *min_visibility_directions).grid(row=6, column=3, sticky="w")

tk.Label(window, text='Present Weather').grid(row=7, column=1, sticky="w")
intensity_options = {'NSW': 'NSW', 'moderate': '', '- light': '-', '+ heavy': '+', 'VC in the vicinity': 'VC'}
description_options = ['  ', 'MI shallow', 'BC patches / broken', 'PR partial', 'DR drifting', 'BL blowing',
                       'SH shower', 'TS thunderstorm', 'FZ freezing']
precipitation_options = ['  ', 'DZ drizzle', 'RA rain', 'SN snow', 'SG snow grains', 'IC ice crystals',
                         'PL ice pellets', 'GR hail', 'GS small hail or snow pellets (< 5mm)']
visibility_options = ['  ', 'BR mist', 'FG fog', 'FU smoke', 'VA volcanic ash', 'DU dust', 'SA sand', 'HZ haze']

intensity_var = tk.StringVar(value='NSW')
tk.OptionMenu(window, intensity_var, *intensity_options.keys()).grid(row=7, column=2, sticky="w")

description_var = tk.StringVar(value=description_options[0])
tk.OptionMenu(window, description_var, *description_options).grid(row=7, column=3, sticky="w")

precipitation_var = tk.StringVar(value=precipitation_options[0])
tk.OptionMenu(window, precipitation_var, *precipitation_options).grid(row=7, column=4, sticky="w")

visibility_var = tk.StringVar(value=visibility_options[0])
tk.OptionMenu(window, visibility_var, *visibility_options).grid(row=7, column=5, sticky="w")

tk.Label(window, text='Cloud L1 amount').grid(row=8, column=1, sticky="w")
cloud1_amount_var = tk.StringVar(value='SKC: 0/8')
tk.OptionMenu(window, cloud1_amount_var, *CLOUDS.keys()).grid(row=8, column=2, sticky="w")
tk.Label(window, text='Cloud L1 type').grid(row=8, column=3, sticky="w")
cloud1_entry = tk.Entry(window, width=14)
cloud1_entry.grid(row=8, column=4, sticky="w")

tk.Label(window, text='Cloud L2 amount').grid(row=9, column=1, sticky="w")
cloud2_amount_var = tk.StringVar(value='SKC: 0/8')
tk.OptionMenu(window, cloud2_amount_var, *CLOUDS.keys()).grid(row=9, column=2, sticky="w")
tk.Label(window, text='Cloud L2 type').grid(row=9, column=3, sticky="w")
cloud2_entry = tk.Entry(window, width=14)
cloud2_entry.grid(row=9, column=4, sticky="w")

tk.Label(window, text='Cloud L3 amount').grid(row=10, column=1, sticky="w")
cloud3_amount_var = tk.StringVar(value='SKC: 0/8')
tk.OptionMenu(window, cloud3_amount_var, *CLOUDS.keys()).grid(row=10, column=2, sticky="w")
tk.Label(window, text='Cloud L3 type').grid(row=10, column=3, sticky="w")
cloud3_entry = tk.Entry(window, width=14)
cloud3_entry.grid(row=10, column=4, sticky="w")

tk.Label(window, text='Temperature').grid(row=11, column=1, sticky="w")
temperature_entry = tk.Entry(window, width=14)
temperature_entry.grid(row=11, column=2, sticky="w")

tk.Label(window, text='Humidity').grid(row=11, column=3, sticky="w")
humidity_entry = tk.Entry(window, width=14)
humidity_entry.grid(row=11, column=4, sticky="w")

tk.Label(window, text='Pressure').grid(row=12, column=1, sticky="w")
pressure_entry = tk.Entry(window, width=14)
pressure_entry.grid(row=12, column=2, sticky="w")

result_text = tk.Text(window, height=5, width=60)
result_text.grid(row=13, column=1, columnspan=5, sticky="w")

tk.Button(window, text='Generate METAR', command=generate_metar).grid(row=14, column=1, columnspan=5)

window.mainloop()
