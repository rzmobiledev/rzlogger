from pathlib import Path
from distutils.core import setup
import setuptools

directory = Path(__file__).parent

setup(
    name="rizallogger",
    packages=setuptools.find_packages(),
    version="0.2",
    license="MIT",
    description="Make easy to log your project",
    long_description=(directory / "README.md").read_text(),
    author="Safrizal",
    author_email="rzmobiledev@gmail.com",
    url="https://github.com/rzmobiledev/rzlogger",
    download_url="https://github.com/rzmobiledev/rzlogger/archive/v_01.tar.gz",
    keywords=["rzlogger", "easylog", "rizallogger", "rz-logger"],
    # package need to install / package used in this package
    requires=["logging"],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
