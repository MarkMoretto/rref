python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
twine upload --repository pypi dist/*