# Streamlit Authentication Demo (Microsoft Entra ID)

This repository contains a minimal example of authentication in a Streamlit application using **OpenID Connect** with **Microsoft Entra ID**.

It demonstrates how to:
- authenticate users with an external Identity Provider (IdP)
- manage sessions using Streamlit built-in authentication
- retrieve user information from the authentication token

---

## 📖 Full Guide

This project is explained step-by-step in the accompanying article:

👉 https://medium.com/p/66171ab88555

The article covers:
- authentication flow in Streamlit
- Microsoft Entra ID configuration
- limitations of the built-in approach
- production considerations

---

## 🚀 Getting Started

### 1. Install dependencies

Make sure you have `uv` installed (or use your preferred Python environment manager):

```bash
uv sync
```

### 2.Configure authentication

Create a .streamlit/secrets.toml file:

[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "your-cookie-secret"

[auth.microsoft]
client_id = "your-client-id"
client_secret = "your-client-secret"
server_metadata_url = "https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration"

⚠️ Do not commit this file.

### 3. Run the app

```bash
make run
```

### 🧪 What this demo shows
Login / logout flow
Session persistence via cookies
Access to user information via st.user

### ⚠️ Limitations

This setup is great for quick prototypes but has limitations:

cookie duration is not configurable
relies on a local secrets.toml file
not ideal for containerized production environments

👉 See the article for a deeper discussion and workarounds.