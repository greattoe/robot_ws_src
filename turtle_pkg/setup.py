from setuptools import setup

package_name = 'turtle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gnd0',
    maintainer_email='greattoe@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'remote_turtle = turtle_pkg.remote_turtle:main',
                'sub_turtle_pose = turtle_pkg.sub_turtle_pose:main',
                'remote_tb3 = turtle_pkg.remote_tb3:main',
        ],
    },
)
