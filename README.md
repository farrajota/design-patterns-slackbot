# Design Patterns

Send random design patterns to your slack for you or your teammates to see.

The motivation for making this is due to the existence of dozens and dozens of design patterns one can [find in the wild](https://github.com/DovAmir/awesome-design-patterns#cloud-architecture) but you have no idea of their existence but still you would like to learn more about to enrich your knowledge and toolkit.

This repo provides a tool to easily ingest this kind of information by providing a summarized view of the patterns which you can learn more about and share it with your friends.

> Note: This repo is slowly being updated but if you would like to contribute, feel free to make a pull request and I'll gladly review it.

## Requirements

- Python 3.6+
- Slack API key
- Slack channel

# Usage - Slack

To send a message, first set `SLACK_API_KEY` and `SLACK_CHANNEL` as environment variables with the api key and channel to send messages to.

```bash
export SLACK_API_KEY="xxxx-xxxxxxxx-xxxxxxxxxx-xxxxxxxxxxxxxxxxx"
export SLACK_CHANNEL="#monitoring-testing"
```

Then, to send a message with a random pattern just run the following script:

```bash
python slackbot/send_messages.py --random
```

You should see some message like the following:

![Sample slack image](images/sample_message.png "Slackbot message")

Additionally, to generate a random list of messages that will not be repeated and to send a single message do the following:

```bash
python slackbot/send_messages.py  # sends a message to slack
python slackbot/send_messages.py  # sends a different message
python slackbot/send_messages.py  # send another different one
```

> Idea: Setup a cronjob to send random messages to slack every morning to your team to share this knowledge.

# Patterns

## Cloud Architecture

- [Azure cloud design patterns](cloud_design_patterns/README.md)

## TODO

- Add patterns:
    - [general architecture](https://github.com/DovAmir/awesome-design-patterns#general-architecture)
    - [Cloud architecture](https://github.com/DovAmir/awesome-design-patterns#cloud-architecture)

# References

- https://github.com/DovAmir/awesome-design-patterns#cloud-architecture

# License

[MIT License](LICENSE)
