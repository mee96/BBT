<div align="center">

<img src="frontend/src/assets/bbt-lila.png" width="80px" align="left"/>
<img src="frontend/src/assets/bbt-red.png" width="80px" align="right"/>

```
           ╔══════════════════════════════════════════════════════╗
           ║  ✦ B U B B L E T E A   A P I  ✦                     ║
           ║  🧋 una api kawaii para gestionar bubble teas 🧋    ║
           ╚══════════════════════════════════════════════════════╝
```

<img src="frontend/src/assets/puddin.png" width="70px"/>
<img src="frontend/src/assets/macaron.png" width="70px"/>
<img src="frontend/src/assets/milk.png" width="70px"/>

![Python](https://img.shields.io/badge/Python-3.11-a0c4ff?style=flat-square&logo=python&logoColor=white&labelColor=7b4fa6)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-f9d0f0?style=flat-square&logo=fastapi&logoColor=white&labelColor=c77dcc)
![Angular](https://img.shields.io/badge/Angular-21-ffd6e7?style=flat-square&logo=angular&logoColor=white&labelColor=7b4fa6)
![MySQL](https://img.shields.io/badge/MySQL-Aiven-a0d8ef?style=flat-square&logo=mysql&logoColor=white&labelColor=c77dcc)
![Firebase](https://img.shields.io/badge/Firebase-Auth-ffe5b4?style=flat-square&logo=firebase&logoColor=white&labelColor=7b4fa6)

**[🌐 Demo en viu](https://bubbletea-api.vercel.app)** · **[📖 API Docs](https://bbt-760x.onrender.com/docs)** · **[🐛 Issues](https://github.com/mee96/BBT/issues)**

</div>

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   què és això?                   │
└─────────────────────────────────────────┘
```

**BubbleTea API** és un projecte full-stack que permet explorar, gestionar i degustar (virtualment) una col·lecció de 55 bubble teas 🧋

Construït com a projecte que combina un backend en FastAPI amb una base de dades MySQL a Aiven, autenticació Firebase, i un frontend Angular amb estètica pixel art kawaii.

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   stack                          │
└─────────────────────────────────────────┘
```

| Capa | Tecnologia |
|------|-----------|
| 🔮 Frontend | Angular 21 · SCSS · Firebase Auth |
| ⚡ Backend | FastAPI · Python 3.11 · SQLAlchemy |
| 🗄️ Base de dades | MySQL · Aiven Cloud |
| 🔐 Auth | Firebase Authentication |
| 🚀 Deploy | Vercel (frontend) · Render (backend) |

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   endpoints principals           │
└─────────────────────────────────────────┘
```

### 🧋 Bubble Teas
```
GET    /bubbleteas/              → llista amb filtres (categoria, vegà, calent...)
GET    /bubbleteas/random        → beguda aleatòria del dia
GET    /bubbleteas/{id}          → detall d'una beguda
POST   /bubbleteas/              → crear beguda 🔒
PUT    /bubbleteas/{id}          → editar beguda 🔒
DELETE /bubbleteas/{id}          → soft delete 🔒
```

### 👤 Usuaris
```
GET    /usuarios/                → llista d'usuaris
POST   /usuarios/                → registre (públic)
GET    /usuarios/firebase/{uid}  → perfil per UID Firebase
PUT    /usuarios/firebase/{uid}  → actualitzar perfil 🔒
```

### 🏷️ Altres
```
GET    /categorias/              → categories de begudes
GET    /toppings/                → toppings disponibles
GET    /alergenos/               → informació d'al·lèrgens
GET    /pedidos/                 → comandes
```

> 🔒 Endpoints protegits requereixen token Firebase (`Authorization: Bearer <token>`)

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   estructura del projecte        │
└─────────────────────────────────────────┘
```

```
BBT/
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
        │   ├── home/        → hero + stats + beguda random
        │   ├── bebidas/     → grid amb filtres 🔒
        │   ├── login/
        │   ├── register/
        │   ├── user/        → perfil + edició
        │   └── admin/       → CRUD panel 🔒
        └── services/
```

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   com arrencar en local          │
└─────────────────────────────────────────┘
```

### Backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env   # omple les credencials
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
ng serve
```

> Accedeix a `http://localhost:4200` ✨

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   variables d'entorn             │
└─────────────────────────────────────────┘
```

Crea un fitxer `.env` al directori `backend/`:

```env
HOST=...
USER=...
PASSWORD=...
DB=...
PORT=...
```

Per a Firebase Admin (necessari per a endpoints protegits), afegeix la variable `FIREBASE_CREDENTIALS` amb el JSON del service account.

---

```
┌─────────────────────────────────────────┐
│  ● ● ●   característiques               │
└─────────────────────────────────────────┘
```

- 🧋 **55 bubble teas** amb categories, toppings i al·lèrgens
- 🎲 **Beguda aleatòria del dia** al perfil d'usuari
- 🌱 Filtres per **vegà**, **calent**, **categoria**, **actiu**
- 🔐 **Autenticació Firebase** amb `firebase_uid` com a PK d'usuari
- 🗑️ **Soft delete** — les begudes mai es perden de la BD
- 🎨 Disseny **pixel art kawaii** amb font Press Start 2P
- 📱 Layout responsive amb fons quadriculat pastel

---

<div align="center">

<img src="frontend/src/assets/pusheen.png" width="80px"/>

```
┌───────────────────────────────────────────┐
│  ● ● ●   fet amb 🧋 per amor als 🧋      │
└───────────────────────────────────────────┘
```

**Carmen Medina** ·Programadora Full Stack · 2026

*"si l'arquitectura és correcta, tot encaixarà"*

</div>
