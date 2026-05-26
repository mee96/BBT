# Home Desktop Layout — Design Spec
**Date:** 2026-05-25  
**Branch:** dev  
**Files affected:** `frontend/src/app/pages/home/home.html`, `frontend/src/app/pages/home/home.scss`

---

## Objectiu

Implementar un layout de 3 files en grid per a desktop (≥ 768 px) a la pàgina home, mantenint el layout d'una sola columna a mobile (≤ 767 px). Tot el contingut i la lògica Angular existent (`bebidaRandom`, `loading`, `error`, `tabActiu`, `carregarRandom`, `copiarUrl`) es conserva intacte.

---

## Estructura HTML

S'afegiran 3 contenidors `.home-row` dins de `<main class="home">`. Cap canvi a `home.ts`.

```
<main class="home">

  <!-- FILA 1: 1.3fr | 0.9fr -->
  <div class="home-row home-row-1">
    ├── .pbox.pbox-pink          ← hero existent (sense canvis interns)
    └── .row1-right
          ├── <img src="assets/bbt-lila.png" class="bbt-lila-deco">
          └── .pbox.stats-inline
                ├── .titlebar  (stats.exe)
                └── .stats-row
                      ├── .stat-item  17 bebidas
                      ├── .stat-item  7  cats      (border-left dashed)
                      ├── .stat-item  8  tops      (border-left dashed)
                      └── .stat-item  11 ep        (border-left dashed)

  <!-- FILA 2: 0.8fr | 1.2fr -->
  <div class="home-row home-row-2">
    ├── <section class="section">  sec-title "BEGUDA DEL MOMENT" + .pbox.pbox-yellow
    └── <section class="section">  sec-title "ENDPOINTS"         + .pbox

  <!-- FILA 3: 1fr | auto -->
  <div class="home-row home-row-3">
    ├── <section class="section">  sec-title + sec-sub + .pbox-dark (codi)
    └── .deco-svgs                ← contenidor buit per a 2 SVGs decoratius (usuari)
```

### Canvi als stats

Els 4 elements `.pbox.stat` actuals s'eliminen. Substituïts per **un únic `.pbox`** (`.stats-inline`) amb:
- `titlebar` estàndard → títol `stats.exe`
- `.stats-row` (flexbox fila) amb 4 `.stat-item`
- Cada `.stat-item` mostra número gran + label curt
- A partir del segon, `border-left: 1.5px dashed #b8a0d0`
- Labels: **bebidas**, **cats**, **tops**, **ep**

---

## CSS

### Mobile-first (≤ 767 px)

`.home-row` → `display: flex; flex-direction: column; gap: 16px`

Ordre visual en mobile (= ordre DOM):
1. Hero (pbox-pink)
2. Imatge bbt-lila + stats inline
3. Beguda del moment
4. Endpoints
5. Exemples de codi
6. Contenidor SVGs decoratius

### Desktop (≥ 768 px)

`.home-row` → `display: grid; align-items: start`

| Classe | `grid-template-columns` |
|---|---|
| `.home-row-1` | `1.3fr 0.9fr` |
| `.home-row-2` | `0.8fr 1.2fr` |
| `.home-row-3` | `1fr auto` |

### Imatge `bbt-lila.png`

```scss
.bbt-lila-deco {
  display: block;
  width: 100%;
  max-width: 200px;
  height: auto;
  margin: 0 auto;
  transform: rotate(-6deg);
}
```

Visible tant a mobile com a desktop (apilada sobre l'stats pbox a mobile).

### `.row1-right`

```scss
.row1-right {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
```

### `.stats-row` / `.stat-item`

```scss
.stats-row {
  display: flex;
  padding: 12px;
}

.stat-item {
  flex: 1;
  text-align: center;
  padding: 8px 12px;

  & + .stat-item {
    border-left: 1.5px dashed #b8a0d0;
  }
}
```

### `.deco-svgs`

```scss
.deco-svgs {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
}
```

---

## Classes existents conservades

Tots els estils existents (`.pbox`, `.pbox-pink`, `.pbox-yellow`, `.pbox-dark`, `.titlebar`, `.hero-content`, `.random-body`, `.endpoints`, `.code-tabs`, `.code-body`, etc.) es mantenen sense modificació.

S'eliminen únicament: `.stats` (el grid de 4 targetes) i `.stat-body` (ja no cal si es fa servir `.stats-row` + `.stat-item`).

---

## Fora d'abast

- Contingut intern dels pboxes (cap canvi a texts, links, lògica Angular)
- Els SVGs decoratius (`.deco-svgs` queda buit, l'usuari els afegirà)
- Cap canvi a `home.ts`
