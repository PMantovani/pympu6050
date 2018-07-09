import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pympu6050",
    version="1.0.0",
    author="Pedro Mantovani Antunes",
    author_email="pmantovani94@gmail.com",
    description="An API in Python for communication with the MPU6050 accelerometer/gyroscope. Perfect for Raspberry Pi.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PMantovani/pympu6050",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
)