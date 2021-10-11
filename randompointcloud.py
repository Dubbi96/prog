import numpy as np
import pyvista as pv
from pyvista import examples

def generate_points(subset=0.02):
    dataset = examples.download_lidar()
    ids = np.random.randint(low=0, high=dataset.n_points-1,
                            size=int(dataset.n_points * subset))
    return dataset.points[ids]


points = np.random.rand(2, 3)
point_cloud = pv.PolyData(points)


def compute_vectors(mesh):
    origin = mesh.center
    vectors = mesh.points - origin
    vectors = vectors / np.linalg.norm(vectors, axis=1)[:, None]
    return vectors

vectors = compute_vectors(point_cloud)
vectors[0:5, :]

point_cloud['vectors'] = vectors
print(point_cloud)
arrows = point_cloud.glyph(orient='vectors', scale=False, factor=0.15,)

# Display the arrows
plotter = pv.Plotter()
plotter.add_mesh(point_cloud, color='maroon', point_size=10.,
                 render_points_as_spheres=True)
plotter.add_mesh(arrows, color='lightblue')
# plotter.add_point_labels([point_cloud.center,], ['Center',],
#                          point_color='yellow', point_size=20)
plotter.show_grid()
plotter.show()