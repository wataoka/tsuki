build-package:
	python setup.py sdist bdist_wheel
upload-package:
	twine upload dist/*