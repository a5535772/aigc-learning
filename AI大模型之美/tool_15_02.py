
import re
def parse_weather_info(weather_info: str) -> dict:
    # 将天气信息拆分成不同部分
    parts = weather_info.split('. ')

    # 解析天气
    weather = parts[0].strip()

    # 解析温度范围，并提取最小和最大温度
    temperature_range = parts[1].strip().replace('℃', '').split('/')
    temperature_max = int(temperature_range[0])
    temperature_min = int(temperature_range[1])

    # 解析风力
    wind_force = parts[2].strip()

    # 返回解析后的天气信息字典
    weather_dict = {
        'weather': weather,
        'temperature_min': temperature_min,
        'temperature_max': temperature_max,
        'wind_force': wind_force
    }

    return weather_dict

# 示例
# weather_info = "多云转阴. 36/28℃. 3-4级"
# weather_dict = parse_weather_info(weather_info)
# print(weather_dict)