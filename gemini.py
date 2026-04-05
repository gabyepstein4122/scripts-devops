import google.generativeai as genai

genai.configure(api_key="AIzaSyAPaqaP6iamFENHuxEy8blMdG-m5X6RR_g")

# --- CODIGO GUARDADO PARA CONSULTAR MODELOS ---
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
# ----------------------------------------------

model = genai.GenerativeModel('gemini-2.0-flash')
print("Autenticacion exitosa")
chat = model.start_chat()

print("Hola! soy Gemini, como te puedo ayudar? (salir para cerrar)")

while True:
        pregunta = input('>')
        if pregunta.lower() == 'salir':
                break
        respuesta = chat.send_message(pregunta)
        print("Gemini:", respuesta.text)
