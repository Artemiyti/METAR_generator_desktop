# METAR Generator

The METAR Generator is a desktop application designed to create METAR reports using Tkinter in Python. This application allows users to input various weather parameters and generate a METAR report.

## Features

- User-friendly interface to input weather data
- Generate accurate METAR reports
- Supports various weather conditions, cloud types, and visibility options
- Calculates dew point based on temperature and relative humidity

## Installation

1. Clone the repository:
    
    bash
    
    Copy code
    
    `git clone https://github.com/ /METAR_generator.git`
    
2. Change to the project directory:
    
    bash
    
    Copy code
    
    `cd METAR_generator`
    
3. Install the required packages:
    
    bash
    
    Copy code
    
    `pip install -r requirements.txt`
    

## Usage

1. Run the application:
    
    bash
    
    Copy code
    
    `python metar_generator.py`
    
2. Fill in the required fields in the application interface:
    
    - **Airport**: Select the airport from the dropdown menu.
    - **Wind direction (º)**: Enter the wind direction in degrees.
    - **Wind speed (knot)**: Enter the wind speed in knots.
    - **Visibility Prevailing**: Enter the prevailing visibility.
    - **Visibility Minimum**: Enter the minimum visibility and select the direction from the dropdown menu.
    - **Present Weather**: Select intensity, description, precipitation, and reduced visibility options from the dropdown menus.
    - **Cloud layers**: Select cloud amount, type, and ceiling for up to three layers.
    - **Temperature (Cº)**: Enter the temperature in Celsius.
    - **Humidity (%)**: Enter the relative humidity percentage.
    - **Pressure QNH (hPa)**: Enter the QNH pressure in hectopascals.
    - **Horizon**: Select the horizon visibility from the dropdown menu.
    - **Contrast**: Select the contrast from the dropdown menu.
    - **Remarks**: Enter any additional remarks.
3. Click the "Generate" button to create the METAR report. The generated report will be displayed in the text box below.
    

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
