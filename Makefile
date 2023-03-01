install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

package-remove:
	python3 -m pip uninstall hexlet-code

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games