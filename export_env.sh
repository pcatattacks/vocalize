conda env export --no-build | grep -v "^prefix: " > environment.yml
