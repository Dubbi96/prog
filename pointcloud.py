import numpy as np
import pyvista as pv
from pyvista import examples

def generate_points(subset=0.02):
    dataset = examples.download_lidar()
    ids = np.random.randint(low=0, high=dataset.n_points-1,
                            size=int(dataset.n_points * subset))
    return dataset.points[ids]


points = generate_points()
print(points[0:5, :])

point_cloud = pv.PolyData(points)
print(point_cloud)
print(type(point_cloud))

np.allclose(points, point_cloud.points)

point_cloud.plot(eye_dome_lighting=True)

data = points[:,-1]

point_cloud["elevation"] = data

point_cloud.plot(render_points_as_spheres=True)
