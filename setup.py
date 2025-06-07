from setuptools import setup, find_packages

setup(
    name='diagnose-tool',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['psutil', 'colorama'],
    author='Thorsten Bylicki',
    author_email='109308073+bylickilabs@users.noreply.github.com',
    description='CLI System Diagnose Tool für Kali/Linux',
    url='https://github.com/bylickilabs/system-diagnose-tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
