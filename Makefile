install: # установить зависимости
	poetry install

package-remove: # для автоматического удаления предыдущего пакета
        python3 -m pip uninstall hexlet-code

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


make lint:
    poetry run flake8 brain_games

