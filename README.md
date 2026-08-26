<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=f4b8d4&height=180&section=header&text=✦%20BUBBLE%20TEA%20API%20✦&fontColor=2d1b6e&fontSize=34&desc=una%20api%20kawaii%20para%20gestionar%20bubble%20teas&descSize=16&descColor=2d1b6e&descAlignY=65&fontAlignY=42" width="100%" alt="Bubble Tea API" />

<br/>

<img src="frontend/src/assets/bbt-lila.png" width="70px"/>
<img src="frontend/src/assets/puddin.png" width="60px"/>
<img src="frontend/src/assets/macaron.png" width="60px"/>
<img src="frontend/src/assets/milk.png" width="60px"/>
<img src="frontend/src/assets/bbt-red.png" width="70px"/>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.11-c5b9f0?style=for-the-badge&logo=python&logoColor=2d1b6e)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-f4b8d4?style=for-the-badge&logo=fastapi&logoColor=2d1b6e)
![Angular](https://img.shields.io/badge/Angular-21-a8c4f0?style=for-the-badge&logo=angular&logoColor=2d1b6e)
![MySQL](https://img.shields.io/badge/MySQL-Aiven-b8e8d4?style=for-the-badge&logo=mysql&logoColor=2d1b6e)
![Firebase](https://img.shields.io/badge/Firebase-Auth-f0e4a0?style=for-the-badge&logo=firebase&logoColor=2d1b6e)

<br/>

[![Demo](https://img.shields.io/badge/🌐_Demo_en_viu-f4b8d4?style=flat-square&logoColor=2d1b6e)](https://bubbletea-api.vercel.app)
&nbsp;
[![API Docs](https://img.shields.io/badge/📖_API_Docs-b8e8d4?style=flat-square&logoColor=2d1b6e)](https://bbt-760x.onrender.com/docs)
&nbsp;
[![Issues](https://img.shields.io/badge/🐛_Issues-a8c4f0?style=flat-square&logoColor=2d1b6e)](https://github.com/mee96/BBT/issues)

</div>

<br/>

---

## <img src="https://api.iconify.design/ph/question-fill.svg?color=%23FF6FA8&height=24" height="22"> &nbsp;Què és això?

**BubbleTea API** és un projecte full-stack que permet explorar, gestionar i degustar (virtualment) una col·lecció de 55 bubble teas.

Construït com a projecte que combina un backend en **FastAPI** amb una base de dades **MySQL** a Aiven Cloud, autenticació amb **Firebase**, i un frontend **Angular** amb una acurada estètica *pixel art kawaii*.

<br/>

---

## <img src="https://api.iconify.design/ph/stack-fill.svg?color=%23B372CF&height=24" height="22"> &nbsp;Stack Tecnològic

| Capa | Tecnologia |
| :--- | :--- |
| <img src="https://api.iconify.design/ph/desktop-tower-fill.svg?color=%23FF6FA8&height=18" height="16"> **Frontend** | Angular 21 · SCSS · Firebase Auth |
| <img src="https://api.iconify.design/ph/cpu-fill.svg?color=%23B372CF&height=18" height="16"> **Backend** | FastAPI · Python 3.11 · SQLAlchemy |
| <img src="https://api.iconify.design/ph/database-fill.svg?color=%235B9BD5&height=18" height="16"> **Base de dades** | MySQL · Aiven Cloud |
| <img src="https://api.iconify.design/ph/key-fill.svg?color=%232FB5AE&height=18" height="16"> **Autenticació** | Firebase Authentication |
| <img src="https://api.iconify.design/ph/rocket-launch-fill.svg?color=%23E0A63B&height=18" height="16"> **Deploy** | Vercel (Frontend) · Render (Backend) |

<br/>

---

## <img src="https://api.iconify.design/ph/code-bold.svg?color=%235B9BD5&height=24" height="22"> &nbsp;Endpoints principals

### <img src="https://api.iconify.design/ph/coffee-fill.svg?color=%23E0A63B&height=20" height="18"> Bubble Teas
<pre><code>GET    /bubbleteas/        → Llista amb filtres (categoria, vegà, calent...)
GET    /bubbleteas/random → Beguda aleatòria del dia
GET    /bubbleteas/{id}   → Detall d'una beguda
POST   /bubbleteas/       → Crear beguda 🔒
PUT    /bubbleteas/{id}   → Editar beguda 🔒
DELETE /bubbleteas/{id}   → Soft delete 🔒</code></pre>

### <img src="https://api.iconify.design/ph/user-fill.svg?color=%23FF6FA8&height=20" height="18"> Usuaris
<pre><code>GET    /usuarios/                → Llista d'usuaris
POST   /usuarios/                → Registre (públic)
GET    /usuarios/firebase/{uid}  → Perfil per UID Firebase
PUT    /usuarios/firebase/{uid}  → Actualitzar perfil 🔒</code></pre>

### <img src="https://api.iconify.design/ph/tag-fill.svg?color=%23B372CF&height=20" height="18"> Altres
<pre><code>GET    /categorias/  → Categories de begudes
GET    /toppings/    → Toppings disponibles
GET    /alergenos/   → Informació d'al·lèrgens
GET    /pedidos/     → Comandes</code></pre>

> 🔒 *Els endpoints protegits requereixen token Firebase (`Authorization: Bearer <token>`).*

<br/>

---

## <img src="https://api.iconify.design/ph/folder-fill.svg?color=%232FB5AE&height=24" height="22"> &nbsp;Estructura del projecte

<pre><code>BBT/
├── 🐍 backend/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   │   ├── bbt.py          → CRUD begudes + filtres + JOINs
│   │   ├── categorias.py
│   │   ├── toppings.py
│   │   ├── usuarios.py
│   │   └── pedidos.py
│   └── database/
│
└── 🅰️ frontend/
    └── src/app/
        ├── pages/
        │   ├── home/        → Hero + Stats + Beguda random
        │   ├── bebidas/     → Grid amb filtres 🔒
        │   ├── login/
        │   ├── register/
        │   ├── user/        → Perfil + Edició
        │   └── admin/       → Panel CRUD 🔒
        └── services/</code></pre>

<br/>

---

## <img src="https://api.iconify.design/ph/play-fill.svg?color=%23B372CF&height=24" height="22"> &nbsp;Com arrencar en local

### Backend
<pre><code>cd backend
pip install -r requirements.txt
cp .env.example .env    # Omple les credencials
uvicorn main:app --reload</code></pre>

### Frontend
<pre><code>cd frontend
npm install
ng serve</code></pre>

> Accedeix a `http://localhost:4200` ✨

<br/>

---

## <img src="https://api.iconify.design/ph/sliders-horizontal-fill.svg?color=%23FF6FA8&height=24" height="22"> &nbsp;Variables d'entorn

Crea un fitxer `.env` al directori `backend/`:

<pre><code>HOST=...
USER=...
PASSWORD=...
DB=...
PORT=...</code></pre>

*Per a **Firebase Admin** (necessari per als endpoints protegits), afegeix la variable `FIREBASE_CREDENTIALS` amb el JSON del Service Account.*

<br/>

---

## <img src="https://api.iconify.design/ph/sparkle-fill.svg?color=%235B9BD5&height=24" height="22"> &nbsp;Característiques principals

* <img src="https://api.iconify.design/ph/coffee-fill.svg?color=%23E0A63B&height=18" height="16"> **55 Bubble Teas:** Catàleg complet amb categories, toppings i al·lèrgens.
* <img src="https://api.iconify.design/ph/dice-five-fill.svg?color=%23B372CF&height=18" height="16"> **Beguda aleatòria del dia:** Generador dinàmic al perfil d'usuari.
* <img src="https://api.iconify.design/ph/funnel-fill.svg?color=%232FB5AE&height=18" height="16"> **Filtres avançats:** Per vegà, calent, categoria o estat actiu.
* <img src="https://api.iconify.design/ph/shield-check-fill.svg?color=%23FF6FA8&height=18" height="16"> **Autenticació Firebase:** Amb `firebase_uid` integrat com a PK d'usuari.
* <img src="https://api.iconify.design/ph/trash-fill.svg?color=%235B9BD5&height=18" height="16"> **Soft Delete:** Les begudes no s'eliminen mai físicament de la BD.
* <img src="https://api.iconify.design/ph/paint-brush-broad-fill.svg?color=%23B372CF&height=18" height="16"> **Estètica Kawaii:** Disseny pixel art amb la font *Press Start 2P*.

<br/>

---

<div align="center">

<img src="frontend/src/assets/pusheen.png" width="70px"/>

<br/>

<b>fet amb 🧋 per amor als 🧋</b>

<br/><br/>

Desenvolupat per **Carme Medina Canalda**  
*Full Stack Developer · Barcelona*

*"Si l'arquitectura és correcta, tot encaixarà"*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-a8c4f0?style=flat-square&logo=linkedin&logoColor=2d1b6e)](https://www.linkedin.com/in/carme-medina-canalda-250457132/)
[![Portfolio](https://img.shields.io/badge/Portfolio-c5b9f0?style=flat-square&logoColor=2d1b6e)](https://carme-portfoli.onrender.com/)

</div>
