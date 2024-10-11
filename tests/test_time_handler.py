from lib.time_handler import *
from unittest.mock import Mock
from datetime import datetime, time
import pytest

def test_properties():
    tz1 = Mock()
    tz2 = Mock()
    th = TimeHandler([tz1, tz2])
    assert th.zone_list == [tz1, tz2]

def test_list_cities():
    tz1 = Mock()
    tz2 = Mock()
    tz1.city = "Paris"
    tz2.city = "Cluj-Napoca"
    th = TimeHandler([tz1, tz2])
    assert th.print_cities() == "Paris, Cluj-Napoca"

def test_adding_zone():
    tz1 = Mock()
    tz2 = Mock()
    th = TimeHandler([tz1])
    assert th.zone_list == [tz1]
    th.add_zone(tz2)
    assert th.zone_list == [tz1, tz2]


def test_get_current_gmt_time():
    th = TimeHandler([])
    time_now = requests.get("http://worldtimeapi.org/api/timezone/GMT")
    formatted_time = datetime.fromisoformat(time_now.json()["datetime"])
    correct_time = time(formatted_time.hour, formatted_time.minute).isoformat(timespec="minutes")
    assert th.get_current_gmt_time() == correct_time

def test_print_current_time_zone_times():
    tz1 = Mock()
    tz2 = Mock()
    tz1.city = "Paris"
    tz2.city = "Cluj-Napoca"
    tz1.gmt_diff = 1
    tz2.gmt_diff = 3
    th = TimeHandler([tz1, tz2])
    current_time = time.fromisoformat(th.get_current_gmt_time())
    tz1_time = time(current_time.hour + 1, current_time.minute).isoformat(timespec="minutes")
    tz2_time = time(current_time.hour + 3, current_time.minute).isoformat(timespec="minutes")
    assert th.print_current_time_zone_times() == f"Times are Paris at {tz1_time}, Cluj-Napoca at {tz2_time}"