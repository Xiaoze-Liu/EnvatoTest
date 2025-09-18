# Pokémon ETL Task

**Please read all instructions carefully before starting.**

## Overview

This is a take-home task designed to assess your practical data engineering skills. Your goal is to create a simple ETL pipeline that:

- Retrieves Pokémon data from the public [PokéAPI](https://pokeapi.co/)
- Saves the data as raw JSON files
- Loads it into a [DuckDB](https://duckdb.org/) database

## Objectives

Create a Python CLI application that performs the following tasks:

1. **Extract**: Retrieve Pokémon data (The [`/pokemon`](https://pokeapi.co/docs/v2#pokemon) endpoint) from the PokéAPI by ID or name and save each Pokémon's data as an individual JSON file in the `data/raw/` directory

2. **Load**: Import the raw data into a landing table in DuckDB without normalisation

3. **Transform**: Process data from the raw table into normalized table(s) ready for downstream data modelling

### Data Modelling Options

You may choose between two approaches:

#### Option 1: Single denormalised table

- `pokemon` (id, name, height, weight, base_experience, types, abilities)
- Where `types` and `abilities` are stored as nested/array data

#### Option 2: Multiple normalised tables

- `pokemon` (id, name, height, weight, base_experience)
- `types` (pokemon_id, slot, type)
- `abilities` (pokemon_id, slot, ability, is_hidden)

Both approaches are acceptable. Please provide reasoning for your chosen approach in your submission. You could also choose to implement in another way if you prefer.

### Example Usage

Your application should support commands like:

```bash
envato-data-engineering-task --pokemon 1
```

This command should:

1. Extract Pokémon #1 data from the API (Bulbasaur)
2. Save the raw JSON to `data/raw/`
3. Load the data into a DuckDB table in the `raw` schema
4. Transform the raw data into normalised table(s) in the `pokeapi` schema

## Project Structure

We've provided a basic Python package structure. Feel free to modify it as needed for your solution.

### Included Files

- **INSTRUCTIONS.md** - This documentation
- **README.md** - You should include a README file with setup instructions and design decisions
- **src/** - Directory for application code
- **tests/** - Directory for application tests
- **data/envato.db** - DuckDB database file with pre-created schemas:
  - `raw` - For landing raw data
  - `pokeapi` - For transformed/normalized data
- **data/raw/** - Directory for raw JSON files
- **.gitignore** - Git ignore rules (production code should use version control)
- **.python-version** - Python version specification
- **pyproject.toml** - Modern Python packaging configuration

### Setup Instructions

To set up your development environment:

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install package in editable mode
pip install -e .
```

Test that the setup works:

```bash
envato-data-engineering-task
# Should output: "Hello from Envato's data engineering take home task!"
```

## Use of AI Tools

We are totally fine with the use of AI tools—it's an important part of the modern development lifecycle. However, like any tool, you need to be able to fully explain and understand your code. You will be asked about your solution, including how to enhance or change it, during the technical interview if your submission is successful. Please ensure you can confidently discuss and modify any code you submit, regardless of how it was produced.

## Evaluation Criteria

### Requirements

- **Language**: Python
- **Approach**: Keep it simple, clean, and testable - no hidden tricks or over-engineering needed
- **Quality**: Production-level code quality expected

### Code Quality Standards

Your submission should meet production standards:

- **Testing**: Unit tests included (we use [Pytest](https://docs.pytest.org/en/stable/), but use what you're comfortable with)
- **Formatting**: Consistent code formatting (we use [Black](https://github.com/psf/black))
- **Linting**: Code analysis and linting (we use [Pylint](https://pypi.org/project/pylint/))
- **Structure**: Modular and well-organised codebase
- **Documentation**: Appropriate code and usage documentation

*Note: We've listed our preferred tools, but feel free to use alternatives you're comfortable with.*

### Documentation Requirements

Include a `README` with your submission containing:

- **Setup instructions**: How to install and run your program
- **Dependencies**: Any additional software requirements
- **Design decisions**: Reasoning behind your architectural choices (optional but appreciated)

## Submission

When you've completed the task:

1. Create a zip file containing all your project files
2. Name the file: `firstname_lastname.zip`
3. Email it back to us (or follow the submission instructions provided in your email)

Good luck! 🚀
