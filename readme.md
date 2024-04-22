# KIBERone TELEGRAM BOT on FAST API

## Telegram bot with webhook on FastAPI

Run app:

`uvicorn bot:app --reload`

For local dev you must to get `ngrok` from [site](https://dashboard.ngrok.com/get-started/setup/windows).

Run this command to create a tunnel:

`./ngrok http 8000`



# Deploy:

pip install -r requirements.txt

change bot.py:
uvicorn.run(app, host="0.0.0.0", port=8000)


sudo apt install nginx curl

server {
    listen 80;
    server_name example.com; # Замените на ваше доменное имя или IP-адрес

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


sudo ln -s /etc/nginx/sites-available/my_app.conf /etc/nginx/sites-enabled/


sudo systemctl restart nginx


source /path/to/your/venv/bin/activate
python bot.py


nohup python3 bot.py > bot.log 2>&1 &
nohup позволяет запустить процесс, который не завершится, когда вы закроете сеанс SSH.

'>' перенаправляет вывод программы в файл bot.log.
'2>&1' перенаправляет stderr (стандартный поток ошибок) в stdout (стандартный поток вывода), что позволяет записывать как вывод, так и ошибки в тот же файл.
'&' позволяет процессу работать в фоновом режиме.

ps aux | grep bot.py
Это покажет вам процесс bot.py, который должен быть запущен.

