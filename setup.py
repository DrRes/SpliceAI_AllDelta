import io
from setuptools import setup


setup(name='spliceai_alldelta',
      description='SpliceAI: A deep learning-based tool to identify splice variants. A modified version for retreiving not only maximum of delta values, but all delta values',
      long_description=io.open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      version='1.2.1.9000',
      author='Shinichi Namba (Originally written by Kishore Jaganathan)',
      author_email='sinnhazime@gmail.com',
      license='GPLv3',
      url='https://github.com/illumina/SpliceAI',
      packages=['spliceai'],
      install_requires=['keras>=2.0.5',
                        'pyfaidx>=0.5.0',
                        'pysam>=0.10.0',
                        'numpy>=1.14.0',
                        'pandas>=0.23.0'],
      extras_require={'cpu': ['tensorflow>=1.2.0'],
                      'gpu': ['tensorflow-gpu>=1.2.0']},
      package_data={'spliceai': ['annotations/grch37.txt',
                                 'annotations/grch38.txt',
                                 'models/spliceai1.h5',
                                 'models/spliceai2.h5',
                                 'models/spliceai3.h5',
                                 'models/spliceai4.h5',
                                 'models/spliceai5.h5']},
      entry_points={'console_scripts': ['spliceai=spliceai.__main__:main']}
      )#,
      #test_suite='tests')
