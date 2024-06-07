from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import pandas as pd
import threading
import os

TOKEN = '7186719852:AAGHfrGW2YahSmd2DSh6c5kPGH23OKCGhwA'
CHANNEL_ID = '-4223828233'
CHANNEL_URL = 'YOUR_CHANNEL_URL'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hola! Envía un archivo Excel con los metadatos para crear posts.')

async def handle_file(update: Update, context: CallbackContext):
    file = await context.bot.get_file(update.message.document.file_id)
    file_path = os.path.join('input.xlsx')
    await file.download_to_drive(file_path)
    print(dir(file))
    await update.message.reply_text('Archivo recibido. Procesando...')
    print("Archivo recibido y descargado")

    # Proceso el archivo excel
    await process_excel(update, context, file_path)

async def process_excel(update: Update, context: CallbackContext, file_path: str):
    try:
        # Leer el archivo Excel
        df = pd.read_excel(file_path)
        print(f"Excel leído con éxito: {df}")

        # Recorrer cada fila del DataFrame
        for index, row in df.iterrows():
            # Obtener los datos de interés
            title = row['ProductId']
            price_with_coupon = row['Discount Price']
            price_without_coupon = row['Origin Price']
            product_link = row['Promotion Url']
            image_url = row['Image Url']

            # Construir el mensaje del post
            post_message = f"{title}\n\n" \
                           f"Precio con cupón: {price_with_coupon}\n" \
                           f"Precio sin cupón: {price_without_coupon}\n" \
                           f"Link del producto: {product_link}\n\n" \
                           f"¡Compra ahora!\n\n" \
                           f"Únete a nuestro canal para más ofertas: {CHANNEL_URL}"

            # Enviar la imagen junto con el mensaje
            await context.bot.send_photo(chat_id=CHANNEL_ID, photo=image_url, caption=post_message)
            print("Post enviado:", post_message)

        print("Procesamiento del archivo completado")
    except Exception as e:
        print(f"Error procesando el archivo Excel: {e}")



# Creo la aplicación del bot
application = Application.builder().token(TOKEN).build()

# Añado manejadores de comandos y mensajes
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.Document.MimeType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"), handle_file))

# Inicio el bot
if __name__ == '__main__':
    application.run_polling()










