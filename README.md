# Building the service

    docker compose build

# Running the service

    docker compose up

# Running alembic migrations

    docker compose exec itenergy-service alembic upgrade head

# Linting

    flake8 && isort --check --diff . && mypy && yamllint .

# Tests

    pytest .