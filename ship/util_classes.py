import math


class Coords:
    """
    Для удобства жонглирования координатами
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_coords(self, velocity, rad):
        """
        Функция вычисления направления движения корабля относительно азимута
        
        Параметры

            velocity (float) - скорость корабля
            rad (float) - азимут корабля в радианах
        
        Если направление движения корабля можно выразить как вектор единичной длины:
        
            vec_v = (cos(rad), sin(rad)),
        
        и если корабль начал движение из точки (x0, y0) со скоростью velocity, 
        то через 1 шаг он сместится вдоль вектора vec_v на расстояние velocity:
            
            dx = x0 + velocity * cos(rad)
            dy = y0 + velocity * sin(rad)
        """
        self.x = round(self.x + velocity * math.cos(rad), 2)
        self.y = round(self.y + velocity *math.sin(rad), 2)


class Azimuth:
    """
    Для удобства жонглирования азимутом
    """

    def __init__(self, azimuth):
        self.azimuth = azimuth
        self.azimuth_in_rad = 0
        self.set_ship_heading_angle()

    def set_ship_heading_angle(self):
        """
        Функция рассчитывает радианы для дальнейших вычислений, 
        Для этого переводит азимут в “математический угол”, таким образом:
        angle = 90 - азимут и сразу переводим в радианы
        """
        self.azimuth_in_rad = round(math.radians(90 - self.azimuth), 5)

    def set_azimuth(self, azimuth):
        """
        Для дальнейшего удобства азимут сразу перевожу в радианы
        """
        self.azimuth = azimuth
        self.set_ship_heading_angle()
