from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="sweet.mobile",
    version="0.0.1",
    author="tonglei",
    author_email="tonglei@qq.com",
    description="Sweet's mobile autotest module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sweeterio/mobile",
    packages=['sweet.modules.mobile'],
    package_data={'.': ['*.py']},
    install_requires=[
        'sweet',
        'Appium-Python-Client'
    ],            
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)