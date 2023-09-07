import serial
import time

def read_vantage_data(port="COM2", verbose=True):
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = 19200
    ser.timeout = 5
    ser.open()

    # Wake up the console
    for attempt in range(5):
        if verbose:
            print(f"Waking up console attempt {attempt + 1}")
        ser.write(b'\n')
        time.sleep(4)
        response = ser.read(2)
        if response == b'\n\r':
            if verbose:
                print("Console is awake.")
            break

    # Request the data
    ser.write(b"LOOP 1\n")
    time.sleep(2)

    data = ser.read(99)
    print(data)
    data.hex()
    print(data)
    ser.close()

    # Decode data
    outside_temp_f = (data[14] << 8 | data[13]) / 10.0
    outside_temp_c = (outside_temp_f - 32) * 5 / 9

    inside_temp_f = (data[11] << 8 | data[10]) / 10.0
    inside_temp_c = (inside_temp_f - 32) * 5 / 9

    outside_humidity = data[34]
    inside_humidity = data[12]
    
    barometer = (((data[9] << 8) | data[8]) / 1000.0)*33.8639

    wind_direction = data[17]

    wind_speed_mph = data[15]
    wind_speed_kmh = wind_speed_mph * 1.6
    
    rain_rate_mm = data[43] * 0.2

    solar_radiation_lux = data[44]

    if verbose:
        print(f"Outside Temperature: {outside_temp_f:.2f} °F")
        print(f"Inside Temperature: {inside_temp_f:.2f} °F")
        print(f"Outside Humidity: {outside_humidity} %")
        print(f"Inside Humidity: {inside_humidity} %")
        print(f"Barometer: {barometer:.2f} hPa")
        print(f"Wind Direction: {wind_direction} degrees")
        print(f"Wind Speed: {wind_speed_kmh:.2f} km/h")
        print(f"Rain Rate: {rain_rate_mm:.2f} mm/h")
        print(f"Solar Radiation: {solar_radiation_lux:.2f} lux")

    return {
        "outside_temp_c": outside_temp_c,
        "inside_temp_c": inside_temp_c,
        "outside_humidity": outside_humidity,
        "inside_humidity": inside_humidity,
        "barometer": barometer,
        "wind_direction": wind_direction,
        "wind_speed_kmh": wind_speed_kmh,
        "rain_rate_mm": rain_rate_mm
    }

# Test
data_dict = read_vantage_data()
