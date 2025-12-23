# CI-GITHUB-ACTIONS

This repository contains a basic implementation of Continuous Integration (CI) using GitHub Actions. It features a simple Streamlit calculator application that computes the square, cube, and fifth power of a given number, along with automated testing.

## Features

- **Calculator App**: A Streamlit-based web application for calculating powers of numbers.
- **Automated Testing**: Unit tests using pytest to ensure code reliability.
- **Continuous Integration**: GitHub Actions workflow that runs tests on every push and pull request to the main branch.

## Project Structure

- `app.py`: The main Streamlit application.
- `_test.py`: Unit tests for the calculator functions.
- `.github/workflows/ci.yaml`: GitHub Actions CI workflow configuration.
- `LICENSE`: Project license.
- `README.md`: This file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CI-GITHUB-ACTIONS.git
   cd CI-GITHUB-ACTIONS
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pytest
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Open your browser to the provided URL (usually `http://localhost:8501`) to use the calculator.

## Testing

Run the tests locally:
```bash
pytest _test.py
```

## Continuous Integration

The project uses GitHub Actions for CI. The workflow (`.github/workflows/ci.yaml`) automatically:
- Checks out the code
- Sets up Python 3.9
- Installs dependencies (pytest and streamlit)
- Runs the test suite

The CI pipeline triggers on pushes and pull requests to the `main` branch.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and add tests.
4. Run tests locally.
5. Submit a pull request.

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file. 
