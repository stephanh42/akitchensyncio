#!/bin/sh

git clean -x -f -d
pandoc --from=markdown --to=plain --output=README README.md && \
python3 setup.py sdist && \
python3 setup.py bdist_wheel && \
echo "To upload:" && echo python3 -m twine upload dist/*
