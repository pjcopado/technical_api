# Technical API

Simple API for handling students, professors and courses.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.10+

```bash
git clone git@github.com:pjcopado/technical_api.git`
```

#### Run on Local

```bash
make install_dependencies
```

```bash
make local_test
```

```bash
make alembic_upgrade
```

#### Run on Docker

```bash
make docker_build_local
```

```bash
make docker_run_local
```
