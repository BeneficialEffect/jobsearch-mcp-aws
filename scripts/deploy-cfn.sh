#!/bin/bash
set -e

STACK_NAME="${1:-jobsearch-mcp-dev}"
TEMPLATE_FILE="cloudformation/main.yaml"
ENVIRONMENT="${2:-dev}"

aws cloudformation deploy \
  --stack-name "$STACK_NAME" \
  --template-file "$TEMPLATE_FILE" \
  --parameter-overrides Environment="$ENVIRONMENT" \
  --capabilities CAPABILITY_IAM \
  --no-fail-on-empty-changeset

echo "Stack deployed: $STACK_NAME"
