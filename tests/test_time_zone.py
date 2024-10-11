from lib.time_zone import *

def test_properties():
    tz = TimeZone("Paris", 1)
    assert tz.city == "Paris"
    assert tz.gmt_diff == 1

def test_move_zone():
    tz = TimeZone("Paris", 1)
    tz.move_zone("Cluj-Napoca", 3)
    assert tz.city == "Cluj-Napoca"
    assert tz.gmt_diff == 3
    tz.move_zone("Paris")
    assert tz.city == "Paris"
    assert tz.gmt_diff == 3
    tz.move_zone(gmt_diff=1)
    assert tz.city == "Paris"
    assert tz.gmt_diff == 1