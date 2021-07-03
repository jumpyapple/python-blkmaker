from setuptools import setup


def readme():
    with open("./README", "r") as f:
        return f.read()


setup(
    name="python-blkmaker",
    version="1.0.0",
    description="Native Python port of libblkmaker (getblocktemplate client implementation)",
    long_description=readme(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    keywords="blkmaker",
    url="https://github.com/luke-jr/python-blkmaker",
    author="Luke Dashjr",
    license="MIT",
    pacakges=["blkmaker"],
    install_requires=["base58"],
    zip_safe=False,
)
