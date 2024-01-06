WEBHOOK_ID=$1
curl -X DELETE https://serra.fibery.io/api/webhooks/v2/${WEBHOOK_ID} \
     -H "Authorization: Token ${FIBERY_API_TOKEN}" \
     -H 'Content-Type: application/json' \
