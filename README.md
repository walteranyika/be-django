
# 🐍 Django Deployment on Render Guide

This is a step-by-step guide for deploying a Django backend project on [Render](https://render.com).

---

## ✅ Prerequisites
- Django project with `sqlite3` or PostgreSQL
- GitHub repo with your project
- `requirements.txt` file
- `Procfile`
- Optional: `render.yaml` file

---

## 🔧 Step 1: Prepare Your Django Project

### 1.1 Add `gunicorn`
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### 1.2 Create a `Procfile`
```
web: gunicorn your_project_name.wsgi
```

### 1.3 Update `settings.py`
```python
ALLOWED_HOSTS = ['your-service-name.onrender.com']
```

### 1.4 (Optional) Add `render.yaml`
```yaml
services:
  - type: web
    name: django-app
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn your_project_name.wsgi
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: your_project_name.settings
```

---

## 🛠️ Step 2: Push to GitHub

```bash
git init
git remote add origin https://github.com/yourusername/yourrepo.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 🚀 Step 3: Deploy on Render

1. Go to [https://dashboard.render.com](https://dashboard.render.com)
2. Click **"New Web Service"**
3. Connect your GitHub repo
4. Fill in:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `gunicorn your_project_name.wsgi`
   - **Environment**: Python 3.x
5. Add environment variables:
   - `PYTHON_VERSION=3.x`
   - `DJANGO_SETTINGS_MODULE=your_project_name.settings`

---

## 💾 Step 4: Database (Optional)

- SQLite works for demos, but not recommended for production.
- Use Render PostgreSQL:
  - Dashboard → Databases → New PostgreSQL
  - Update `DATABASES` in `settings.py`

---

## 🧪 Step 5: Migrate the Database

Use the Render Shell:
```bash
python manage.py migrate
```

---

## 🎉 You're Live!

Your app will be available at:
```
https://your-service-name.onrender.com
```

Happy coding!
