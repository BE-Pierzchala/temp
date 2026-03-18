from code.sql_worker import SqlWorker
import code.fetch_data as fetch_data
import code.CONFIG as config

import time
from datetime import datetime


def within_time_range():
    now = datetime.now().time()
    return config.START_TIME <= now <= config.END_TIME

def get_interval(temperature: float, humidity: float) -> int:
    high_temp = abs(temperature - config.MEDIAN_TEMPERATURE) > config.STD_TEMPERATURE
    high_hum = abs(humidity - config.MEDIAN_HUMIDITY) > config.STD_HUMIDITY

    if high_temp or high_hum:
        return config.HIGH_FREQUENCY
    elif within_time_range():
        return config.MID_FREQUENCY
    return config.LOW_FREQUENCY


def run_measurement() -> int:

    temperature, humidity, heat_index = fetch_data.get_data()

    if temperature is None or humidity is None or heat_index is None:
        return config.LOW_FREQUENCY

    with SqlWorker() as sql:
        sql.insert_data(temperature, humidity, heat_index)

    return get_interval(temperature, humidity)


def main_loop():
    while True:
        next_interval = run_measurement()
        time.sleep(next_interval)


if __name__ == "__main__":
    main_loop()