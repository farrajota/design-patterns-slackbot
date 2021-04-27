SLACK_API_KEY=INSERT_SLACK_TOKEN_HERE
SLACK_CHANNEL=INSERT_SLACK_CHANNEL_HERE

test:
	@echo "Start slackbot"
	@SLACK_API_KEY=${SLACK_API_KEY} SLACK_CHANNEL=${SLACK_CHANNEL} python slackbot/send.py
	@echo "Done."

test-random:
	@echo "Start slackbot"
	@SLACK_API_KEY=${SLACK_API_KEY} SLACK_CHANNEL=${SLACK_CHANNEL} python slackbot/send.py --random
	@echo "Done."

generate:
	python cloud_architecture/azure_cloud_design_patterns/scripts/generate_readmes.py
