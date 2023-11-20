# Building the service

    docker compose build

# Running the service

    docker compose up

# Linting

    flake8 && isort --check --diff . && mypy && yamllint .