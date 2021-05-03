import os
import json
import random
import argparse
import requests
from pathlib import Path
from string import capwords


ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

design_patterns = {
    "Cloud Architecture": [
        os.path.join(ROOT_DIR, "cloud_architecture", "azure_cloud_design_patterns")
    ]
}


def main(slack_api_key: str, channel: str, is_random: bool = False) -> None:
    if is_random:
        send_random_slack_bot_message(
            slack_api_key=slack_api_key,
            channel=channel
        )
    else:
        send_sequential_slack_bot_message(
            slack_api_key=slack_api_key,
            channel=channel
        )


def send_random_slack_bot_message(slack_api_key: str, channel: str) -> None:
    pattern_files: list = load_pattern_files()
    random.shuffle(pattern_files)

    category, filepath = pattern_files[0].split(',')
    data: dict = load_json_file(filepath)

    if "example" not in data:
        data["example"] = []
    if "image_url" not in data:
        data["image_url"] = []

    msg = generate_message(
        name=data["name"],
        summary=data["summary"],
        main_category=category,
        category=data["category"],
        example=data["example"],
        reference=data["reference"],
        image_url=data["image_url"],
    )

    slack_send_message(
        msg=msg,
        slack_api_key=slack_api_key,
        channel=channel
    )


def send_sequential_slack_bot_message(slack_api_key: str, channel: str) -> None:
    filepath = '/tmp/design_patterns.txt'

    if not os.path.exists(filepath):
        Path(filepath).touch()

    with open(filepath, 'r') as f:
        pattern_files = f.read()

    if len(pattern_files) == 0:
        pattern_files: list = load_pattern_files()
        random.shuffle(pattern_files)
    else:
        pattern_files = pattern_files.split('\n')

    with open(filepath, 'w') as f:
        f.writelines("\n".join(pattern_files[1:]))

    category, filepath = pattern_files[0].split(',')
    data: dict = load_json_file(filepath)

    if "example" not in data:
        data["example"] = []
    if "image_url" not in data:
        data["image_url"] = []

    msg = generate_message(
        name=data["name"],
        summary=data["summary"],
        main_category=category,
        category=data["category"],
        example=data["example"],
        reference=data["reference"],
        image_url=data["image_url"],
    )

    slack_send_message(
        msg=msg,
        slack_api_key=slack_api_key,
        channel=channel
    )


def load_pattern_files() -> list:
    filepaths = []
    for category in design_patterns:
        for sub_category in design_patterns[category]:
            dirpath = os.path.join(sub_category, "patterns")
            filenames = os.listdir(dirpath)
            filepaths += [",".join([category, os.path.join(dirpath, filename)]) for filename in filenames]
    return filepaths


def load_json_file(path: str) -> dict:
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data


def generate_message(
    name: str,
    summary: str,
    image_url: str,
    main_category: str,
    category: list,
    example: list,
    reference: list,
) -> dict:
    slack_message = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Today's design pattern on *{capwords(main_category)}*: <{reference[0]['href']}|{capwords(name)} pattern>"
            }
        },
        {
            "type": "section",
            "block_id": "section567",
            "text": {
                "type": "mrkdwn",
                "text": f"*Summary* \n {summary}"
            }
        },
        {
            "type": "section",
            "block_id": "section789",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Category*\n" + '\n'.join([f"`{cat}`"for cat in category])
                },
                {
                    "type": "mrkdwn",
                    "text": "*Examples*\n" + " | ".join([f"<{elem['href']}|{capwords(elem['language'])}>" for elem in example])
                }
            ]
        },
        {
            "type": "section",
            "block_id": "section780",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*References*\n"  + "\n".join([f"<{ref['href']}>" for ref in reference])
                }
            ]
        }
    ]

    if len(image_url) > 0:
         slack_message.append(
             {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": f"{name} design pattern image",
                },
                "block_id": "quickchart-image",
                "image_url": f"{image_url}",
                "alt_text": name,
            },
         )

    return slack_message


def slack_send_message(msg: dict, slack_api_key: str, channel: str) -> None:
    payload = {
        "token": slack_api_key,
        "channel": channel,
        "blocks": json.dumps(msg),
    }
    response = requests.post("https://slack.com/api/chat.postMessage", data=payload)
    response_json = response.json()
    if response.status_code != 200 or not response_json["ok"]:
        raise RuntimeError(f"Slack request failed!\n {json.dumps(response_json, indent=2)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", help="Randomly selects a design pattern.", action="store_true")
    args = parser.parse_args()

    slack_api_key = os.environ.get('SLACK_API_KEY')
    slack_channel = os.environ.get('SLACK_CHANNEL')
    main(slack_api_key=slack_api_key, channel=slack_channel, is_random=args.random)
