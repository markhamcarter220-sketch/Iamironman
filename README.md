
# 🧾 IronLord Deploy Guide

This README includes **everything you need** to deploy both the backend (Render) and frontend (Vercel) using the files inside `IAMIronMan.zip`.

---

## 🔧 Backend (FastAPI) — Deploy to Render

### ✅ Required Files
- `backend/`
- `render.yaml`
- `.env.example` (use values below)

### 🌐 Create Web Service on [Render](https://render.com)
1. Click **New > Web Service**
2. Choose **GitHub repo** or **upload zip**
3. Set Root Directory to: `backend/`

### ⚙️ Auto-Populated Build Settings (via render.yaml)
| Field           | Value                                                      |
|----------------|-------------------------------------------------------------|
| Environment     | Python 3                                                    |
| Build Command   | `pip install -r requirements.txt`                           |
| Start Command   | `uvicorn main:app --host=0.0.0.0 --port=$PORT`              |
| Root Directory  | `backend/`                                                  |
| Instance Type   | Free or Starter                                             |

### 🌍 Environment Variables
Set these in the Render dashboard under "Environment":
```
MONGO_URI=mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.mongodb.net/betterbets?retryWrites=true&w=majority
ODDS_API_KEY=5fa1e2aaf9d7312569798e5c8354ecd5
PORT=10000
```

After deploy, you will get your backend URL (e.g., `https://ironlord-backend.onrender.com`)

---

## ⚛️ Frontend (React/Vite) — Deploy to Vercel

### ✅ Required Files
- `frontend/`

### 🌐 Deploy Steps
1. Go to [Vercel](https://vercel.com)
2. Click **New Project**
3. Import GitHub repo (or upload frontend manually)
4. Set Framework to: `Vite` or `React`
5. Set Root Directory to: `frontend/`

### ⚙️ Vercel Settings
| Field           | Value              |
|----------------|---------------------|
| Build Command   | `npm run build`     |
| Output Dir      | `dist`              |
| Environment     | `VITE_API_URL=https://<your-render-backend-url>` |

Replace the URL with your actual Render backend URL.

---

## ✅ .env.example (included)
```
MONGO_URI=
ODDS_API_KEY=5fa1e2aaf9d7312569798e5c8354ecd5
VITE_API_URL=
PORT=10000
```

---

## 🚀 Go Live
Once both deploys complete:
- Visit Vercel URL → Frontend loads
- Click a scan button → Data loads from Render
- Share link with friends

This is your live SaaS foundation.
