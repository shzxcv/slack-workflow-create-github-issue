import logging
import steps

from slack_bolt.adapter.aws_lambda import SlackRequestHandler

SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

def handler(event, context):
    app = steps.Step().workflows()
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
