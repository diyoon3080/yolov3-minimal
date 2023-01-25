from setuptools import setup

setup(name='yolov3-minimal',
      version='0.1',
      url='https://github.com/zzh8829/yolov3-tf2',
      author='Do Il Yoon',
      author_email='diyoon@mz.co.kr ',
      python_requires='>=3.7',
      install_requires=['numpy', 'tensorflow==2.2.0', 'opencv-python-headless'],
      packages=['yolov3-minimal'])