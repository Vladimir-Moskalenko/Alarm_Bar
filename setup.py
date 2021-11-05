from setuptools import setup

APP = ['0.1.0.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='SmartBar',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)
