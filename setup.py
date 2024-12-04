from setuptools import setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=['mypkg.talker'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jyunta Suzuki',
    maintainer_email='s23C1074ZE@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={  # ここにエントリーポイントを追加
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
        ],
    },
)

