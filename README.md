# StarMap
 
Finds given patch images in the bigger image using OpenCV - Brisk Feature Detector. Uses Brute-Force matcher to match image descriptors. 
 
Run main.py by passing 'main_image' and 'patch_image' filenames as arguments. Images should be placed in the 'Images' directory. Output images are saved in the 'Output' folder with corresponding input image name. Corner points are printed after code execution. 

Examples:

    $ python main.py --main_image='StarMap.png' --patch_image='Small_area.png'
   
Output:

Corner points:

 [[[856 150]]

 [[855 262]]

 [[968 264]]

 [[968 149]]]
 

    $ python main.py --main_image='StarMap.png' --patch_image='Small_area_rotated.png'

Output:

Corner points:

 [[[420 639]]

 [[498 770]]

 [[630 692]]

 [[553 560]]]


Can also run in Colab notebook: cv_test.ipynb (place images in the current working directory) 
