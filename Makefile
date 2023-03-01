install:
	poetry install

package-remove:
    python3 -m pip uninstall hexlet-code

brain-games:
    poetry run brain-games

brain-even:
    poetry run brain-even

build:
    poetry build

publish:
    poetry publish --dry-run

package-install:
    python3 -m pip install --user dist/*.whl

make lint:
    poetry run flake8 brain_games
