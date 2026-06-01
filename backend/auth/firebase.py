"""Seguretat centralitzada amb Firebase Admin SDK.

Tot el codi de verificació viu aquí: s'inicialitza el Firebase Admin SDK
(una sola vegada) i s'exposa la dependència `verify_firebase_token`, que
s'injecta als routers/rutes que requereixen un usuari autenticat.

Credencials (service account de Firebase):
  - FIREBASE_CREDENTIALS         -> JSON complet del service account (recomanat
                                    per a Render i altres entorns sense fitxers).
  - GOOGLE_APPLICATION_CREDENTIALS -> ruta a un fitxer service-account.json.
"""

import json
import os
from pathlib import Path

import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

_bearer = HTTPBearer(auto_error=True)

# Fitxer local de service account (backend/secrets/serviceAccount.json).
# Es fa servir en desenvolupament quan no hi ha variables d'entorn.
_LOCAL_CREDENTIALS = Path(__file__).resolve().parent.parent / "secrets" / "serviceAccount.json"


def _ensure_initialized() -> None:
    """Inicialitza l'app de Firebase Admin una única vegada (lazy).

    Es fa de forma mandrosa perquè el servidor pugui arrencar i servir els
    endpoints públics encara que no hi hagi credencials configurades; només
    fallarà quan es cridi una ruta protegida.
    """
    if firebase_admin._apps:
        return

    raw = os.getenv("FIREBASE_CREDENTIALS")
    if raw:
        cred = credentials.Certificate(json.loads(raw))
        firebase_admin.initialize_app(cred)
    elif os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        firebase_admin.initialize_app(credentials.ApplicationDefault())
    elif _LOCAL_CREDENTIALS.exists():
        firebase_admin.initialize_app(credentials.Certificate(str(_LOCAL_CREDENTIALS)))
    else:
        raise RuntimeError(
            "Falten credencials de Firebase. Defineix FIREBASE_CREDENTIALS "
            "(JSON del service account), GOOGLE_APPLICATION_CREDENTIALS, o posa "
            "el fitxer a backend/secrets/serviceAccount.json."
        )


def verify_firebase_token(
    cred: HTTPAuthorizationCredentials = Depends(_bearer),
) -> dict:
    """Valida l'ID token de Firebase i retorna el token descodificat.

    S'injecta com a dependència a les rutes protegides. El payload retornat
    conté, entre d'altres, `uid` i `email`, disponibles per a la ruta.
    Llança 401 si el token falta, és invàlid o ha caducat.
    """
    _ensure_initialized()
    try:
        return firebase_auth.verify_id_token(cred.credentials)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de Firebase invàlid o caducat",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
