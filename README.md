# ai-company-agent

<img width="1271" alt="agent workflow" src="https://github.com/user-attachments/assets/855321bc-3a50-4368-8801-93512e189cd2">


# Demo

### Simple Case: No Issues With New Account
![5555finalmov-ezgif com-speed](https://github.com/user-attachments/assets/fdda391c-536f-4b6d-a145-05bb7f16712e)

### Complicated Case: Status Pending with Issues
![7777final-ezgif com-speed](https://github.com/user-attachments/assets/959cbbf0-a866-4a14-9cb1-a6062d2767ea)

# Architechture

### Other helpful architechture models

<img width="1000" alt="Screenshot 2024-09-23 at 9 26 53 PM" src="https://github.com/user-attachments/assets/e9d82852-3e98-4813-8a27-3baecde7ce5b">

<img width="700" alt="Screenshot 2024-09-23 at 9 26 53 PM" src="https://github.com/user-attachments/assets/50951d18-2f71-46a3-8bf7-a91f325302cf">



### Description:
AI Company Agent using Amazon Bedrock This project demonstrates how to build an AI agent using Amazon Bedrock to interpret user inputs and execute corresponding API operations via AWS Lambda functions. The agent leverages semantic matching to map user prompts to API descriptions defined in an OpenAPI schema.


### Important Notes
- I Used a resource policy for lambda function rather than an iam for the bedrock agent, it's just what the docs recommended

- You cannot create bedrock knowldgebase with root user, it's just something amazon says in it's documentation it isn't clear why

- Based on the user prompt, it does a semantic match to the description of the api in the openapi schema

- Preprocessing: takes the input, tokenizes, and prepares the prompt in a way that the model can take it in. It also tries to decide if the input was malicious or outside the domain of the agent. 

- Orchestration step: looks at "user input", then looks at "instructions for agent", then looks at "description of the openapi schema". It then breaks down

- The CoT trace shows the agent’s reasoning step-by-step. Open each step to see the CoT details.

<img width="620" alt="Screenshot 2024-09-23 at 6 29 15 PM" src="https://github.com/user-attachments/assets/8f8975fb-ba27-46dc-beac-cd72ed61fcc5">

- In Amazon Bedrock, each Action Group can contain multiple API operations (up to 11), but you can ***only write one Lambda function per Action Group***. This Lambda function is responsible for dynamically handling all of the API operations within that Action Group.

- Amazon Bedrock Agents can use both the API description and the endpoint-specific description to help make decisions about which API operation (endpoint) to invoke. It also uses parameter matching based on user input. 



