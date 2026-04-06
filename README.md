# 📊 Monitor de Cauciones (IOL)

Aplicación en Python que monitorea tasas de cauciones en tiempo real desde IOL y detecta posibles situaciones de estrés de liquidez.

---

## 🧠 Problema

En ciertos días del mercado financiero argentino, puede haber **falta de liquidez en pesos o dólares**, lo que genera **alta volatilidad en las tasas de cauciones**.

Estas situaciones suelen darse en contextos como:

* Fin de mes
* Cierres contables
* Eventos macroeconómicos relevantes
* Cambios en expectativas del mercado

Cuando esto ocurre, las tasas pueden subir rápidamente, reflejando **estrés en el sistema de financiamiento de corto plazo**.

👉 Detectar estos movimientos en tiempo real no siempre es trivial mirando manualmente la página.

Este proyecto surge como una herramienta para:

* Monitorear automáticamente estas tasas
* Identificar condiciones de estrés
* Alertar al usuario de forma inmediata

---

## 🚀 Características

* 🔄 Actualización automática de tasas
* 📈 Monitoreo de cauciones a 1 día y 7 días
* ⚠️ Detección de estrés según umbrales configurables
* 🔔 Alertas visuales y sonoras
* 🖥️ Interfaz gráfica con Tkinter

---

## 🛠️ Tecnologías utilizadas

* Python
* Selenium
* Tkinter
* WebDriver Manager

---

## 📦 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/cauciones-monitor.git
cd cauciones-monitor
```

2. Crear entorno virtual (recomendado):

```bash
python -m venv venv
```

Activar entorno:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / Mac:

```bash
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

Ejecutar la aplicación:

```bash
python main.py
```

---

## ⚙️ Configuración

Podés modificar los umbrales en el archivo `config.py`:

```python
TARGET_ARS = 50.0
TARGET_USD = 1.4
```

---

## ⚠️ Notas

* La aplicación utiliza Selenium en modo headless para obtener los datos.
* Puede tardar unos segundos en iniciar debido a la carga inicial del navegador.
* Depende de la estructura del sitio web, por lo que cambios en la página pueden afectar el funcionamiento.

---

## 📌 Mejoras futuras

* 📊 Gráficos en tiempo real
* 💾 Exportación de datos históricos
* 🔔 Notificaciones del sistema
* ⚡ Optimización del scraping (sin Selenium)

---

## 📄 Licencia

Este proyecto es de uso personal/educativo.
