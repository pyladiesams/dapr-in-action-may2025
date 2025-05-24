from dapr.clients import DaprClient
from dapr.clients.grpc._request import ConversationInput

with DaprClient() as d:
    inputs = [
        ConversationInput(content="What is dapr?", role='user', scrub_pii=True),
    ]

    metadata = {
        'model': 'modelname',
        'key': 'authKey',
        'cacheTTL': '10m',
    }

    print('Input sent: What is dapr?')

    response = d.converse_alpha1(
        name='echo', inputs=inputs, temperature=0.7, context_id='chat-123', metadata=metadata
    )

    for output in response.outputs:
        print(f'Output response: {output.result}')