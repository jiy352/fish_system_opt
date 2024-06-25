from setuptools import setup, find_packages

setup(
    name='fish_system_opt',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Any dependencies you have can be listed here, for example:
        # 'requests',
    ],
    # Include additional files into the package
    include_package_data=True,
)
