# ai-company-agent


-used a resource policy for lambda function rather than an iam for the bedrock agent, it's just simpler this way

-you cannot create bedrock knowldgebase with root user, it's just something amazon says in it's documentation it isn't clear why

- based on the user prompt, it does a semantic match to the description of the api in the openapi schema

- Preprocessing: takes the input, tokenizes, and prepares the prompt in a way that the model can take it in. 

- Orchestration step: looks at "user input", then looks at "instructions for agent", then looks at "description of the openapi schema". It then breaks down 


![5555finalmov-ezgif com-speed](https://github.com/user-attachments/assets/fdda391c-536f-4b6d-a145-05bb7f16712e)


![7777final-ezgif com-speed](https://github.com/user-attachments/assets/959cbbf0-a866-4a14-9cb1-a6062d2767ea)
