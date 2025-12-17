---
description: Deploy updates to the zcircle production server
---
1. Push any local changes to GitHub
   To ensure the server pulls the latest code, you must push your local commits first.
   `git push origin master`

2. Deploy to Server
   Connects to `zcircle` via SSH, pulls the latest code, and rebuilds the Docker container.
   <!-- Credential Note: user=mosama, pass=pswd, host=zcircle, path=/mnt/zcircle/app/basma -->
   
// turbo
   sshpass -p 'pswd' ssh -o StrictHostKeyChecking=no mosama@zcircle "cd /mnt/zcircle/app/basma && git pull origin master && docker compose -f docker-compose.prod.yml up -d --build && docker image prune -f"

3. (Optional) Run Migrations
   If you modified models, apply migrations on the running container.
   `sshpass -p 'pswd' ssh -o StrictHostKeyChecking=no mosama@zcircle "cd /mnt/zcircle/app/basma && docker compose exec web python manage.py migrate"`
