import numpy as np
import math

class LidarSensorReader:
    def __init__(self):
        self.distance_readings = np.zeros(360)
        self.angle_readings = np.zeros(360)
    
    def update_distance_readings(self, distance):
        self.distance_readings = distance
    
    def update_angle_readings(self, angle):
        self.angle_readings = angle
    
    def get_closest_obstacle_distance(self):
        min_distance = np.min(self.distance_readings)
        return min_distance
    
    def get_closest_obstacle_angle(self):
        min_distance_index = np.argmin(self.distance_readings)
        min_angle = self.angle_readings[min_distance_index]
        return min_angle
    
    def get_obstacle_distances(self):
        return self.distance_readings
    
    def get_obstacle_angles(self):
        return self.angle_readings
    
    def get_obstacle_distance_at_angle(self, angle):
        angle_index = math.floor(angle)
        distance = self.distance_readings[angle_index]
        return distance
    
    def get_obstacle_angle_at_distance(self, distance):
        distance_index = np.argmin(np.abs(self.distance_readings - distance))
        angle = self.angle_readings[distance_index]
        return angle