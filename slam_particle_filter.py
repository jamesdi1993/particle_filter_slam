from load_data import load_data
from map import Map
from utils.map_utils import transform_to_lidar_frame, transform_from_lidar_to_body_frame,\
  tranform_from_body_to_world_frame
from utils.robot_utils import LIDAR_ANGLES

import numpy as np

if __name__ == '__main__':
  # Load data
  data = load_data(dataset_index = 20)
  config = {
    'res': 0.25,
    'xmin': -10,
    'xmax': 10,
    'ymin': -10,
    'ymax': 10
  }
  
  # Initialize map;
  map = Map(config)
  map.plot(epoch = 1)

  # Transform the lidar data to the body frame;
  lidar_data = data['lidar_ranges']
  lidar_xy = transform_to_lidar_frame(lidar_data, LIDAR_ANGLES)
  lidar_body = transform_from_lidar_to_body_frame(lidar_xy)

  # return position of the robot;
  position = np.array([[0],[0],[0]])
  lidar_world = tranform_from_body_to_world_frame(position, lidar_body)
  print("The shape of the lidar rays in world frame is: %s" % (lidar_world.shape,))