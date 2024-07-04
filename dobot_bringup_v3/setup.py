from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'dobot_bringup_v3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dobot',
    maintainer_email='dobot@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dobot_bringup  = dobot_bringup_v3.dobot_bringup:main',
            'feedback  = dobot_bringup_v3.feedback:main',
           
        ],
    },
)
