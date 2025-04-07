# slack-emoji-notifier

これは、Slackのカスタム絵文字が追加されたときに指定のチャンネルに通知を送るGitHub Actions対応のBotです。

## 📦 主な機能

- Slackに新しいカスタム絵文字が追加されたかを定期的にチェック
- 新しい絵文字が見つかったら、指定されたチャンネルに通知
- GitHub Actionsのスケジュール機能で自動実行
- GitHubの無料枠で動作可能

## 🛠 セットアップ手順

### 1. Slack Botを作成

- [Slack API: Your Apps](https://api.slack.com/apps) にアクセス
- 新しいアプリを作成し、以下のOAuthスコープを追加：
  - `emoji:read`
  - `chat:write`
- アプリをワークスペースにインストールし、Botトークン（`xoxb-`で始まる）を取得

### 2. GitHubリポジトリを作成

- このテンプレートをクローンまたはアップロード
- GitHubの「Settings > Secrets and variables > Actions」で以下のシークレットを設定：

  | 名前               | 値                              |
  |--------------------|----------------------------------|
  | `SLACK_TOKEN`      | Slack Botのトークン             |
  | `SLACK_CHANNEL_ID` | 通知を送信したいチャンネルのID |

### 3. スケジュールの調整（任意）

`.github/workflows/emoji-check.yml` の `cron` を編集することで、実行タイミングを変更できます。

## 🚀 デプロイ方法

- コードをコミット
- GitHubの「Actions」タブからワークフローを手動実行するか、スケジュール実行を待つ

## 📎 備考

- `emoji_list.json` に絵文字リストを保存して差分を検出しています
- `.gitignore` でこのファイルをGitの管理対象外にしてください

## 🧑‍💻 作者

N.T
