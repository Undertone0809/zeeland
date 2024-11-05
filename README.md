# Zeeland

![coverage](./assets/images/coverage.svg)

Zeeland's core infrastructure serves the following frameworks:

| Lib                                             | Description                                                                                             |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Cogit   | LLM MultiAgent task inference and autonomous orchestration framework/Comming soon                                                      |
| [Promptulate](https://github.com/Undertone0809/promptulate)   | A LLM application and Agent development framework.                                                      |
| [Gcop](https://github.com/Undertone0809/gcop)                 | Your git AI copilot.                                                                                   |

## TODO

The following libraries are under development and will be released soon:

| Lib                                             | Description                                                                                             |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [UACP](https://github.com/Undertone0809/UACP)                 | Universal Agent Communication Protocol.                                                                  |
| [P3G](https://github.com/Undertone0809/P3G)                   | Python Package Project Generator.                                                                       |
| [cushy-storage](https://github.com/Undertone0809/cushy-storage) | A lightweight ORM framework that provides disk caching for Python objects.                             |
| [omnius](https://github.com/Undertone0809/omnius)             | A lightweight event bus framework. You can easily build a powerful event bus in your project.        |
| [cushy-socket](https://github.com/Undertone0809/cushy-socket) | A Python socket library. You can create a TCP/UDP connection easily.                                |
| [imarkdown](https://github.com/Undertone0809/imarkdown)       | A practical Markdown image URL converter.                                                               |
| [cushy-serial](https://github.com/Undertone0809/cushy-serial) | A lightweight Python serial library. You can create a serial program easily.                         |
| [ecjtu](https://github.com/Undertone0809/ecjtu)               | ecjtu API SDK service, best practices for client SDK design.                                           |

## Quick start

Conda package manager is recommended. Create a conda environment.

```bash
conda create -n zeeland python==3.10
```

Activate conda environment and install poetry

```bash
conda activate zeeland
pip install poetry
```

Then you can run the client using the following command:

```bash
zeeland --help
```

or with `Poetry`:

```bash
poetry run zeeland --help
```

### Basic Usage

Create a metadata file in the default storage path.

```python
import json
import os

from zeeland import get_default_storage_path


def main():
    storage_path = get_default_storage_path("test")
    metadata_path = os.path.join(storage_path, "metadata.json")

    metadata = {"name": "test", "version": "1.0.0", "description": "Test metadata file"}

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Created metadata file at: {metadata_path}")
    with open(metadata_path, "r") as f:
        print("Content:")
        print(json.dumps(json.load(f), indent=4))


if __name__ == "__main__":
    main()
```

### Makefile usage

[`Makefile`](https://github.com/Undertone0809/zeeland/blob/main/Makefile) contains a lot of functions for faster development.

<details>
<summary>Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>Codestyle and type checks</summary>
<p>

Automatic formatting uses `ruff`.

```bash
make format
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `ruff` and `darglint` library

</p>
</details>

<details>
<summary>Code security</summary>
<p>

> If this command is not selected during installation, it cannnot be used.

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>All linters</summary>
<p>

Of course there is a command to run all linters in one:

```bash
make lint
```

the same as:

```bash
make check-codestyle && make test && make check-safety
```

</p>
</details>

<details>
<summary>Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/Undertone0809/python-package-template/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

</p>
</details>

<details>
<summary>Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 🛡 License

[![License](https://img.shields.io/github/license/Undertone0809/zeeland)](https://github.com/Undertone0809/zeeland/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/Undertone0809/zeeland/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{zeeland,
  author = {zeeland},
  title = {zeeland frameworks core infra},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Undertone0809/zeeland}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/P3G-%F0%9F%9A%80-brightgreen)](https://github.com/Undertone0809/python-package-template)

This project was generated with [P3G](https://github.com/Undertone0809/P3G)
