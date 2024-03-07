from setuptools import find_packages
from setuptools import setup

package_name = 'ar_track'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ground0',
    maintainer_email='ground0@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sub_marker_pose = ar_track.sub_marker_pose:main',
            'pub_tb3_pose2d  = ar_track.pub_tb3_pose2d:main',
            'test_move_tb3   = ar_track.test_move_tb3:main',
            'stop_tb3        = ar_track.stop_tb3:main',
            'track_marker    = ar_track.track_marker:main',
            'track_marker2   = ar_track.track_marker2:main', #align2marker
            'align2marker   = ar_track.align2marker:main', 
            'timer_test      = ar_track.timer_test:main',
            'img_compressed2raw      = ar_track.img_compressed2raw:main',
            #img_compressed2raw
        ],
    },
)
