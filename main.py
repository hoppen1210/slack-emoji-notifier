import os
import json
import requests

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]
STORAGE_FILE = "emoji_list.json"

def fetch_emoji_list():
    url = "https://slack.com/api/emoji.list"
    headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
    response = requests.get(url, headers=headers)
    print(response.status_code, response.text)
    return response.json().get("emoji", {})

def notify_new_emoji(new_names, emoji_dict):
    for name in new_names:
        url = emoji_dict[name]
        text = f":{name}: `:{name}:` が新しく追加されたよ！"
        payload = {
            "channel": CHANNEL_ID,
            "text": text,
        }
        res = requests.post("https://slack.com/api/chat.postMessage", json=payload,
                      headers={"Authorization": f"Bearer {SLACK_TOKEN}", "Content-Type": "application/json"})
        print(res.status_code, res.text)

def extract_image_id(url):
    return url.split("/")[-1].split(".")[0]

def main():
    new_list = fetch_emoji_list()
    new_ids_set = set(
        extract_image_id(url)
        for url in new_list.values()
        if not url.startswith("alias:")
    )

    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, "r") as f:
                old_ids = set(json.load(f))
        except json.JSONDecodeError:
            old_ids = set()
    else:
        old_ids = set()

    added_ids = new_ids_set - old_ids
    if added_ids:
        added_names = [
            name for name, url in new_list.items()
            if extract_image_id(url) in added_ids
        ]
        notify_new_emoji(added_names, new_list)
        with open(STORAGE_FILE, "w") as f:
            json.dump(list(new_ids_set), f)

if __name__ == "__main__":
    main()
