import numpy as np

# AQI Breakpoints
# https://en.wikipedia.org/wiki/Air_quality_index#Computing_the_AQI
o3_breakpoints = np.array([0, 55, 71, 86, 106])  # ppb
pm25_breakpoints = np.array([0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5])  # micrograms per cubic meter
pm10_breakpoints = np.array([0, 55, 155, 255, 355, 425, 505])  # micrograms per cubic meter


def closest_breakpoints(target, arr):
    idx = arr[arr <= target].argmax()
    base_break = arr[idx]
    ceil_break = arr[idx + 1]
    base_aqi = 0
    ceil_aqi = 0
    if idx == 0:
        base_aqi = 0
        ceil_aqi = 50
    else:
        base_aqi = 50 * idx
        ceil_aqi = 50 * (idx + 1)
    return base_break, ceil_break, base_aqi, ceil_aqi


def o3_aqi(o3_ppb):
    base_break, ceil_break, base_aqi, ceil_aqi = closest_breakpoints(o3_ppb, o3_breakpoints)

    aqi_val = base_aqi + (((ceil_aqi - base_aqi)/(ceil_break - base_break)) * (o3_ppb - base_break))

    return aqi_val


