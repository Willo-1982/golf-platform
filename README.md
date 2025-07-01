# ⛳ Golf Platform

🚀 A full-stack modern golf app — secure FastAPI backend + Streamlit frontend + PWA mobile shell.

---

## 📦 Features

✅ Secure JWT login  
✅ WHS handicap index with <20 rounds adjustment  
✅ Strokes gained analysis  
✅ Swing video library (link or upload)  
✅ Groups, friends, competitions, leaderboards  
✅ GPS maps with Mapbox / Google toggle  
✅ Push notifications (via OneSignal)  
✅ PWA mobile installable

---

## 🚀 Local setup

### 🔥 Backend (FastAPI)
```bash
cd fastapi-backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Runs at `http://127.0.0.1:8000`.

### 🏌️ Frontend (Streamlit)
```bash
cd ../streamlit-app
pip install -r requirements.txt
streamlit run app.py
```
Runs at `http://localhost:8501`.

### 📱 PWA shell
- Open `pwa-shell/index.html` or deploy to Netlify / Vercel.

---

## 🌐 Deploy

### 🚀 Backend
- Deploy to Heroku / Render (runs `uvicorn main:app`).

### 🚀 Streamlit
- Deploy to [streamlit.io](https://share.streamlit.io/) (100% free).

### 🚀 PWA
- Push repo to GitHub.
- Link to Netlify or Vercel, set **publish directory** to `/pwa-shell`.

---

## 🚀 OneSignal Setup
1. Sign up at [https://onesignal.com](https://onesignal.com).
2. Create a new **Web Push app**.
3. Enter your Netlify site URL.
4. Copy your `appId` into `pwa-shell/index.html`.

---

## 📝 License
Open source & fully yours to run. Build your own club, or even commercial product.

---

## ⚙️ Environment Configuration

This project uses a `.env` file to keep secrets and settings out of your codebase.

### 🔥 How to set up your environment variables

1️⃣ Copy the example file:

```bash
cp fastapi-backend/.env.example fastapi-backend/.env
```

2️⃣ Edit `.env` and fill in your real secrets, for example:

```
SECRET_KEY="super-secret-key"
DATABASE_URL="sqlite:///./test.db"
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

3️⃣ Your `.env` is automatically ignored by Git (thanks to `.gitignore`).

---

### 🚀 Run locally with these environment variables
In your `/fastapi-backend` folder, start your server:

```bash
uvicorn main:app --reload
```

✅ It will load all values from `.env` automatically.

---

### 💡 Notes
- **Never commit your actual `.env` file.**  
- You can safely commit `.env.example` to show what needs to be set.

---

