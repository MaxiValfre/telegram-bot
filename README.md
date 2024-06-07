OfferBot
OfferBot es un bot de Telegram que permite enviar publicaciones con ofertas a un canal de Telegram desde un archivo Excel. El bot lee los datos de un archivo Excel que contiene metadatos sobre productos y envía publicaciones formateadas al canal.

Características
Lee archivos Excel con metadatos sobre productos.
Genera publicaciones con título, precios, enlace al producto e imagen.
Envía las publicaciones a un canal de Telegram.
Requisitos
Python 3.7+
Una cuenta de Telegram
Un bot de Telegram y su token de acceso
Instalación
Clona este repositorio:

sh
Copiar código
git clone https://github.com/tu_usuario/offerbot.git
cd offerbot
Crea y activa un entorno virtual (opcional pero recomendado):

sh
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las dependencias:

sh
Copiar código
pip install -r requirements.txt
Configuración
Crea un bot de Telegram y obtén el token de acceso desde BotFather.

Actualiza las siguientes variables en bot.py con tus datos:

python
Copiar código
TOKEN = 'TU_TOKEN_DE_TELEGRAM'
CHANNEL_ID = 'TU_ID_DEL_CANAL'
CHANNEL_URL = 'TU_URL_DEL_CANAL'
Uso
Inicia el bot:

sh
Copiar código
python bot.py
Envía un archivo Excel al bot a través de Telegram. El archivo Excel debe tener las siguientes columnas:

ProductId: Identificador del producto.
Discount Price: Precio con descuento.
Origin Price: Precio original.
Promotion Url: Enlace de promoción del producto.
Image Url: URL de la imagen del producto.
El bot procesará el archivo y enviará publicaciones formateadas al canal de Telegram especificado.

Ejemplo de archivo Excel
ProductId	Discount Price	Origin Price	Promotion Url	Image Url
Producto1	$10	$20	http://linkproducto1	http://imagenproducto1
Producto2	$15	$25	http://linkproducto2	http://imagenproducto2
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para contribuir al proyecto.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Para cualquier pregunta o consulta, puedes contactar a través de tu correo electrónico.
