# Development Guidelines

## Code Quality Standards

### Python Code Formatting
- **Line Length**: 100 characters maximum (configured in pyproject.toml)
- **Formatter**: Black for consistent code formatting
- **Linter**: Ruff for fast Python linting
- **Type Hints**: Use Pydantic for data validation and type safety

### Package Structure
- Use `__init__.py` files for package initialization
- Follow Python packaging standards with pyproject.toml
- Separate production and development dependencies

## Infrastructure as Code Patterns

### CloudFormation Templates
- Use YAML format for CloudFormation templates
- Include comprehensive parameter validation with AllowedValues
- Implement proper resource naming with environment prefixes
- Use AWS intrinsic functions (!Sub, !Ref) for dynamic values

### Resource Naming Convention
```yaml
BucketName: !Sub 'jobsearch-mcp-${Environment}-${AWS::AccountId}'
```
- Format: `{service}-{component}-{environment}-{account-id}`
- Ensures uniqueness across environments and accounts

### Security Best Practices
- Enable encryption by default (AES256 for S3)
- Use least privilege access patterns
- Include proper IAM capabilities in deployment scripts

## Deployment Standards

### Shell Script Patterns
- Use `set -e` for fail-fast behavior
- Provide default values with parameter expansion: `${1:-default}`
- Include descriptive echo statements for deployment feedback
- Use AWS CLI with proper error handling

### Environment Management
- Support multiple environments (dev, staging, prod)
- Use environment-specific parameter overrides
- Include `--no-fail-on-empty-changeset` for idempotent deployments

## Development Workflow

### Dependency Management
- Pin minimum versions for production dependencies
- Use separate requirements files for dev/prod
- Include version constraints for security and compatibility

### Project Configuration
- Use pyproject.toml for modern Python packaging
- Configure development tools (black, ruff) in pyproject.toml
- Maintain consistent tool configurations across the project

## Documentation Standards

### README Structure
- Include clear project description and purpose
- Provide setup instructions with platform-specific commands
- Document deployment procedures with example commands
- Use code blocks with proper syntax highlighting

### Code Comments
- Keep code self-documenting where possible
- Use docstrings for public APIs
- Include inline comments for complex business logic only

## Testing Patterns

### Test Framework
- Use pytest as the primary testing framework
- Include pytest in development dependencies
- Structure tests to match source code organization