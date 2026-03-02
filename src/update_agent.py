import os
from abacusai import ApiClient

# Your agent configuration code here
def create_agent_workflow():
    # Define your workflow nodes, graph, etc.
    # This is where your agent logic goes
    pass

# Get API key from environment variable
api_key = os.environ.get('ABACUS_API_KEY')
if not api_key:
    raise Exception('ABACUS_API_KEY environment variable is not set')

# Initialize client with API key
client = ApiClient(api_key=api_key)

# Update the agent
agent = client.update_model(
    model_id='your_model_id_here',
    # Add your agent parameters here
    workflow_graph=workflow_graph,
    agent_interface=agent_interface,
    # ... other parameters
)

# Wait for deployment to complete
agent.wait_for_publish()
print(f"Agent updated successfully: {agent}")
