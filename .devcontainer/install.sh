# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the Dapr CLI
wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash

# Install the Dapr runtime
dapr uninstall
dapr init
