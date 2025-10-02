# Treeson

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Treeson is a command-line tool that converts directory structures and GitHub repositories into JSON format. Perfect for documentation, analysis, and tooling purposes.

## Features

- **Directory to JSON**: Convert local directory structures to structured JSON
- **GitHub Repository Support**: Fetch and convert GitHub repository structures
- **Smart Filtering**: Built-in ignore patterns for common files/folders
- **Highly Configurable**: Custom ignore patterns, depth limits, and hidden file handling
- **Multiple Output Options**: stdout, file output, compact or pretty-printed JSON
- **Fast and Lightweight**: Minimal dependencies, efficient processing

## Installation

### Using pip

```bash
pip install treeson
```

### From source

```bash
git clone https://github.com/SergioBonatto/treeson.git
cd treeson
pip install -e .
```

### Using uv

```bash
uv add treeson
```

## Quick Start

### Convert current directory to JSON

```bash
treeson
```

### Convert specific directory

```bash
treeson /path/to/directory
```

### Convert GitHub repository

```bash
treeson https://github.com/user/repository
```

### Save output to file

```bash
treeson . --output structure.json
```

## Usage

```
treeson [TARGET] [OPTIONS]
```

### Arguments

- `TARGET`: Directory path or GitHub URL (default: current directory)

### Options

| Option | Short | Description |
|--------|-------|-------------|
| `--ignore PATTERN` | `-i` | Additional files/folders to ignore (can be used multiple times) |
| `--branch NAME` | `-b` | GitHub branch name (default: main) |
| `--include-hidden` | | Include hidden files and directories |
| `--max-depth N` | | Maximum directory depth to traverse |
| `--output FILE` | `-o` | Write output to file instead of stdout |
| `--compact` | | Output compact JSON (no indentation) |
| `--version` | | Show version and exit |

## Examples

### Basic usage

```bash
# Current directory
treeson

# Specific directory
treeson /home/user/projects

# GitHub repository
treeson https://github.com/python/cpython
```

### Advanced usage

```bash
# Ignore additional patterns
treeson -i "*.log" -i temp -i cache .

# Specify GitHub branch
treeson --branch develop https://github.com/user/repo

# Include hidden files with depth limit
treeson --include-hidden --max-depth 3 .

# Compact output to file
treeson --compact --output project-structure.json .
```

## Output Format

The tool generates a JSON structure where:
- Directories are represented as objects with nested structure
- Files are listed in a `"files"` array within each directory
- The structure preserves the hierarchical organization

### Example output

```json
{
  "files": ["main.py", "README.md"],
  "src": {
    "files": ["__init__.py", "utils.py"],
    "models": {
      "files": ["user.py", "base.py"]
    }
  },
  "tests": {
    "files": ["test_main.py"]
  }
}
```

## Default Ignore Patterns

Treeson automatically ignores common files and directories:

- `.git`
- `__pycache__`
- `.DS_Store`
- `node_modules`
- `venv`, `.venv`
- `.idea`
- `.pytest_cache`
- `.mypy_cache`
- `.tox`
- `dist`
- `build`
- `*.egg-info`

## Configuration

### Programmatic Usage

```python
from treeson.cli import dir_to_json, TreesonConfig
from pathlib import Path

# Custom configuration
config = TreesonConfig(
    ignores={"temp", "logs", "*.tmp"},
    include_hidden=True,
    max_depth=5
)

# Convert directory
result = dir_to_json(Path("/path/to/dir"), config)
print(result)
```

### GitHub API Usage

```python
from treeson.cli import github_repo_to_json, TreesonConfig

# Convert GitHub repository
config = TreesonConfig(ignores={"docs", "examples"})
result = github_repo_to_json(
    "https://github.com/user/repo",
    config,
    branch="main"
)
print(result)
```

## Error Handling

Treeson handles various error conditions gracefully:

- **Permission denied**: Warnings are shown, processing continues
- **Network errors**: Clear error messages for GitHub API issues
- **Invalid paths**: Descriptive error messages
- **Rate limiting**: Automatic handling of GitHub API limits

## Requirements

- Python 3.8+
- `requests` library (for GitHub functionality)

## Development

### Setup development environment

```bash
git clone https://github.com/SergioBonatto/treeson.git
cd treeson
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### Running tests

```bash
python -m pytest
```

### Code formatting

```bash
black treeson/
isort treeson/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v0.1.1
- Initial release
- Basic directory to JSON conversion
- GitHub repository support
- CLI interface with comprehensive options
- Smart ignore patterns

## Support

If you encounter any issues or have questions, please:

1. Check the [existing issues](https://github.com/SergioBonatto/treeson/issues)
2. Create a new issue with detailed information
3. Include the command you ran and the error message

---

Made with care by [Sergio Bonatto](https://github.com/SergioBonatto)
