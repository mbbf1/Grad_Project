cd %~dp0
CALL C:\Users\Dell\miniconda3\pkgs\conda-24.1.2-py312haa95532_0\Scripts\activate.bat
CALL conda activate pt
CALL python "D:\ProjectsIdeas\GroupProject\DroneDetection\DroneDetection\detect.py" --weights b256_88.pt --conf 0.25 --img-size 1080 --source Test.mp4