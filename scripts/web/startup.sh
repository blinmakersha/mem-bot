#!/usr/bin/env bash

get_ngrok_url() {
  curl --silent --show-error http://ngrok:4040/api/tunnels | jq -r '.tunnels[0].public_url'
}

NGROK_URL=""
while [ -z "$NGROK_URL" ]; do
  echo "Ждём ngrok URL..."
  NGROK_URL=$(get_ngrok_url)
done

echo "Ngrok URL получен: $NGROK_URL"

# Обновление переменной окружения
export MEM_BACKEND_HOST=$NGROK_URL

if [[ $WEBHOOK_URL != "" ]];
  then
    exec uvicorn src.main:create_app --host=$BIND_IP --port=$BIND_PORT
  else
    exec python src/main_polling.py
fi;
