from setuptools import setup, find_packages


f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='django-tags',
    version='0.10d1',
    description='django-tags is a reusable Django application for simple tags.',
    long_description=readme,
    author='Thiago Avelino',
    author_email='thiago@avelino.xxx',
    url='http://github.com/avelino/django-tags/tree/master',
    packages=find_packages(),
    package_data = {
        'tags': [
            'locale/*/LC_MESSAGES/*',
        ],
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
    install_requires=['Django'],
    include_package_data=True,
    zip_safe=False,
)
