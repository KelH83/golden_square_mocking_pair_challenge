from lib.time_zone import *
from lib.time_handler import *
import pytest

def test_properties():
    tz1 = TimeZone("Paris", 1)
    tz2 = TimeZone("Cluj-Napoca", 3)
    th = TimeHandler([tz1, tz2])
    assert th.zone_list == [tz1, tz2]

def test_list_cities():
    tz1 = TimeZone("Paris", 1)
    tz2 = TimeZone("Cluj-Napoca", 3)
    th = TimeHandler([tz1, tz2])
    assert th.print_cities() == "Paris, Cluj-Napoca"

def test_adding_zone():
    tz1 = TimeZone("Paris", 1)
    tz2 = TimeZone("Cluj-Napoca", 3)
    th = TimeHandler([tz1])
    assert th.zone_list == [tz1]
    th.add_zone(tz2)
    assert th.zone_list == [tz1, tz2]

@pytest.mark.skip(reason="not easily runnable")
def test_get_current_gmt_time():
    th = TimeHandler([])
    assert th.get_current_gmt_time() == "18:56"

@pytest.mark.skip(reason="not easily runnable")
def test_print_current_time_zone_times():
    tz1 = TimeZone("Paris", 1)
    tz2 = TimeZone("Cluj-Napoca", 3)
    th = TimeHandler([tz1, tz2])
    assert th.print_current_time_zone_times() == "Times are Paris at 19:56, Cluj-Napoca at 21:56"