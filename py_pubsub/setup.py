from setuptools import setup

package_name = 'py_pubsub'

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
                'simple_pub = py_pubsub.minimal_pub:main',
                'listener = py_pubsub.minimal_sub:main',
                'timer_test = py_pubsub.timer_test:main',
                'pub_by_kb = py_pubsub.pub_by_kb:main',
                'sub_by_kb = py_pubsub.sub_by_kb:main',
        ],
    },
)
