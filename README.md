# Poetry workflow

**be sure to set virtualenvs.in-project = true**

```zsh
poetry new {project_name}
cd {project_name}
poetry shell # creates the virtual env inside the project
# add [tool.poetry.scripts] to the pyproject.toml
```