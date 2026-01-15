# jobsearch-mcp-aws
MCP server for popular UK job sites


## Project Structure

```
├── src/                    # Python source code
├── cloudformation/         # CloudFormation templates
├── scripts/               # Deployment scripts
├── requirements.txt       # Python dependencies
└── pyproject.toml        # Project configuration
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Deploy CloudFormation

```bash
chmod +x scripts/deploy-cfn.sh
./scripts/deploy-cfn.sh jobsearch-mcp-dev dev
```
