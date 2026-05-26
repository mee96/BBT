categorias = [
    {"categoria_id": 1, "nombre": "Té con Leche",  "nombre_zh": "奶茶"},
    {"categoria_id": 2, "nombre": "Leche Fresca",  "nombre_zh": "鲜奶"},
    {"categoria_id": 3, "nombre": "Frutal",        "nombre_zh": "果茶"},
    {"categoria_id": 4, "nombre": "Probiótico",    "nombre_zh": "养乐多"},
    {"categoria_id": 5, "nombre": "Frappé",        "nombre_zh": "冰沙"},
    {"categoria_id": 6, "nombre": "Especiales",    "nombre_zh": "特调"},
    {"categoria_id": 7, "nombre": "Té",            "nombre_zh": "茶"},
]

tamanos = [
    {"tamano_id": 1, "codigo": "M", "nombre": "Mediano"},
    {"tamano_id": 2, "codigo": "L", "nombre": "Grande"},
]

toppings = [
    {"topping_id": 1, "nombre": "Perlas de Tapioca",               "precio_extra": 0.50},
    {"topping_id": 2, "nombre": "Gelatina de Hierba Aromática",    "precio_extra": 0.50},
    {"topping_id": 3, "nombre": "Pudding",                         "precio_extra": 0.50},
    {"topping_id": 4, "nombre": "Gelatina de Coco",                "precio_extra": 0.80},
    {"topping_id": 5, "nombre": "Perlas de Tapioca Azúcar Moreno", "precio_extra": 0.80},
    {"topping_id": 6, "nombre": "Perlas Popping - Fresa",          "precio_extra": 0.80},
    {"topping_id": 7, "nombre": "Perlas Popping - Lichi",          "precio_extra": 0.80},
    {"topping_id": 8, "nombre": "Nube Crema de Leche",             "precio_extra": 1.00},
]

alergenos = [
    {"alergeno_id": 1, "nombre": "Lácteo"},
    {"alergeno_id": 2, "nombre": "Gluten"},
    {"alergeno_id": 3, "nombre": "Soja"},
    {"alergeno_id": 4, "nombre": "Frutos secos"},
    {"alergeno_id": 5, "nombre": "Cafeína"},
]

