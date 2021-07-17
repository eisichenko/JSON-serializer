# JSON-serializer

![build](https://github.com/eisichenko/JSON-serializer/actions/workflows/ci.yml/badge.svg) [![codecov](https://codecov.io/gh/eisichenko/JSON-serializer/branch/master/graph/badge.svg?token=BuufL9jLZZ)](https://codecov.io/gh/eisichenko/JSON-serializer)

- Was **not** used `import json`, written **own** json serializer.

- Serializes and deserializes:

    - `int`, `str`, `float`, `bool`, `NoneType`

    - `dict`, `list`, `tuple`, `set`, `frozenset`, `bytes`, `bytearray`

    - `CodeType`

    - **custom:** `classes`, `functions`, `functions with decorators`, `objects`, `iterator clases`, `iterator objects`

- **Automatically** dumps and loads all global variables and dependencies of a given object.
