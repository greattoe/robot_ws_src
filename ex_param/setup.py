from setuptools import setup

package_name = 'ex_param'

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
    maintainer='gus29',
    maintainer_email='gus29@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'turtle_by_param = ex_param.turtle_by_param:main',
                'req_set_param = ex_param.req_set_param:main',
                'req_get_param = ex_param.req_get_param:main',
                'req_get_param2 = ex_param.req_get_param2:main',
                'reg_params = ex_param.reg_params:main',
                'waypoint1 = ex_param.waypoint1:main',
                'waypoint2 = ex_param.waypoint2:main',
                'waypoint3 = ex_param.waypoint3:main',
                'waypoint4 = ex_param.waypoint4:main',
        ],
    },
)
