# The Flask Template Leveraging LocalStack for simulated s3 filestore&middot; [![Version Badge](https://img.shields.io/badge/version-1.0.0-brightgreen)](#)

A basic Flask starter project to get started with Docker Compose, LocalStack and Shipyard.

## Includes

- Jinja + Bootstrap (from CDN)
- uWSGI entrypoint
- Celery (with example heartbeat task configured)
- Flask-SQLAlchemy
- [LocalStack](https://github.com/localstack/localstack)

## Dependencies

- Make
- Docker & Docker Compose

## Getting Started

- Run `make develop` at the root of this project.
- Visit the app at http://localhost:8080/files to list objects in LocalStack s3 bucket
- Visit http://localhost:8080/files/create to add test object
- Make your code changes! The app will reload whenever you save.
