# Vantage Data Reader

This script provides a function to read and interpret data from a Vantage weather station.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Output](#output)
- [Author](#author)
- [License](#license)

## Setup

1. **Clone the Repository**

   \```bash
   git clone [https://github.com/F3rNaNDEZ57/Davis_VantagePro2_Serial_communication]
   \```

2. **Navigate to Directory**

   \```bash
   cd path-to-your-repo
   \```

3. **Install Dependencies**

   ```\bash
   pip install -r requirements.txt
   \```

4. **Python Version**
   
   Ensure you have Python 3.x installed.

## Usage

By default, the `read_vantage_data` function will attempt to read data from the serial port labeled `COM2`. You can adjust the port and verbosity using the function's parameters.

Example:
\```python
data_dict = read_vantage_data(port="COM3", verbose=True)
\```

## Output

When `verbose` is set to `True`, the function will print the following weather data:

- **Outside Temperature:** (°F)
- **Inside Temperature:** (°F)
- **Outside Humidity:** (%)
- **Inside Humidity:** (%)
- **Barometer:** (hPa)
- **Wind Direction:** (degrees)
- **Wind Speed:** (km/h)
- **Rain Rate:** (mm/h)
- **Solar Radiation:** (lux)

The function also returns a dictionary with parsed data values in metric units.

## Author

[Fernando WKD]


