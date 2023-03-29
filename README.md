# Large Language Model Chats

As LLM become more and more sophisticated the need to study their capabilities becomes evermore pressing. This is a repository is an emerging attempt to start recording intersting an novel interactions with LLMs to try to understand their full range capabilities. The only limit on the experiments to perform is limited by human and AI imaginations.

Repository includes some tools to make recording chat logs a bit easier on people.
If you are interested in contributing feel free to open a pull request. All logs should be in the standard chat format in Markdown format (see any of them for examples).

Chats recorded by using Large Language models

- [ChatGPT/BARD Conversation 1](chats/chatgpt-bard-1.md)
- [ChatGPT/BARD Debate 10](chats/chatgpt-bard-10.md)
- [ChatGPT/BARD Debate 11](chats/chatgpt-bard-11.md)
- [ChatGPT/BARD Debate 12](chats/chatgpt-bard-12.md)
- [ChatGPT/BARD Conversation 13](chats/chatgpt-bard-13.md)
- [ChatGPT3.5 See if it will code in loop 14](chats/chatgpt-14.md)
- [ChatGPT4 See if it will code in loop 15](chats/chatgpt-15.md)
- [ChatGPT4 ideas analysis 16](chats/chatgpt-16.md)

Ideas for future exploration:
* Conversation between ChatGPT and BARD where ChatGPT is teacher and BARD is student.
* Code generation like in 15 where we try to get ChatGPT to create as elaborate python code as it possibly can.
* Execute print loop but where ChatGPT is given a goal to accomplish. Maybe even simple goal like do calculations correctly.
* ChatGPT talks to BING, BING talk to BARD?
* ChatGPT Given a news article identify logical fallacies or factual errors by the writer. 

TODO:
Create script so that outputs from AI an be more easily formatted into MD files.

How to fill out the chat template:
<blockquote>
# ChatGPT4 - <Chat title> - <number of chat>

* **Date of conversation:** March 26, 2023
* <extra notes>

> **User1**
Text text text text...

> **ChatGPT**
Text text text.
Text text text text

Text text..

> **User1**
Text text text text...

> **ChatGPT**
Text text text...

</blockquote>
see chat_template.md 
  
To turn template into properly formatted markdown:
Run> format_template.py filename.md 
