from setuptools import setup, find_packages

setup(
    name='django-google-credentials',
    version='0.0.2',
    description='Django app storing Google API OAuth credentials.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    license='BSD',
    url='http://github.com/praekelt/django-google-credentials',
    packages = find_packages(),
    dependency_links = [
    ],
    install_requires=[
        'django',
        'google-api-python-client',
        'south',
    ],
    tests_require=[
        'django-setuptest',
    ],
    test_suite="setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
