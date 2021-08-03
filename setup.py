from setuptools import setup, find_packages

setup(name="keyBinder",
    version="0.0.1",
    author="MyBadProjects",
    author_email="<cheems.website>",
    description="A simple key binding package.",
    long_description="A simple package which allows you to bind keys to functions.",
    url="<https://cheems.website/keyBinder>"
    packages=find_packages(),
    install_requires=['keyboard'],
    keywords=['python', 'key', 'keyboard', 'bind', 'keybind', 'key bind'],
    classifiers= [
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved ::  Apache-2.0 License",
        "Operating System :: OS Independent"])
