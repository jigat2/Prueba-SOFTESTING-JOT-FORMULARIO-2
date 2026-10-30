# Automatizacion

Prueba practica de automatizacion.

# Información del aspirante

- **Nombre:** Jacobo Ordoñez
- **Prueba:** Softesting – automatización de formulario web
- **Repositorio:** <https://github.com/jigat2/Prueba-SOFTESTING-JOT-FORMULARIO-2>

# Herramientas

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje |
| Selenium WebDriver | Automatización del navegador |
| Google Chrome + ChromeDriver | Navegador (Selenium Manager configura el driver automáticamente) |
| VS Code | Editor |
| Git / GitHub | Control de versiones |

## Gestor de dependencias y librerías

- **Gestor:** `pip` (con entorno virtual `venv`)
- **Librerías:**
  - `selenium` (`webdriver`, `By`, `Keys`, `WebDriverWait`, `expected_conditions`)
  - Librerías estándar de Python: `os`, `time`, `datetime`

Instalación en PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install selenium
```

## Estructura

```
Softesting/
├── main.py       # Script que automatiza el formulario
├── Entrada.py    # Datos de entrada para el formulario
└── README.md
```

## Ejecución

Desde la carpeta del proyecto, con el entorno virtual activo:

```powershell
python main.py
```

El robot abre Chrome, accede al formulario de [QA Practice](https://qa-practice.netlify.app/bugs-form), completa nombre, apellido, teléfono, país, correo y contraseña, y envía el formulario. Después de esperar unos segundos, cierra el navegador.

# Configuración de datos

Edita `Entrada.py` para cambiar los valores:

```python
NAME = "..."
LASTNAME = "..."
EMAIL = "..."
MOBILE = "..."
COUNTRY = "..."
PASSWORD = "..."
```


