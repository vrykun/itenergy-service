# Building the service

    docker compose build

# Running the service

    docker compose up

# Linting

    docker compose run --no-deps --rm itenergy-domain-service-test sh -c 'flake8 && isort --check --diff . && mypy && yamllint .'