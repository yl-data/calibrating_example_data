import glob
import calibrating

# marker 特征提取器
feature_lib = calibrating.ArucoFeatureLib(occlusion=True)
# 标定并获得相机模型
cam = calibrating.Cam(glob.glob("paired_stereo_and_depth_cams_aruco/*/depth_cam_color.jpg"), feature_lib)
# 保存内参
cam.dump("intrinsic.yaml")
# 可视化标定板覆盖范围
calibrating.showb(cam.vis_image_points_cover())

