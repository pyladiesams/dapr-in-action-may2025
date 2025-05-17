# A conversational agent over unstructured documents with Chainlit

This exercise demonstrates how to build a fully functional, enterprise-ready agent that can parse unstructured documents, learn them and converse with users over their contents while remembering all previous interactions. This example also shows how to integrate Dapr with Chainlit, giving users a fully functional chat interface to talk to their agent.

## Key Benefits

- **Converse With Unstructured Data**: Users can upload documents and have them parsed, contextualized and be made chattable
- **Conversational Memory**: The agent maintains context across interactions in the user's [database of choice](https://docs.dapr.io/reference/components-reference/supported-state-stores/)
- **UI Interface**: Use an out-of-the-box, LLM-ready chat interface using [Chainlit](https://github.com/Chainlit/chainlit)
- **Cloud Agnostic**: Uploads are handled automatically by Dapr and can be configured to target [different backends](https://docs.dapr.io/reference/components-reference/supported-bindings)


## Environment Setup

1. Navigate to `advanced_workshop/06-document-agent-chainlit/` and install the dependencies:

<!-- STEP
name: Install Python dependencies
-->

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

<!-- END_STEP -->

2. Create a `.env` file for your API keys in `advanced_workshop/06-document-agent-chainlit/`:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

## Examples

### Upload a PDF and chat to a document agent

Run the agent:

```bash
dapr run --app-id doc-agent --resources-path ./components -- chainlit run app.py -w
```

Wait until the browser opens up. Once open, you're ready to upload any document and start asking questions about it! You can find the agent page at http://localhost:8000.

Upload a PDF of your choice, or use the example `red_foxes.pdf` file in this example.

#### Testing the agent's memory

If you exit the app and restart it, the agent will remember all the previously uploaded documents. The documents are stored in the binding component configured in `./components/filestorage.yaml`.

When you install Dapr using `dapr init`, Redis is installed by default and this is where the conversation memory is saved. To change it, edit the `./components/conversationmemory.yaml` file.

## Summary

**How It Works:**
1. Dapr starts, loading the file storage and conversation history storage configs from the `components` folder.
2. Chainlit loads and starts the agent UI in your browser.
3. When a file is uploaded, the contents are parsed and fed to the agent to be able to answer questions.
4. If the file storage component YAML is correctly configured, Dapr will upload the file to the storage provider.
5. The conversation history is automatically managed by Dapr and saved in the state store configured in `./components/conversationmemory.yaml`.

## Next Steps

After completing this exercise, you can:

- Modify the assistant’s instructions for different use cases (e.g., summarization, Q&A, highlighting key points).