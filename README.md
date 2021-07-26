# URDF-Model-Viewer-Test-

Still wip

Model Viewer Page: https://gjnguyen18.github.io/urdf-loader-test/

When uploading robot, make sure to select the entire description folder rather than just the urdf file.
But if loading robot from url, use the urdf file

This also contains animation files for the sawyer in 'sawyer animations'. Simply pick the csv file and load it in.

To create csv files from pkl files, input cd to the repo folder and type in: "python pklUnpacker.py [pkl file path]"
User also must manually enter into the csv file "time,[jointname1],[jointname2],[jointname3]..." with jointnames being the joint names showing for the robot in the viewer.

Also rmoo files can be loaded directly for the ur5 and other animation files of that type

Quicklinks:

Robot URDFS:

ur5: 
https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/ur5_description/urdf/ur5.urdf

sawyer (with gripper): 
https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/sawyer_description/urdf/sawyer_gripper.urdf

ur5 Animations:

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/ur5%20animations/ur5_relaxed_ik_ECA3.rmoo

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/ur5%20animations/ur5_rotations_relaxed_ik_ECA.rmoo

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/ur5%20animations/ur5_rotations_relaxed_ik_ECAA.rmoo


sawyer Animations:

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/sawyer%20animations/6_toys_base_0.csv

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/sawyer%20animations/7_tracing_base_0.csv

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/sawyer%20animations/11_stirring_base_0.csv

Scenes:

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/Kitchen_dynamic/urdf/Kitchen_dynamic.urdf

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/Kitchen_standard/urdf/Kitchen_standard.urdf

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/Kitchen_static/urdf/Kitchen_static.urdf


JSON files:

https://raw.githubusercontent.com/gjnguyen18/URDF-Model-Viewer-Test-Files/main/scenes/sample%20scene.json

