from __future__ import absolute_import, division, print_function

import rospy
from rasberry_perception_pkg.dynamic_reconfigure import RealSenseCameraConfiguration
import random


def camera_reconfigure_example():
    rospy.init_node("camera_reconfigure_example", anonymous=True)
    config = RealSenseCameraConfiguration("linear_3dof_2d_camera")

    rate = rospy.Rate(5)

    laser_power = config.get_laser_power()
    rgb_exposure = config.get_rgb_exposure()

    laser_power_info = config.get_laser_power_info()
    laser_power_min, laser_power_max = laser_power_info['min'], laser_power_info['max']

    rgb_exposure_info = config.get_rgb_exposure_info()
    rgb_exposure_min, rgb_exposure_max = rgb_exposure_info['min'], rgb_exposure_info['max']

    while not rospy.is_shutdown():
        print("Current Laser Power='{}', RGB Exposure='{}'".format(config.get_laser_power(), config.get_rgb_exposure()))
        config.set_laser_power(random.uniform(laser_power_min, laser_power_max))
        config.set_rgb_exposure(random.randint(rgb_exposure_min, rgb_exposure_max))
        rate.sleep()


if __name__ == '__main__':
    camera_reconfigure_example()
