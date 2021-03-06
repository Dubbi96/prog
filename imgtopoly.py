import os
import os.path
import shutil
from PIL import Image
import numpy as np
import pyvista as pv

#원 데이터 경로
glob_path = "C:/Users/Dell/2dtodepth/2dtodepth/spm/outfile/"

file_list = os.listdir(glob_path)
file_list_jpg1 = []
file_list_png1 = []

file_list_jpg = [file for file in file_list if file.endswith(".jpg")]
file_list_png = [file for file in file_list if file.endswith(".png")]

for i in range(0,len(file_list_jpg)):
    #데이터 이름만 추출
    file_list_jpg1.append(file_list_jpg[i].split('.jp')[0])
for i in range(0,len(file_list_png)):
    file_list_png1.append(file_list_png[i].split('.pn')[0])

for k in range(0,len(file_list_jpg1)):
    reshaped_list1 = []
    reshaped_list3 = []
    img = Image.open(glob_path + file_list_jpg1[k] + '.jpg').convert("L")
    grayimg1 = np.asarray(img.getdata()).reshape(img.size[1], img.size[0], -1)
    print(grayimg1)
    print(type(grayimg1))
    print(glob_path + file_list_jpg1[k] + '.jpg')
    print(grayimg1.shape)
    
    reshaped_gi1 = grayimg1.reshape(288,1024)
    for i in range(0,reshaped_gi1.shape[0]):
        for j in range (0, reshaped_gi1.shape[1]):
            reshaped_list1.append([i,j,reshaped_gi1[i][j]])
            
    # for i in range(0,reshaped_gi1.shape[0]):
        # for j in range (513, reshaped_gi1.shape[1]):
            # reshaped_list3.append([i,j,(reshaped_gi1[i][j]+reshaped_gi1[i][j-512])/2])
            
    reshaped_polydata1 = np.array(reshaped_list1)
    # reshaped_polydata3 = np.array(reshaped_list3)
    print(reshaped_polydata1)
    print(type(reshaped_polydata1))
    
    #polydata 1
    point_cloud = pv.PolyData(reshaped_polydata1)

    np.allclose(reshaped_polydata1, point_cloud.points)

    point_cloud.plot(eye_dome_lighting=True)
    
    point_cloud.save(glob_path + file_list_jpg1[k] + '.vtk')
    
    data = reshaped_polydata1[:,-1]

    point_cloud["elevation"] = data
    
    point_cloud.plot(render_points_as_spheres=True)
    
    # #polydata 3
    # point_cloud = pv.PolyData(reshaped_polydata3)

    # np.allclose(reshaped_polydata3, point_cloud.points)

    # point_cloud.plot(eye_dome_lighting=True)

    # data = reshaped_polydata3[:,-1]

    # point_cloud["elevation"] = data

    # point_cloud.plot(render_points_as_spheres=True)

for k in range(0,len(file_list_png1)):
    reshaped_list2 = []
    reshaped_list4 = []
    img = Image.open(glob_path + file_list_png1[k] + '.png').convert("L")
    grayimg2 = np.asarray(img.getdata(glob_path + file_list_png1[k] + '.png')).reshape(img.size[1], img.size[0], -1)
    print(type(grayimg2))
    print(glob_path + file_list_png1[k] + '.png')
    print(grayimg2.shape)
    reshaped_gi2 = grayimg2.reshape(288,1024)
    for i in range(0,reshaped_gi2.shape[0]):
        for j in range (0, reshaped_gi2.shape[1]):
            reshaped_list2.append([i,j,reshaped_gi2[i][j]])
    
    # for i in range(0,reshaped_gi1.shape[0]):
        # for j in range (513, reshaped_gi1.shape[1]):
            # reshaped_list4.append([i,j,(reshaped_gi2[i][j]+reshaped_gi2[i][j-512])/2])
    
    reshaped_polydata2 = np.array(reshaped_list2)
    # reshaped_polydata4 = np.array(reshaped_list4)
    print(reshaped_polydata2)
    print(type(reshaped_polydata2))

    #polydata 2
    point_cloud = pv.PolyData(reshaped_polydata2)
    
    np.allclose(reshaped_polydata2, point_cloud.points)

    point_cloud.plot(eye_dome_lighting=True)

    data = reshaped_polydata2[:,-1]

    point_cloud["elevation"] = data

    point_cloud.plot(render_points_as_spheres=True)
    
    point_cloud.save(glob_path + file_list_png1[k] + '.vtk')

    #polydata 4
    # point_cloud = pv.PolyData(reshaped_polydata4)
    
    # np.allclose(reshaped_polydata4, point_cloud.points)

    # point_cloud.plot(eye_dome_lighting=True)

    # data = reshaped_polydata4[:,-1]

    # point_cloud["elevation"] = data

    # point_cloud.plot(render_points_as_spheres=True)

