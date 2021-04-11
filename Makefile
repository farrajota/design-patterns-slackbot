SLACK_API_KEY=INSERT_SLACK_TOKEN_HERE
SLACK_CHANNEL=INSERT_SLACK_CHANNEL_HERE

test:
	@echo "Start slackbot"
	@SLACK_API_KEY=${SLACK_API_KEY} SLACK_CHANNEL=${SLACK_CHANNEL} python src/slackbot.py
	@echo "Done."

generate:
	python generate_readmes.py
