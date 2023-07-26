import os



from langchain import OpenAI, ConversationChain
llm = OpenAI(temperature=0)
# etting verbose=True so we can see the prompt
# conversation = ConversationChain(llm=llm, verbose=True)
conversation = ConversationChain(llm=llm, verbose=False)
output = conversation.predict(input="Hi there!")
print(output)

output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(output)

while True:
    myInput = input()
    if(myInput == "exit"):
        break
    output = conversation.predict(input=myInput)
    print(output)