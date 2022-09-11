import github_issue
import os

from slack_bolt import App
from slack_bolt.workflows.step import WorkflowStep


class Step:
    def __init__(self):
        self.app = App(
            process_before_response=True,
            token=os.getenv("slack_bot_token"),
            signing_secret=os.environ.get("slack_signing_secret"),
        )
        self.step = WorkflowStep.builder("step")

    def edit(self, ack, step, configure):
        ack()

        blocks = [
            {
                "type": "input",
                "block_id": "issue_title_input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "issue_title",
                    "placeholder": {"type": "plain_text", "text": "issue title input"},
                },
                "label": {"type": "plain_text", "text": "Issue title"},
            },
            {
                "type": "input",
                "block_id": "issue_body_input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "issue_body",
                    "placeholder": {"type": "plain_text", "text": "issue body input"},
                },
                "label": {"type": "plain_text", "text": "Issue body"},
            },
        ]
        configure(blocks=blocks)

    def save(self, ack, view, update):
        ack()

        values = view["state"]["values"]
        issue_title = values["issue_title_input"]["issue_title"]
        issue_body = values["issue_body_input"]["issue_body"]

        inputs = {
            "issue_title": {"value": issue_title["value"]},
            "issue_body": {"value": issue_body["value"]},
        }
        outputs = [
            {
                "type": "text",
                "name": "issue_url",
                "label": "Issue URL",
            }
        ]
        update(inputs=inputs, outputs=outputs)

    def execute(self, step, complete, fail):
        inputs = step["inputs"]
        print(inputs)
        title = inputs["issue_title"]["value"]
        body = inputs["issue_body"]["value"]
        url = github_issue.GithubIssue().create(title=title, body=body, label="bug")
        outputs = {
            "issue_url": url,
        }
        complete(outputs=outputs)

    def workflows(self):
        ws = WorkflowStep(
            callback_id="create_github_issue",
            edit=self.edit,
            save=self.save,
            execute=self.execute,
        )
        self.app.step(ws)
        return self.app
