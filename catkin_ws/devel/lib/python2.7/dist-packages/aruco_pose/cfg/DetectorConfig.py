## *********************************************************
##
## File autogenerated for the aruco_pose package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Constant for adaptive thresholding before finding contours', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'adaptiveThreshConstant', 'edit_method': '', 'default': 7.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Minimum window size for adaptive thresholding before finding contours', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'adaptiveThreshWinSizeMin', 'edit_method': '', 'default': 3, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Maximum window size for adaptive thresholding before finding contours', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'adaptiveThreshWinSizeMax', 'edit_method': '', 'default': 23, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Increments from adaptiveThreshWinSizeMin to adaptiveThreshWinSizeMax during the thresholding', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'adaptiveThreshWinSizeStep', 'edit_method': '', 'default': 10, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Maximum number of iterations for stop criteria of the corner refinement process', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'cornerRefinementMaxIterations', 'edit_method': '', 'default': 30, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Corner refinement method', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'cornerRefinementMethod', 'edit_method': "{'enum_description': 'An enum to set corner refinement method', 'enum': [{'srcline': 31, 'description': 'No refinement', 'srcfile': '/home/tsaipeihsain/catkin_ws/src/aruco_pose/cfg/DetectorParams.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'CORNER_REFINE_NONE'}, {'srcline': 32, 'description': 'Do subpixel refinement', 'srcfile': '/home/tsaipeihsain/catkin_ws/src/aruco_pose/cfg/DetectorParams.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'CORNER_REFINE_SUBPIX'}, {'srcline': 33, 'description': 'Use contour-Points', 'srcfile': '/home/tsaipeihsain/catkin_ws/src/aruco_pose/cfg/DetectorParams.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'CORNER_REFINE_CONTOUR'}, {'srcline': 34, 'description': 'Use the AprilTag2 approach', 'srcfile': '/home/tsaipeihsain/catkin_ws/src/aruco_pose/cfg/DetectorParams.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'CORNER_REFINE_APRILTAG'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Minimum error for the stop criteria of the corner refinement process', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'cornerRefinementMinAccuracy', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Window size for the corner refinement process (in pixels)', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'cornerRefinementWinSize', 'edit_method': '', 'default': 5, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': "check if there is a white marker. In order to generate a 'white' marker just invert a normal marker by using a tilde", 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'detectInvertedMarker', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Error correction rate respect to the maximum error correction capability for each dictionary', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'errorCorrectionRate', 'edit_method': '', 'default': 0.6, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Minimum distance between corners for detected markers relative to its perimeter', 'max': 0.25, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'minCornerDistanceRate', 'edit_method': '', 'default': 0.05, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Number of bits of the marker border, i.e. marker border width', 'max': 10, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'markerBorderBits', 'edit_method': '', 'default': 1, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Maximum number of accepted erroneous bits in the border (i.e. number of allowed white bits in the border)', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'maxErroneousBitsInBorderRate', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Minimum distance of any corner to the image border for detected markers (in pixels)', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'minDistanceToBorder', 'edit_method': '', 'default': 3, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'minimum mean distance beetween two marker corners to be considered similar, so that the smaller one is removed. The rate is relative to the smaller perimeter of the two markers', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'minMarkerDistanceRate', 'edit_method': '', 'default': 0.05, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Determine minimum perimeter for marker contour to be detected. This is defined as a rate respect to the maximum dimension of the input image', 'max': 4.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'minMarkerPerimeterRate', 'edit_method': '', 'default': 0.03, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Determine maximum perimeter for marker contour to be detected. This is defined as a rate respect to the maximum dimension of the input image', 'max': 4.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'maxMarkerPerimeterRate', 'edit_method': '', 'default': 4.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Minimun standard deviation in pixels values during the decodification step to apply Otsu thresholding (otherwise, all the bits are set to 0 or 1 depending on mean higher than 128 or not)', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'minOtsuStdDev', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Width of the margin of pixels on each cell not considered for the determination of the cell bit. Represents the rate respect to the total size of the cell, i.e. perpectiveRemovePixelPerCell', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'perspectiveRemoveIgnoredMarginPerCell', 'edit_method': '', 'default': 0.13, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Number of bits (per dimension) for each cell of the marker when removing the perspective', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'perspectiveRemovePixelPerCell', 'edit_method': '', 'default': 4, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Minimum accuracy during the polygonal approximation process to determine which contours are squares', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'polygonalApproxAccuracyRate', 'edit_method': '', 'default': 0.03, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Detection of quads can be done on a lower-resolution image, improving speed at a cost of pose accuracy and a slight decrease in detection rate. Decoding the binary payload is still done at full resolution', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'aprilTagQuadDecimate', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'What Gaussian blur should be applied to the segmented image (used for quad detection?) Parameter is the standard deviation in pixels. Very noisy images benefit from non-zero values', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'aprilTagQuadSigma', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Detector_CORNER_REFINE_NONE = 0
Detector_CORNER_REFINE_SUBPIX = 1
Detector_CORNER_REFINE_CONTOUR = 2
Detector_CORNER_REFINE_APRILTAG = 3
