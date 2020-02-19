### Create packages and wheels
python setup.py sdist bdist_wheel

### Simple upload to PyPi
twine upload dist/*

### Simple upload to TestPyPi
twine upload --repository testpypi dist/*

### Upload specific version
twine upload --skip-existing dist/rref-0.3.0*