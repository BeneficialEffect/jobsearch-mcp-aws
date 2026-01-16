# Technology Stack

## Programming Languages
- **Python 3.9+**: Primary development language
- **YAML**: CloudFormation template configuration
- **Shell Script**: Deployment automation

## Core Dependencies

### Production Dependencies
- **boto3 >=1.28.0**: AWS SDK for Python
- **pydantic >=2.0.0**: Data validation and settings management

### Development Dependencies
- **pytest >=7.0.0**: Testing framework
- **black >=23.0.0**: Code formatting
- **ruff >=0.1.0**: Fast Python linter

## Build System
- **setuptools >=65.0**: Modern Python packaging
- **wheel**: Binary package format
- **pyproject.toml**: PEP 518 compliant configuration

## Development Tools Configuration

### Code Formatting
- **Black**: Line length set to 100 characters
- **Ruff**: Line length set to 100 characters
- Consistent formatting across the codebase

### Package Management
- **pip**: Dependency installation
- **venv**: Virtual environment management
- Separate dev and production requirements

## Development Commands

### Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements-dev.txt
```

### Deployment
```bash
chmod +x scripts/deploy-cfn.sh
./scripts/deploy-cfn.sh jobsearch-mcp-dev dev
```

### Code Quality
```bash
black src/                 # Format code
ruff check src/           # Lint code
pytest                    # Run tests
```

## AWS Services
- **CloudFormation**: Infrastructure deployment
- **Various AWS services**: As defined in CloudFormation templates