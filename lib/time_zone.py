class TimeZone:
    def __init__(self, city, gmt_diff):
        self.city = city
        self.gmt_diff = gmt_diff
    
    def move_zone(self, city=None, gmt_diff=None):
        if city:
            self.city = city
        if gmt_diff:
            self.gmt_diff = gmt_diff