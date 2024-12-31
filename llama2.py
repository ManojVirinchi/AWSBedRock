import boto3
import json

# Define the prompt message
prompt_message = """ 
what is the cricket score of the match india vs australia in the t20 world cup 2024
"""

# Define the request payload with the correct structure
request_payload = {
    "prompt": f"[INST]{prompt_message}[/INST]",
    
}

# Convert the payload to JSON
body = json.dumps(request_payload)

# Initialize the AWS Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Invoke the model
response = bedrock.invoke_model(
    modelId="meta.llama2-70b-chat-v1",
    body =body
    
)

# Process the response
response_body = json.loads(response['body'].read())
response_text = response_body['generation']
print(response_text)
