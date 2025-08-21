
Job Tracker App - Dependencies & Setup (Ubuntu EC2)
===================================================

1. Update System
----------------
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl build-essential

2. Install Node.js & NPM
-------------------------
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v

3. Backend Setup
-----------------
cd job-tracker/backend/
npm install express cors dotenv mongoose
npm install nodemon --save-dev

(Ensure MongoDB Atlas or local MongoDB connection is configured in .env file)

4. Frontend Setup
------------------
cd job-tracker/frontend/
npm install

5. Build Tools (Production)
----------------------------
sudo apt install -y nginx
sudo npm install -g pm2

6. Optional: Docker Setup
--------------------------
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker --now

7. Run App
-----------
Frontend (dev mode): npm run dev -- --host 0.0.0.0
Backend: node server.js
Backend (PM2): pm2 start server.js

Checklist
---------
- [x] Git installed
- [x] Node.js + NPM installed
- [x] Backend dependencies installed
- [x] Frontend dependencies installed
- [x] Nginx installed (for production frontend serving)
- [x] PM2 installed (backend process management)
- [x] MongoDB connection setup (Atlas/local)
- [ ] Optional: Docker installed
