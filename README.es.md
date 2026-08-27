<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=f4b8d4&height=180&section=header&text=✦%20BUBBLE%20TEA%20API%20✦&fontColor=2d1b6e&fontSize=34&desc=una%20api%20kawaii%20para%20gestionar%20bubble%20teas&descSize=16&descColor=2d1b6e&descAlignY=65&fontAlignY=42" width="100%" alt="Bubble Tea API" />

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
</div>

<br/>

![Python](https://img.shields.io/badge/Python-3.11-c5b9f0?style=for-the-badge&logo=python&logoColor=2d1b6e)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-f4b8d4?style=for-the-badge&logo=fastapi&logoColor=2d1b6e)
![Angular](https://img.shields.io/badge/Angular-21-a8c4f0?style=for-the-badge&logo=angular&logoColor=2d1b6e)
![MySQL](https://img.shields.io/badge/MySQL-Aiven-b8e8d4?style=for-the-badge&logo=mysql&logoColor=2d1b6e)
![Firebase](https://img.shields.io/badge/Firebase-Auth-f0e4a0?style=for-the-badge&logo=firebase&logoColor=2d1b6e)

<br/>

[![Demo](https://img.shields.io/badge/🌐_Demo_en_vivo-f4b8d4?style=flat-square&logoColor=2d1b6e)](https://bubbletea-api.vercel.app)
&nbsp;
[![API Docs](https://img.shields.io/badge/📖_API_Docs-b8e8d4?style=flat-square&logoColor=2d1b6e)](https://bbt-760x.onrender.com/docs)
&nbsp;
[![Issues](https://img.shields.io/badge/🐛_Issues-a8c4f0?style=flat-square&logoColor=2d1b6e)](https://github.com/mee96/BBT/issues)
[![Keep Alive Active](https://img.shields.io/badge/Keep--Alive-Active-b8e8d4?style=flat-square&logo=githubactions&logoColor=2d1b6e)](https://github.com/mee96/keep-alive)

</div>

<br/>

---

## <img src="https://api.iconify.design/ph/question-fill.svg?color=%23FF6FA8&height=24" height="22"> &nbsp;¿Qué es esto?

**BubbleTea API** es un proyecto full-stack que permite explorar, gestionar y degustar (virtualmente) una colección de 53 bubble teas.

Construido como un proyecto que combina un backend en **FastAPI** con una base de datos **MySQL** en Aiven Cloud, autenticación con **Firebase** y un frontend **Angular** con una cuidada estética *pixel art kawaii*.

<br/>

---

## <img src="https://api.iconify.design/ph/stack-fill.svg?color=%23B372CF&height=24" height="22"> &nbsp;Stack Tecnológico

| Capa | Tecnología |
| :--- | :--- |
| <img src="https://api.iconify.design/ph/desktop-tower-fill.svg?color=%23FF6FA8&height=18" height="16"> **Frontend** | Angular 21 · SCSS · Firebase Auth |
| <img src="https://api.iconify.design/ph/cpu-fill.svg?color=%23B372CF&height=18" height="16"> **Backend** | FastAPI · Python 3.11 · SQLAlchemy |
| <img src="https://api.iconify.design/ph/database-fill.svg?color=%235B9BD5&height=18" height="16"> **Base de datos** | MySQL · Aiven Cloud |
| <img src="https://api.iconify.design/ph/key-fill.svg?color=%232FB5AE&height=18" height="16"> **Autenticación** | Firebase Authentication |
| <img src="https://api.iconify.design/ph/rocket-launch-fill.svg?color=%23E0A63B&height=18" height="16"> **Deploy** | Vercel (Frontend) · Render (Backend) |

<br/>

---

## <img src="https://api.iconify.design/ph/code-bold.svg?color=%235B9BD5&height=24" height="22"> &nbsp;Endpoints principales

### <img src="https://api.iconify.design/ph/coffee-fill.svg?color=%23E0A63B&height=20" height="18"> Bubble Teas
<pre><code>GET    /bubbleteas/        → Lista con filtros (categoría, vegano, caliente...)
GET    /bubbleteas/random → Bebida aleatoria del día
GET    /bubbleteas/{id}   → Detalle de una bebida
POST   /bubbleteas/       → Crear bebida 🔒
PUT    /bubbleteas/{id}   → Editar bebida 🔒
DELETE /bubbleteas/{id}   → Soft delete 🔒</code></pre>

### <img src="https://api.iconify.design/ph/user-fill.svg?color=%23FF6FA8&height=20" height="18"> Usuarios
<pre><code>GET    /usuarios/                → Lista de usuarios
POST   /usuarios/                → Registro (público)
GET    /usuarios/firebase/{uid}  → Perfil por UID de Firebase
PUT    /usuarios/firebase/{uid}  → Actualizar perfil 🔒</code></pre>

### <img src="https://api.iconify.design/ph/tag-fill.svg?color=%23B372CF&height=20" height="18"> Otros
<pre><code>GET    /categorias/  → Categorías de bebidas
GET    /toppings/    → Toppings disponibles
GET    /alergenos/   → Información sobre alérgenos
GET    /pedidos/     → Pedidos</code></pre>

> 🔒 *Los endpoints protegidos requieren un token de Firebase (`Authorization: Bearer <token>`).*

<br/>

---

## <img src="https://api.iconify.design/ph/folder-fill.svg?color=%232FB5AE&height=24" height="22"> &nbsp;Estructura del proyecto

<pre><code>BBT/
├── 🐍 backend/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   │   ├── bbt.py          → CRUD de bebidas + filtros + JOINs
│   │   ├── categorias.py
│   │   ├── toppings.py
│   │   ├── usuarios.py
│   │   └── pedidos.py
│   └── database/
│
└── 🅰️ frontend/
    └── src/app/
        ├── pages/
        │   ├── home/        → Hero + Stats + Bebida aleatoria
        │   ├── bebidas/     → Grid con filtros 🔒
        │   ├── login/
        │   ├── register/
        │   ├── user/        → Perfil + Edición
        │   └── admin/       → Panel CRUD 🔒
        └── services/</code></pre>

<br/>

---

## <img src="https://api.iconify.design/ph/play-fill.svg?color=%23B372CF&height=24" height="22"> &nbsp;Cómo ejecutar en local

### Backend
<pre><code>cd backend
pip install -r requirements.txt
cp .env.example .env    # Completa las credenciales
uvicorn main:app --reload</code></pre>
> ⚡ **Disponibilidad:** El backend se mantiene activo sin *cold starts* gracias a un ping automático de [Keep-Alive](https://github.com/mee96/keep-alive).
>
### Frontend
<pre><code>cd frontend
npm install
ng serve</code></pre>

> Accede a `http://localhost:4200` ✨

<br/>

---

## <img src="https://api.iconify.design/ph/sliders-horizontal-fill.svg?color=%23FF6FA8&height=24" height="22"> &nbsp;Variables de entorno

Crea un archivo `.env` en el directorio `backend/`:

<pre><code>HOST=...
USER=...
PASSWORD=...
DB=...
PORT=...</code></pre>

*Para **Firebase Admin** (necesario para los endpoints protegidos), añade la variable `FIREBASE_CREDENTIALS` con el JSON de la cuenta de servicio.*

<br/>

---

## <img src="https://api.iconify.design/ph/sparkle-fill.svg?color=%235B9BD5&height=24" height="22"> &nbsp;Características principales

* <img src="https://api.iconify.design/ph/coffee-fill.svg?color=%23E0A63B&height=18" height="16"> **53 Bubble Teas:** Catálogo completo con categorías, toppings y alérgenos.
* <img src="https://api.iconify.design/ph/dice-five-fill.svg?color=%23B372CF&height=18" height="16"> **Bebida aleatoria del día:** Generador dinámico en el perfil de usuario.
* <img src="https://api.iconify.design/ph/funnel-fill.svg?color=%232FB5AE&height=18" height="16"> **Filtros avanzados:** Por vegano, caliente, categoría o estado activo.
* <img src="https://api.iconify.design/ph/shield-check-fill.svg?color=%23FF6FA8&height=18" height="16"> **Autenticación Firebase:** Con `firebase_uid` integrado como PK de usuario.
* <img src="https://api.iconify.design/ph/trash-fill.svg?color=%235B9BD5&height=18" height="16"> **Soft Delete:** Las bebidas nunca se eliminan físicamente de la base de datos.
* <img src="https://api.iconify.design/ph/paint-brush-broad-fill.svg?color=%23B372CF&height=18" height="16"> **Estética Kawaii:** Diseño pixel art con la fuente *Press Start 2P*.

<br/>

---

<div align="center">

<img src="frontend/src/assets/pusheen.png" width="70px"/>

<br/>

<b>hecho con 🧋 por amor a los 🧋</b>

<br/><br/>

Desarrollado por **Carme Medina Canalda**  
*Full Stack Developer · Barcelona*

*"Si la arquitectura es correcta, todo encajará"*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-a8c4f0?style=flat-square&logo=linkedin&logoColor=2d1b6e)](https://www.linkedin.com/in/carme-medina-canalda-250457132/)
[![Portfolio](https://img.shields.io/badge/Portfolio-c5b9f0?style=flat-square&logoColor=2d1b6e)](https://carme-portfoli.onrender.com/)

</div>