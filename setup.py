from setuptools import setup


setup(
    name='httpie-http2',
    description='HTTP/2 plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.0.1',
    author='Jakub Roztocil',
    author_email='jakub@roztocil.co',
    license='BSD',
    url='https://github.com/jakubroztocil/httpie-http2',
    download_url='https://github.com/jakubroztocil/httpie-http2',
    py_modules=['httpie_http2'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.transport.v1': [
            'httpie_http2 = httpie_http2:HTTP2TransportPlugin'
        ]
    },
    install_requires=[
        'httpie>0.9.0',
        'hyper'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
