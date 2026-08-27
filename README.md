<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=f4b8d4&height=180&section=header&text=✦%20BUBBLE%20TEA%20API%20✦&fontColor=2d1b6e&fontSize=34&desc=a%20kawaii%20api%20for%20managing%20bubble%20teas&descSize=16&descColor=2d1b6e&descAlignY=65&fontAlignY=42" width="100%" alt="Bubble Tea API" />

<br/>

<img src="frontend/src/assets/bbt-lila.png" width="70px"/>
<img src="frontend/src/assets/puddin.png" width="60px"/>
<img src="frontend/src/assets/macaron.png" width="60px"/>
<img src="frontend/src/assets/milk.png" width="60px"/>
<img src="frontend/src/assets/bbt-red.png" width="70px"/>

<br/><br/>

<div align="center">
<a href="README.md"><img src="https://img.shields.io/badge/English-1b2e4b?style=flat-square" alt="English"></a>
<a href="README.es.md"><img src="https://img.shields.io/badge/Espa%C3%B1ol-a8c4f0?style=flat-square&logoColor=1b2e4b" alt="Español"></a>
<a href="README.ca.md"><img src="https://img.shields.io/badge/Català-f4b8d4?style=flat-square&logoColor=2d1b6e" alt="Català"></a>
</div>

<br/>

