# Objective
In this project, we would be combining multiple services and open-source tools to make a Chatbot that recommends songs based on the tone of the conversation which the user is having with the chatbot.

# Project Context
The purpose of chat bots is to support and scale business teams in their relations with customers. It could live in any major chat applications like Facebook Messenger, Slack, Telegram, Text Messages, etc. Chatbot applications streamline interactions between people and services, enhancing customer experience. At the same time, they offer companies new opportunities to improve the customers engagement process and operational efficiency by reducing the typical cost of customer service.
In this project, we would be building an extensive Chatbot service, to which you can talk to. And talking to a chatbot wouldn't be business-driven. It would just be casual conversations. Further, on top of it, the chatbot would also be recommending songs to the user based on the tone of the user. This song recommendation feature employs the use of Last.fm API, very much similar to the popular Spotify API. Also for tone/emotion analysis of the conversation we will be using the IBM Tone Analyzer API.

# Product Architecture
![ME_ME_PROJECT_CHATBOT_PYTHON_MODULE_ME_PROJECT_CHATBOT_PYTHON_MODULE_CHATBOT_PYTHON_architecture](https://github.com/NebulaTris/vibescape/assets/94922914/c382eeb0-9eab-4430-9613-43023f32c8c7)

# High-Level Approach
- User starts the conversation
- Emotional Analysis of the conversation is done using the IBM Emotional API
- Get the reply to the conversation from the Cakechat Chatbot
- Based on the Emotion which the app perceives, top songs are retrieved using Last.fm songs API
- If a user listens to a particular song for sometime, a similar song would be recommended to the user using Last.fm API.

# Primary goals
- Setting up an open-source project locally and handling the errors being faced
- Using multiple services to build up a new service over them.
- Having a real-world chatbot, to which you can literally chat like you chatting to a real person and enjoying the music recommended by the system.