bebidas = [
    # --- Té con Leche ---
    {
        "bubbletea_id": 1, "nombre": "Té con Leche Clásico",
        "tipo_bubbletea": "Té con Leche", "descripcion": "Clásico té negro con leche",
        "categoria_id": 1, "disponible_caliente": True,
        "es_vegano": False, "tiene_cafeina": True,
        "precio_M": 4.50, "precio_L": None,
        "alergenos": ["Lácteo", "Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 2, "nombre": "Té con Leche y Jazmín",
        "tipo_bubbletea": "Té con Leche", "descripcion": "Té de jazmín con leche",
        "categoria_id": 1, "disponible_caliente": True,
        "es_vegano": False, "tiene_cafeina": True,
        "precio_M": 4.50, "precio_L": None,
        "alergenos": ["Lácteo", "Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 3, "nombre": "Leche sabor a Taro",
        "tipo_bubbletea": "Té con Leche", "descripcion": "Bebida cremosa de taro con leche",
        "categoria_id": 1, "disponible_caliente": False,
        "es_vegano": False, "tiene_cafeina": False,
        "precio_M": 4.50, "precio_L": None,
        "alergenos": ["Lácteo"], "activo": True,     
    },
    # --- Leche Fresca ---
    {
        "bubbletea_id": 4, "nombre": "3 Hermanos con Leche Fresca",
        "tipo_bubbletea": "Leche Fresca", "descripcion": "Tapioca, Pudding y Gelatina con leche fresca",
        "categoria_id": 2, "disponible_caliente": False,
        "es_vegano": False, "tiene_cafeina": False,
        "precio_M": 6.00, "precio_L": None,
        "alergenos": ["Lácteo"], "activo": True,
    },
    # --- Frutal ---
    {
        "bubbletea_id": 5, "nombre": "Té Verde con Sabor a Mango",
        "tipo_bubbletea": "Frutal", "descripcion": "Té verde con sirope de mango",
        "categoria_id": 3, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 5.00, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 6, "nombre": "Té Negro con Sabor a Maracuyá",
        "tipo_bubbletea": "Frutal", "descripcion": "Té negro con maracuyá",
        "categoria_id": 3, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 5.00, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 7, "nombre": "Té Verde con Zumo de Limón Natural",
        "tipo_bubbletea": "Frutal", "descripcion": "Té verde con zumo de limón exprimido",
        "categoria_id": 3, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 5.00, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 8, "nombre": "Rey del Limón",
        "tipo_bubbletea": "Frutal", "descripcion": "Té verde con un limón entero",
        "categoria_id": 3, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 5.90, "precio_L": 5.90,
        "alergenos": ["Cafeína"], "activo": True,
    },
    # --- Probiótico ---
    {
        "bubbletea_id": 9, "nombre": "Té Verde con Yakult",
        "tipo_bubbletea": "Probiótico", "descripcion": "Té verde con Yakult",
        "categoria_id": 4, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 5.90, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 10, "nombre": "Mango Yakult",
        "tipo_bubbletea": "Probiótico", "descripcion": "Mango con Yakult",
        "categoria_id": 4, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": False,
        "precio_M": 5.90, "precio_L": None,
        "alergenos": [], "activo": True,             
    },
    {
        "bubbletea_id": 11, "nombre": "Zumo de Limón Natural con Yakult",
        "tipo_bubbletea": "Probiótico", "descripcion": "Limón natural con Yakult",
        "categoria_id": 4, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": False,
        "precio_M": 5.90, "precio_L": None,
        "alergenos": [], "activo": True,
    },
    # --- Frappé ---
    {
        "bubbletea_id": 12, "nombre": "Frappé de Taro",
        "tipo_bubbletea": "Frappé", "descripcion": "Frappé cremoso de taro",
        "categoria_id": 5, "disponible_caliente": False,
        "es_vegano": False, "tiene_cafeina": False,
        "precio_M": 5.50, "precio_L": None,
        "alergenos": ["Lácteo"], "activo": True,
    },
    {
        "bubbletea_id": 13, "nombre": "Frappé de Mango y Maracuyá",
        "tipo_bubbletea": "Frappé", "descripcion": "Frappé de mango con maracuyá",
        "categoria_id": 5, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": False,
        "precio_M": 5.50, "precio_L": None,
        "alergenos": [], "activo": True,
    },
    # --- Especiales ---
    {
        "bubbletea_id": 14, "nombre": "Popping Marte",
        "tipo_bubbletea": "Especial", "descripcion": "Té verde de mango con perlas popping de fresa",
        "categoria_id": 6, "disponible_caliente": False,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 5.50, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 15, "nombre": "Piruleta de Fresa",
        "tipo_bubbletea": "Especial", "descripcion": "Té verde con leche y perlas popping de fresa",
        "categoria_id": 6, "disponible_caliente": False,
        "es_vegano": False, "tiene_cafeina": True,
        "precio_M": None, "precio_L": 6.00,
        "alergenos": ["Lácteo", "Cafeína"], "activo": True,  
    },
    # --- Té ---
    {
        "bubbletea_id": 16, "nombre": "Té Negro",
        "tipo_bubbletea": "Té", "descripcion": "Té negro solo",
        "categoria_id": 7, "disponible_caliente": True,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 3.90, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
    {
        "bubbletea_id": 17, "nombre": "Té Verde",
        "tipo_bubbletea": "Té", "descripcion": "Té verde solo",
        "categoria_id": 7, "disponible_caliente": True,
        "es_vegano": True, "tiene_cafeina": True,
        "precio_M": 3.90, "precio_L": None,
        "alergenos": ["Cafeína"], "activo": True,
    },
]

usuarios = [
    {
        "usuario_id": 1, "nombre": "Ana García",
        "nombre_usuario": "anagarcia", "email": "ana@email.com",
        "pais": "España", "ciudad": "Barcelona",
    },
    {
        "usuario_id": 2, "nombre": "Marc Puig",
        "nombre_usuario": "marcpuig", "email": "marc@email.com",
        "pais": "España", "ciudad": "Madrid",
    },
]

pedidos = [
    {
        "pedido_id": 1, "usuario_id": 1,
        "fecha_pedido": "2025-05-22 10:30:00",
        "estado": "PENDIENTE", "precio_total": 14.00,
        "lineas": [
            {
                "bubbletea_id": 1, "nombre_bebida": "Té con Leche Clásico",
                "tamano": "M", "cantidad": 2,
                "nivel_azucar": "Regular", "nivel_hielo": "Regular",
                "precio_unidad": 4.50, "toppings": ["Perlas de Tapioca"],
            },
            {
                "bubbletea_id": 5, "nombre_bebida": "Té Verde con Sabor a Mango",
                "tamano": "M", "cantidad": 1,
                "nivel_azucar": "70%", "nivel_hielo": "Poco",
                "precio_unidad": 5.00, "toppings": ["Perlas Popping - Fresa"],
            },
        ],
    },
    {
        "pedido_id": 2, "usuario_id": 2,
        "fecha_pedido": "2025-05-22 11:15:00",
        "estado": "ENVIADO", "precio_total": 11.40,
        "lineas": [
            {
                "bubbletea_id": 8, "nombre_bebida": "Rey del Limón",
                "tamano": "L", "cantidad": 1,
                "nivel_azucar": "50%", "nivel_hielo": "Extra",
                "precio_unidad": 5.90, "toppings": [],
            },
            {
                "bubbletea_id": 13, "nombre_bebida": "Frappé de Mango y Maracuyá",
                "tamano": "M", "cantidad": 1,
                "nivel_azucar": "Regular", "nivel_hielo": "Regular",
                "precio_unidad": 5.50, "toppings": ["Gelatina de Coco"],
            },
        ],
    },
]
