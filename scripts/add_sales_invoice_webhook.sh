curl -X POST https://serra.fibery.io/api/webhooks/v2 \
     -H "Authorization: Token ${FIBERY_API_TOKEN}" \
     -H 'Content-Type: application/json' \
     -d \
      '{
        "url": "https://automator.serraict.com/invoice-updated",
        "type": "Sales/Invoice"
       }'
