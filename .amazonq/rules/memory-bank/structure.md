# Project Structure

## Directory Organization

```
jobsearch-mcp-aws/
├── src/                    # Python source code
│   └── __init__.py        # Package initialization
├── cloudformation/         # AWS CloudFormation templates
│   └── main.yaml          # Main infrastructure template
├── scripts/               # Deployment and utility scripts
│   └── deploy-cfn.sh      # CloudFormation deployment script
├── .amazonq/              # Amazon Q configuration
│   └── rules/             # Project rules and documentation
├── pyproject.toml         # Project configuration and dependencies
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── README.md              # Project documentation
├── LICENSE                # License file
└── .gitignore            # Git ignore patterns
```

## Core Components

### Source Code (`src/`)
- Contains the main Python MCP server implementation
- Package structure for modular development
- Entry point for the job search functionality

### Infrastructure (`cloudformation/`)
- AWS CloudFormation templates for cloud deployment
- Infrastructure as Code (IaC) approach
- Scalable AWS resource definitions

### Deployment (`scripts/`)
- Automated deployment scripts
- Environment-specific configuration support
- Development and production deployment workflows

## Architectural Patterns

### MCP Server Architecture
- Model Context Protocol implementation
- Standardized interface for AI tool integration
- Event-driven communication model

### Cloud-Native Design
- AWS-first deployment strategy
- Infrastructure as Code principles
- Scalable and maintainable cloud resources

### Python Package Structure
- Modern Python packaging with pyproject.toml
- Clear separation of concerns
- Development tooling integration