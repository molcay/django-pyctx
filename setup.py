import os

from setuptools import setup, find_packages

__ROOT_DIR__ = os.path.abspath(os.path.dirname(__file__))
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def readme():
    with open(os.path.join(__ROOT_DIR__, 'README.md')) as f:
        return f.read()


def get_info():
    info = {}
    with open(os.path.join(__ROOT_DIR__, 'django_pyctx', '__version__.py'), 'r') as f:
        exec(f.read(), info)
    return info


package_info = get_info()

setup(name=package_info['__title__'],
      version=package_info['__version__'],
      description=package_info['__description__'],
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 2.0',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='pyctx django django-pyctx django-request-logger django-req-ctx',
      url=package_info['__url__'],
      author=package_info['__author__'],
      author_email=package_info['__author_email__'],
      license=package_info['__license__'],
      packages=find_packages(),
      install_requires=[
          'pyctx',
          'django',
      ],
      zip_safe=False,
      )