![Python](https://img.shields.io/badge/Python-3.11-c5b9f0?style=for-the-badge&logo=python&logoColor=2d1b6e)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-f4b8d4?style=for-the-badge&logo=fastapi&logoColor=2d1b6e)
![Angular](https://img.shields.io/badge/Angular-21-a8c4f0?style=for-the-badge&logo=angular&logoColor=2d1b6e)
![MySQL](https://img.shields.io/badge/MySQL-Aiven-b8e8d4?style=for-the-badge&logo=mysql&logoColor=2d1b6e)
![Firebase](https://img.shields.io/badge/Firebase-Auth-f0e4a0?style=for-the-badge&logo=firebase&logoColor=2d1b6e)


<br/>

[![Demo](https://img.shields.io/badge/🌐_Live_Demo-f4b8d4?style=flat-square&logoColor=2d1b6e)](https://bubbletea-api.vercel.app)
&nbsp;
[![API Docs](https://img.shields.io/badge/📖_API_Docs-b8e8d4?style=flat-square&logoColor=2d1b6e)](https://bbt-760x.onrender.com/docs)
&nbsp;
[![Issues](https://img.shields.io/badge/🐛_Issues-a8c4f0?style=flat-square&logoColor=2d1b6e)](https://github.com/mee96/BBT/issues)
[![Keep Alive Active](https://img.shields.io/badge/Keep--Alive-Active-b8e8d4?style=flat-square&logo=githubactions&logoColor=2d1b6e)](https://github.com/mee96/keep-alive)

</div>

<br/>

---

## <img src="https://api.iconify.design/ph/question-fill.svg?color=%23FF6FA8&height=24" height="22"> &nbsp;What is this?

**BubbleTea API** is a full-stack project that lets you explore, manage, and (virtually) taste a collection of 53 bubble teas.

Built as a project combining a **FastAPI** backend with a **MySQL** database on Aiven Cloud, **Firebase** authentication, and an **Angular** frontend with a carefully crafted *kawaii pixel art* aesthetic.

<br/>

---

## <img src="https://api.iconify.design/ph/stack-fill.svg?color=%23B372CF&height=24" height="22"> &nbsp;Technology Stack

| Layer | Technology |
| :--- | :--- |
| <img src="https://api.iconify.design/ph/desktop-tower-fill.svg?color=%23FF6FA8&height=18" height="16"> **Frontend** | Angular 21 · SCSS · Firebase Auth |
| <img src="https://api.iconify.design/ph/cpu-fill.svg?color=%23B372CF&height=18" height="16"> **Backend** | FastAPI · Python 3.11 · SQLAlchemy |
| <img src="https://api.iconify.design/ph/database-fill.svg?color=%235B9BD5&height=18" height="16"> **Base de dades** | MySQL · Aiven Cloud |
| <img src="https://api.iconify.design/ph/key-fill.svg?color=%232FB5AE&height=18" height="16"> **Autenticació** | Firebase Authentication |
| <img src="https://api.iconify.design/ph/rocket-launch-fill.svg?color=%23E0A63B&height=18" height="16"> **Deploy** | Vercel (Frontend) · Render (Backend) |

<br/>

---

## <img src="https://api.iconify.design/ph/code-bold.svg?color=%235B9BD5&height=24" height="22"> &nbsp;Main Endpoints

### <img src="https://api.iconify.design/ph/coffee-fill.svg?color=%23E0A63B&height=20" height="18"> Bubble Teas
<pre><code>GET    /bubbleteas/        → List with filters (category, vegan, hot...)
GET    /bubbleteas/random → Random drink of the day
GET    /bubbleteas/{id}   → Drink details
POST   /bubbleteas/       → Create drink 🔒
PUT    /bubbleteas/{id}   → Edit drink 🔒
DELETE /bubbleteas/{id}   → Soft delete 🔒</code></pre>

### <img src="https://api.iconify.design/ph/user-fill.svg?color=%23FF6FA8&height=20" height="18"> Users
<pre><code>GET    /usuarios/                → User list
POST   /usuarios/                → Registration (public)
GET    /usuarios/firebase/{uid}  → Profile by Firebase UID
PUT    /usuarios/firebase/{uid}  → Update profile 🔒</code></pre>

### <img src="https://api.iconify.design/ph/tag-fill.svg?color=%23B372CF&height=20" height="18"> Other
<pre><code>GET    /categorias/  → Drink categories
GET    /toppings/    → Available toppings
GET    /alergenos/   → Allergen information
GET    /pedidos/     → Orders</code></pre>

> 🔒 *Protected endpoints require a Firebase token (`Authorization: Bearer <token>`).*

<br/>

---

## <img src="https://api.iconify.design/ph/folder-fill.svg?color=%232FB5AE&height=24" height="22"> &nbsp;Project Structure

<pre><code>BBT/
├── 🐍 backend/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   │   ├── bbt.py          → Drink CRUD + filters + JOINs
│   │   ├── categorias.py
│   │   ├── toppings.py
│   │   ├── usuarios.py
│   │   └── pedidos.py
│   └── database/
│
└── 🅰️ frontend/
    └── src/app/
        ├── pages/
        │   ├── home/        → Hero + Stats + Random drink
        │   ├── bebidas/     → Grid with filters 🔒
        │   ├── login/
        │   ├── register/
        │   ├── user/        → Profile + Editing
        │   └── admin/       → CRUD Panel 🔒
        └── services/</code></pre>

<br/>

---

## <img src="https://api.iconify.design/ph/play-fill.svg?color=%23B372CF&height=24" height="22"> &nbsp;Run Locally

### Backend
<pre><code>cd backend
pip install -r requirements.txt
cp .env.example .env    # Fill in the credentials
uvicorn main:app --reload</code></pre>
> ⚡ **Availability:** The backend stays active without *cold starts* thanks to an automatic ping from [Keep-Alive](https://github.com/mee96/keep-alive).
> 
### Frontend
<pre><code>cd frontend
npm install
ng serve</code></pre>

> Open `http://localhost:4200` ✨


<br/>

---

## <img src="https://api.iconify.design/ph/sliders-horizontal-fill.svg?color=%23FF6FA8&height=24" height="22"> &nbsp;Environment Variables

Create a `.env` file in the `backend/` directory:

<pre><code>HOST=...
USER=...
PASSWORD=...
DB=...
PORT=...</code></pre>

*For **Firebase Admin** (required for protected endpoints), add the `FIREBASE_CREDENTIALS` variable with the Service Account JSON.*

<br/>

---

## <img src="https://api.iconify.design/ph/sparkle-fill.svg?color=%235B9BD5&height=24" height="22"> &nbsp;Key Features

* <img src="https://api.iconify.design/ph/coffee-fill.svg?color=%23E0A63B&height=18" height="16"> **53 Bubble Teas:** Complete catalog with categories, toppings, and allergens.
* <img src="https://api.iconify.design/ph/dice-five-fill.svg?color=%23B372CF&height=18" height="16"> **Random drink of the day:** Dynamic generator on the user profile.
* <img src="https://api.iconify.design/ph/funnel-fill.svg?color=%232FB5AE&height=18" height="16"> **Advanced filters:** By vegan, hot, category, or active status.
* <img src="https://api.iconify.design/ph/shield-check-fill.svg?color=%23FF6FA8&height=18" height="16"> **Firebase Authentication:** With `firebase_uid` integrated as the user PK.
* <img src="https://api.iconify.design/ph/trash-fill.svg?color=%235B9BD5&height=18" height="16"> **Soft Delete:** Drinks are never physically removed from the database.
* <img src="https://api.iconify.design/ph/paint-brush-broad-fill.svg?color=%23B372CF&height=18" height="16"> **Kawaii Aesthetic:** Pixel art design with the *Press Start 2P* font.

<br/>

---

<div align="center">

<img src="frontend/src/assets/pusheen.png" width="70px"/>

<br/>

<b>made with 🧋 for the love of 🧋</b>

<br/><br/>

Developed by **Carme Medina Canalda**<br/>
*Full Stack Developer · Barcelona*

*"If the architecture is right, everything will fit"*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-a8c4f0?style=flat-square&logo=linkedin&logoColor=2d1b6e)](https://www.linkedin.com/in/carme-medina-canalda-250457132/)
[![Portfolio](https://img.shields.io/badge/Portfolio-c5b9f0?style=flat-square&logoColor=2d1b6e)](https://carme-portfoli.onrender.com/)

</div>
