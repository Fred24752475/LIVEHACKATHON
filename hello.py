"""First Strands smoke test — Bedrock via IAM credentials.

Requires:
  - aws configure (IAM access keys, region us-east-1)
  - Claude model access enabled in Bedrock
  - NO AWS_BEARER_TOKEN_BEDROCK env var (that breaks Converse)
"""

from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator

# Use an inference profile ID (required for Claude Sonnet 4 on-demand).
model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-6",
    region_name="us-east-1",
)

agent = Agent(model=model, tools=[calculator])
result = agent("What is the square root of 1764? Reply with just the number.")
print(result)
