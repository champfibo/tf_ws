from setuptools import setup
import os
from glob import glob

package_name = 'learning_tf2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),

        (os.path.join('share', package_name,'launch'), glob(os.path.join('launch','*_launch.py'))),
    ],
    
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='patcharapon',
    maintainer_email='patcharapon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

            'static_turtle_tf2_broadcaster = learning_tf2_py.static_turtle_tf2_broadcaster:main',
            'turtle_tf2_broadcaster = learning_tf2_py.turtle_tf2_broadcaster:main',
            'turtle_tf2_broadcaster2 = learning_tf2_py.turtle_tf2_broadcaster2:main',
            'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
            'param_talker = learning_tf2_py.python_parameters_node:main',
            'test1 = learning_tf2_py.test1:main',
            'fixed_frame_tf2_broadcaster = learning_tf2_py.fixed_frame_tf2_broadcaster:main',
            'tf_carver = learning_tf2_py.tf_carver:main',
        ],
    },
)
