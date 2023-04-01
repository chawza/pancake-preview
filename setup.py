from distutils.core import setup

setup(
    name='pancake-preview',
    version='0.1',
    description='Live prevewing templates without running djanngo projects',
    author=['Adrian Holovaty', 'Nabeel Kahlil Maulana'],
    author_email='nabeelkahlil403@gmail.com',
    url='https://github.com/chawza/pancake-preview',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=['pancake_preview'],
    install_requires=[
        'css-inline',
        'Django',
        'uvicorn',
        'fastapi',
        'watchfiles',
        'typer',
        'websockets'
    ]
)
