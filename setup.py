from distutils.core import setup

setup(
    name="rzlogger",
    packages=["rzlogger"],
    version="0.1",
    license="MIT",
    description="Make easy to log your project",
    author="Safrizal",
    author_email="rzmobiledev@gmail.com",
    url="https://github.com/rzmobiledev/rzlogger",
    download_url="https://github.com/rzmobiledev/rzlogger/archive/v_01.tar.gz",
    keywords=["rzlogger", "easylog", "loggerrz"],
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
