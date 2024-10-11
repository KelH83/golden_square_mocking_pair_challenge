from datetime import datetime, time, timedelta
import requests

class TimeHandler:
    def __init__(self, zone_list):
        self.zone_list = zone_list
    
    def add_zone(self, zone):
        self.zone_list.append(zone)
    
    def print_cities(self):
        cities = []
        for zone in self.zone_list:
            cities.append(zone.city)
        return ", ".join(cities)
    
    def get_current_gmt_time(self):
        # try `curl "http://worldtimeapi.org/api/timezone/GMT"` to see the
        # returned value we store in time_json
        time_json = requests.get("http://worldtimeapi.org/api/timezone/GMT")
        
        # date_time will look something like:
        # "2023-10-28T18:56:55.015943+00:00"
        date_time = datetime.fromisoformat(time_json.json()["datetime"])
        
        # returned string will be a time formatted such as "18:56"
        return time(date_time.hour, date_time.minute).isoformat(timespec="minutes")
    
    def print_current_time_zone_times(self):
        current_time = time.fromisoformat(self.get_current_gmt_time())
        cities_and_times = []
        
        for zone in self.zone_list:
            adjusted_time = time(current_time.hour + zone.gmt_diff, current_time.minute)
            cities_and_times.append(zone.city + " at " + adjusted_time.isoformat(timespec="minutes"))
        return "Times are " + ", ".join(cities_and_times)