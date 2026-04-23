class ECU1Core:
    def __init__(self):
        self.speed = 0

    def update_speed(self, speed):
        self.speed = speed

    def get_state(self):
        return {"speed": self.speed}