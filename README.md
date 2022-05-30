# Example calibration board images for `calibrating`


Example images are captured by paired_stereo_and_depth_cams:  
[![paired_stereo_and_depth_cams_1](https://user-images.githubusercontent.com/10448025/131831496-7a38c677-a578-4a4e-a01e-aa102dad9dbc.jpg)](https://github.com/yl-data/calibrating_example_data/raw/master/paired_stereo_and_depth_cams.jpg?raw=true)

## File structure
```bash
$ tree .
├── depth_camera_intric.yaml
├── paired_stereo_and_depth_cams_checkboard
│   ├── 1
|   |   ├── depth_cam_color.jpg
|   |   ├── depth_cam_depth.png
|   |   ├── stereo_l.jpg
|   |   └── stereo_r.jpg
|   ├── ...
│   └── 9
├── paired_stereo_and_depth_cams_aruco
│   ├── 1
│   ├── ...
│   └── 9
└── README.md
```
## Checkboard example
**depth_cam_color.jpg**:  
![depth_cam_color.jpg](paired_stereo_and_depth_cams_checkboard/1/depth_cam_color.jpg)
**depth_cam_depth.png**:  
![depth_cam_depth.png](paired_stereo_and_depth_cams_checkboard/1/depth_cam_depth.png)
**stereo_l.jpg**:  
![stereo_l.jpg](paired_stereo_and_depth_cams_checkboard/1/stereo_l.jpg)
**stereo_r.jpg**:  
![stereo_r.jpg](paired_stereo_and_depth_cams_checkboard/1/stereo_r.jpg)


## Marker example: `cv2.aruco`
**depth_cam_color.jpg**:  
![depth_cam_color.jpg](paired_stereo_and_depth_cams_aruco/1/depth_cam_color.jpg)
**depth_cam_depth.png**:  
![depth_cam_depth.png](paired_stereo_and_depth_cams_aruco/1/depth_cam_depth.png)
**stereo_l.jpg**:  
![stereo_l.jpg](paired_stereo_and_depth_cams_aruco/1/stereo_l.jpg)
**stereo_r.jpg**:  
![stereo_r.jpg](paired_stereo_and_depth_cams_aruco/1/stereo_r.jpg)


Note: 
- aruco images are resized by `boxx.resize(img, 0.5)`
- Checkboard images are croped by `python -m boxx.script "p-[imsave(pa, imread(pa)[924:2724,1486:3986]) for pa in glob('*/stereo*.jpg')]"`

