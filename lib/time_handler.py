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
        time_json = requests.get("http://worldtimeapi.org/api/timezone/GMT")
        date_time = datetime.fromisoformat(time_json.json()["datetime"])
        return time(date_time.hour, date_time.minute).isoformat(timespec="minutes")
    
    def print_current_time_zone_times(self):
        current_time = time.fromisoformat(self.get_current_gmt_time())
        cities_and_times = []
        
        for zone in self.zone_list:
            adjusted_time = time(current_time.hour + zone.gmt_diff, current_time.minute)
            cities_and_times.append(zone.city + " at " + adjusted_time.isoformat(timespec="minutes"))
        return "Times are " + ", ".join(cities_and_times)