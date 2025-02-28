from setuptools import setup, Extension
from os import path

from Cython.Build import cythonize
import sys 

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

extensions = [
	Extension(
		"cysimdjson.cysimdjson",
		[			
			'cysimdjson/cysimdjson.pyx',
			'cysimdjson/simdjson/simdjson.cpp',
			'cysimdjson/pysimdjson/errors.cpp',
			'cysimdjson/cysimdjsonc.cpp',
		],
		language="c++",
		extra_compile_args=[
			"-std=c++17",  # for std::string_view class that became standard in C++17
			"-Wno-deprecated",
		# NOTE Windows doesn't know how to handle "-Wno-deprecated"		
		] if sys.platform != "win32" else ["/std:c++17"],
	)
]

setup(
	name='cysimdjson',
	version="21.11",
	description='Cython-based wrapper for SIMDJSON',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='TeskaLabs Ltd',
	author_email='info@teskalabs.com',
	platforms='any',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
	],
	packages=[
		"cysimdjson",
	],
	url='https://github.com/TeskaLabs/cysimdjson',
	project_urls={
		"Source": "https://github.com/TeskaLabs/cysimdjson",
		'Tracker': 'https://github.com/TeskaLabs/cysimdjson/issues',
	},
	install_requires=[
	],
	setup_requires=[
		"cython"
	],
	package_data={
		"cysimdjson": [
			"cysimdjson.pyx",
			"cysimdjson.h",
			"cysimdjsonc.h",
			"jsoninter.h",
			"pysimdjson/errors.h",
			"simdjson/simdjson.h",
		]
	},
	ext_modules=cythonize(extensions),
)
