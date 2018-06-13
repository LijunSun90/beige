import numpy as np
# import matplotlib.pyplot as plt
import matplotlib.path as mpath

class CustomizedShape():
    def __init__(self):
        # Define the shape of a robot.
        shape_description_robot = [
            (1., 2., mpath.Path.MOVETO),
            (1., 1., mpath.Path.LINETO),
            (2., 1., mpath.Path.LINETO),
            (2., -1., mpath.Path.LINETO),
            (1., -1., mpath.Path.LINETO),
            (1., -2., mpath.Path.LINETO),
            (-1., -2., mpath.Path.LINETO),
            (-1., -1., mpath.Path.LINETO),
            (-2., -1., mpath.Path.LINETO),
            (-2., 1., mpath.Path.LINETO),
            (-1., 1., mpath.Path.LINETO),
            (-1., 2., mpath.Path.LINETO),
            (0., 0., mpath.Path.CLOSEPOLY),
        ]
        u, v, codes = zip(*shape_description_robot)
        self.marker_robot = mpath.Path(np.asarray((u, v)).T, codes)

        # Define the shape of a target.
        shape_description_target = [
            (np.cos(72*3.25*np.pi/180), np.sin(72*3.25*np.pi/180), mpath.Path.MOVETO),
            (np.cos(72*1.25*np.pi/180), np.sin(72*1.25*np.pi/180), mpath.Path.LINETO),
            (np.cos(72*4.25*np.pi/180), np.sin(72*4.25*np.pi/180), mpath.Path.LINETO),
            (np.cos(72*2.25*np.pi/180), np.sin(72*2.25*np.pi/180), mpath.Path.LINETO),
            (np.cos(72*0.25*np.pi/180), np.sin(72*0.25*np.pi/180), mpath.Path.LINETO),
            (np.cos(72*3.25*np.pi/180), np.sin(72*3.25*np.pi/180), mpath.Path.LINETO),
            (0., 0., mpath.Path.CLOSEPOLY),
        ]
        u, v, codes = zip(*shape_description_target)
        self.marker_target = mpath.Path(np.asarray((u, v)).T, codes)


# data = np.random.rand(8, 8)
# plt.scatter(data[:, 0], data[:, 1], c='0.75', marker=CustomizedShape().marker_robot, s=64)
# plt.show()