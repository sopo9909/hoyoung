from flask import Flask, Response
from slackeventsapi import SlackEventAdapter
import os
from threading import Thread
from slack import WebClient
import json
 
# This `app` represents your existing Flask app
app = Flask(__name__)
greetings = ["hi", "hello", "hello there", "hey"]
SLACK_SIGNING_SECRET = os.environ['9952ac01eafae92fe30d05d97f61cd2d']
slack_token = os.environ['xoxb-1545617412550-1596845048695-dxAZ4YEFfHEaYLmYlnS1xkPI']
VERIFICATION_TOKEN = os.environ['qirhEwe9E8PDXqG7lYH04rHu']
 
#instantiating slack client
slack_client = WebClient(slack_token)
# An example of one of your Flask app's routes
@app.route("/")
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}
 
    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}
    return
slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/slack/events", app
)  
@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]
            if any(item in command.lower() for item in greetings):
                message = (
                    "Hello <@%s>! :tada:"
                    % message["user"]  # noqa
                )
                slack_client.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)
# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=5000)
