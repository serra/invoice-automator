# use op cli to export api token to env var
# Usage: source export_api_token_from_1password.sh
# Dependencies: op cli, jq

op signin
export FIBERY_API_TOKEN=$(op item get "Fibery" --vault "personal" --fields fibery_api_token --format=json | jq -r '.value')