from setuptools import setup

setup(name='GMusicRecord'
    ,version='0.2.2'
    ,description=r'Automates making a record of gmusic songs so that the user can know if google removed some parts of the library.'
    ,author='Troy1010'
    #,author_email=''
    #,url=''
    ,license='MIT'
    ,packages=['GMusicRecord']
    ,zip_safe=False
    ,test_suite='nose.collector'
    ,tests_require=['nose']
    ,python_requires=">=3.6"
    ,install_requires=['gmusicapi'
        ,'TM_CommonPy'
        ]
    ,setup_requires=['nose'
        ,'gmusicapi'
        ,'TM_CommonPy'
        ]
      )
