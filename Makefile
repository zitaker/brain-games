 first_installation:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

#package-remove:
#	python3 -m pip uninstall hexlet-code
#
#install:
#	poetry install
#
#brain-games:
#	poetry run brain-games
#
#brain-even:
#	poetry run brain-even
#
#brain-calc:
#	poetry run brain-calc
#
#brain-gcd:
#	poetry run brain-gcd
#
#brain-progression:
#	poetry run brain-progression
#
#brain-prime:
#	poetry run brain-prime
#
#build:
#	poetry build
#
#publish:
#	poetry publish --dry-run
#
#package-install:
#	python3 -m pip install --user dist/*.whl
#
#make lint:
#	poetry run flake8 brain_games
