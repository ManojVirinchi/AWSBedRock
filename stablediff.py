import boto3
import json
import base64
import os

prompt_message = "a 4K wallpaper of Virat kohli with his daughter "

prompt_template = [{"text" : prompt_message, "weight" : 1}]
bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "text_prompts": prompt_template,
    "cfg_scale" : 10,
    "seed" : 0,
    "steps": 50,
    "width" : 1024,
    "height": 1024
}

body = json.dumps(payload)
response = bedrock.invoke_model(
    body=body,
    modelId="stability.stable-diffusion-xl-v1",
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response['body'].read())
#print(response_body)
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

filename = "viratKohli.png"
with open(filename, "wb") as f:
    f.write(image_bytes)
