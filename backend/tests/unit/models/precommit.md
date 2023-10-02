# pre commit hooks

## what is a git hook

git hooks are shell scripts that trigger a specific action in git, such as
commit push. Shell scripts are stored in the .git/hooks folder of your
repository, and are tools to check automatically code before executing a git
command.

## what is pre-commit hook

It is the git hook that runs before a commit is created. It is used to check if
there are mistakes in the code before commiting it, such as syntax errors, code
style, etc.

We are all human, and we can make mistakes, so it is good to have an
automatic tool to review for us.

## Nice, where should I start?

As more libraries and projects uses pre-commit hooks, it is hard to share them
across projects, aside that they are not versioned (any change in a githook,
needs to be copy/pasted among all projects).
[Pre-commit](https://pre-commit.com/) is a tool that allows to share pre-commit
hooks across projects, and version them.

## Use cases

- review code guide style
  - [black](https://github.com/psf/black)
- linters
  - [ruff](https://github.com/astral-sh/ruff) (fast linter, mean to group
    several linters in one)
  - [pyflakes](https://github.com/PyCQA/pyflakes)
  - [pydocstyle](https://github.com/PyCQA/pycodestyle)
  - [pylint](https://github.com/pylint-dev/pylint) support unit 3.8
  - [markdownlint](https://github.com/igorshubovych/markdownlint-cli
  - [flake8](https://github.com/PyCQA/flake8)
  - [autoflake](https://github.com/PyCQA/autoflake)
  - [autopep8](https://github.com/pre-commit/mirrors-autopep8)
- security issues
  - [bandit](https://github.com/PyCQA/bandit)
- sorts
  - [isort](https://github.com/PyCQA/isort)
  - [toml-sort](https://github.com/pappasam/toml-sort)
- typing
    [mypy](https://github.com/pre-commit/mirrors-mypy)

## vs IDE

Wait, for many of this use cases, I can configure my IDE to do it for me, why
then should I use pre-commit hooks? Well, IDE configuration is up to you, and it
is not shared across the team. Even, there are several IDE in the market, and
not all of them have the same features. Pre-commit hooks are shared across the
team, and are versioned, so if you change something, everyone will have the same
configuration.

## vs CI

Now I got you!! I run this checks in my CI with github actions/Jenkins, why
should I bother to use pre-commit hooks?

Well, for sure similar checks **must** be done in CI, but pre-commit hooks are
usually faster, and can fix most of the issues automatically for you before CI
is triggered. So, it is not a replacement for CI (specially as pre-commit can be
override using **--no-verify**, but a complement.
