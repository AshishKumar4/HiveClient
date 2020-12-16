import setuptools


setuptools.setup(
    name="hive-white0racle", # Replace with your own username
    version="0.0.1",
    author="Ashish Kumar Singh",
    author_email="ashishkmr472@gmail.com",
    description="Client side cli and libraries to connect and setup     \
                a automated distributed ML experimentation system",
    # long_description="",
    # long_description_content_type="text/markdown",
    url="https://github.com/ashishkumar4/hiveclient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)