# Lab 5: Static Code Analysis — Issue Log

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug / Code quality | 8 | A list used as a default argument could be shared between function calls. | Replaced the default list with `None` and initialized a new list inside the function. |
| Bare exception | Code quality | 21 | A bare `except` could catch unexpected exceptions. | Caught the specific `KeyError` and `ValueError` exceptions. |
| Shell command execution | Security | 36 | `os.system()` constructed and executed a shell command, creating a command-injection risk. | Replaced shell execution with `pathlib` file operations. |
| Unsafe file handling | Code quality | 32 | The file was opened without a context manager or explicit encoding. | Used `with open()` and `encoding="utf-8"`. |
| Incorrect capacity check | Logic / Bug | 11 | The original condition could allow bookings beyond the configured capacity. | Changed the comparison to reject bookings when the class is full. |
| Negative capacity | Validation | 26 | Negative class capacities were accepted. | Added validation to reject negative values. |
| Function naming | Style | 27 | `addMembers` did not follow the recommended snake_case naming convention. | Renamed the function to `add_members`. |
| Missing documentation | Style | Multiple | The module and functions lacked docstrings. | Added module and function docstrings. |
| Formatting violations | Style | Multiple | Flake8 reported missing blank lines and a bare exception. | Corrected spacing and exception handling. |

## Verification Summary

- Pylint after fixes: 10.00/10.
- Bandit after fixes: No issues identified.
- Flake8 after fixes: No reported violations.
