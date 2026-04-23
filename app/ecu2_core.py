class ECU2Core:
    def __init__(self):
        self.speed = 0
        self.brake = False

    def update_speed(self, speed):
        self.speed = speed
        self.brake = speed > 80

    def get_state(self):
        return {"speed": self.speed, "brake": self.brake}