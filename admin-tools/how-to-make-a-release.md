# Get latest sources:

    $ git pull

# Change version in xdis/version.py.

    $ emacs VERSION.py
    $ source VERSION.py
    $ echo $VERSION
    $ git commit -m"Get ready for release $VERSION" .

# Update ChangeLog:

    $ make ChangeLog

#  Update NEWS from ChangeLog. Then:

	$ emacs NEWS.md
    $ make check
    $ git commit --amend .
    $ git push   # get CI testing going early
    $ make check-full

# Make sure pyenv is running and check versions

    $ pyenv local && source admin-tools/check-versions.sh

# Make packages and tag

    $ . ./admin-tools/make-dist.sh
	$ pyenv local 3.8.2
	$ twine check dist/columnize-$VERSION*

Goto https://github.com/rocky/pycolumnize/releases/new

# Upload to Pypi

    $ twine upload dist/columnize-${VERSION}*

# Pull tags:

	$ git pull --tags
