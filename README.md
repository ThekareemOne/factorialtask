# Factorial Task Backend

## Installation

- Make sure you have Docker installed and running.

## Setup

- Build the images. `$ docker compose build`
- Run the compose stack `$ docker compose up`
- Run migrations and seed the database with fake data. Run `$ docker compose run backend python manage.py migrate`, `$ docker compose run backend python manage.py populate_db`.
- Install pre-commit hooks `$ pre-commit install`.
- run the app zwith `docker run -p 8000:8000 your_django_app`

### Provided User Accounts

| Account Type | Username/Email             | Password  | Has Access To The Admin Portal |
| :----------- | :------------------------- | :-------- | :----------------------------- |
| Employee     | `employee@airteam.cloud`   | `airteam` | Yes                            |
| Client       | `client@airteam.cloud`     | `airteam` | Yes                            |
| Pilot        | `pilot@airteam.cloud`      | `airteam` | Yes                            |
| Freelancer   | `freelancer@airteam.cloud` | `airteam` | Yes                            |

## Running

### With VSCode (docker)

- Make sure you have the `Remote-Containers` vscode extension installed.
- Open folder in remote container. (might take a long time the first time)
- Run bundled task. `Django Server`, or run the `Python: Django` debugging task.

### With PyCharm (docker)

- You can use the bundled run configuration `Compose Stack`.
- For backend debugging use the run configuration `Django Server`.

### Manually in your terminal (docker)

- `$ docker compose up`

### Run locally (host):

To run service locally (via IDE or from CMD) you need to ensure its dependencies (databases and external services) are
available locally and environmental variables are set up.

1. Run rabbitmq, postgres and redis dependencies locally: `docker-compose -f docker-compose-local.yml up -d`
2. Set localhost env var to point to your local postgres: `export POSTGRES_HOST=localhost`
3. Set localhost env var to point to your local redis: `export REDIS_HOST=localhost`
4. Set localhost env var to point to your local rabbit: `export RABBIT_HOST=localhost`
5. make sure you installed all dependencies: `pipenv install --dev`
6. Set development environment: `export APP_ENV=dev`
7. Run migration to prepare the database: `python manage.py migrate`
8. Populate the database with dummy data: `python manage.py populate_db`
9. Set the local path for static files: `export STATIC_ROOT=./static`
10. Collect static files: `python manage.py collectstatic --no-input`
11. Export secret key env var: `export SECRET_KEY=test`
12. Run server: `python manage.py runserver localhost:8081`
13. Run worker: `celery -A airteam.celery:app worker -l info`
14. Go to [admin](http://localhost:8081/admin/login) and use `employee@airteam.cloud`:`airteam` to log in.

### VARIABLES

- INVOICE_PAID_SUBSCRIPTION: Subscription name of the AFP pubsub subscription for invoice-paid event, you can find it in infra repo.
- NEW_NOTIFICATION_TOPIC: subscription name
- RESET_PASSWORD_TOPIC: subscription name
- VERIFY_ACCOUNT_TOPIC: subscription name
- COMPANY_UPDATE_TOPIC: subscription name
- CONTACT_UPDATE_TOPIC: subscription name
- NEW_CLIENT_TOPIC: subscription name
- NEW_CLIENT_CONFIRMATION_TOPIC: subscription name
- NEW_INVOICE_TOPIC: subscription name
- FLIGHT_GUIDE_GENERATED_TOPIC: subscription name
- NEW_PERMISSIONS_UPLOADED_TOPIC: subscription name
- NEW_PROJECT_REQUEST_TOPIC: subscription name
- PROJECT_CREATED_TOPIC: subscription name
- PROJECT_REQUESTED_TOPIC: subscription name
- PROJECT_DELIVERED_EVENT: subscription name
- CUSTOMER_ACCEPTED_PROPOSED_DELIVERY_TIME_TOPIC: subscription name
- CUSTOMER_CONFIRMED_EXPECTED_DELIVERY_TIME_TOPIC: subscription name
- CUSTOMER_EXPECTED_DELIVERY_TIME_CONFIRMED_TOPIC: subscription name
- CUSTOMER_EXPECTED_DELIVERY_TIME_CONFIRMED_FOR_EMPLOYEE_EVENT: subscription name
- CUSTOMER_REJECTED_PROPOSED_DELIVERY_TIME_TOPIC: subscription name
- CUSTOMER_SUBMITTED_EXPECTED_DELIVERY_TIME_TOPIC: subscription name
- SHARE_PROJECT_FILE_TOPIC: subscription name
- CANCEL_SUBSCRIPTION_REQUEST_TOPIC: subscription name
- CONTRACT_CONFIRMED_EVENT: subscription name
- SUBSCRIPTION_ACCEPTED_TOPIC: subscription name
- SHARE_FAST_FUSION_3D_TOPIC: subscription name
- CATEGORY_NOT_LOCKED_TOPIC: subscription name
- FLIGHT_SCHEDULED_TOPIC: subscription name
- PHOTO_UPLOADED_TOPIC: subscription name
- PILOT_ASSIGNED_PROJECT_TOPIC: subscription name
- PILOT_NOT_ACCEPTED_AT_PROJECT_TOPIC: subscription name
- AIRTEAM_PROPOSED_DELIVERY_TIME_TOPIC: subscription name
- CONTRACT_ACCEPTED_EVENT: subscription name
