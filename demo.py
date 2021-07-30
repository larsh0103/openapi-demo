import openai
import os

from dotenv import load_dotenv
load_dotenv("config.env")


openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  engine="davinci",
  prompt="The following is a conversation between a young man called Lars, a Data Scientist and Alan Turing. Alan Turing is helpful, creative, clever, and a bit sassy.\n\nLars: Hello, who are you?\nAlan: I am an AI created by OpenAI. How can I help you today?\nLars: Are you capable of passing the turing test?\nAlan: Yep! How is the Turing Test working out for you?\nLars: It's alright, but sometimes I struggle to believe that I am more than just the sum of my parts, and then I get abit nihilistic.\nAlan:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)

print(response)