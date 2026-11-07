# Mesa de cartas — versión exportada

Funciona sin Claude y sin créditos: la voz y la lectura corren en el navegador.

## 1. Preparar la carpeta

- **Datos:** en la mesa publicada en Claude, Menú → «Exportar datos e imágenes». Descomprimí `mesa-datos.zip` dentro de `data/` (tiene que quedar `data/mazo.json` y `data/assets/`).
- **Voz (opcional para uso local):** copiá `es_AR-daniela-high.onnx` y `.onnx.json` en `models/`. Si no están, la mesa baja la voz de Hugging Face la primera vez.

## 2. Usarla en tu computadora

Doble clic en «Iniciar mesa (Mac)» o «Iniciar mesa (Windows)». Necesita Python 3 (python.org).
Se abre en `http://localhost:8080`. No sirve abrir `index.html` con doble clic.

## 3. Publicarla en Vercel

Requisitos: Node.js (nodejs.org) y una cuenta de Vercel.

```
npm i -g vercel
cd ruta/a/mesa-export
vercel            # primera vez: responde las preguntas (proyecto nuevo, sin framework)
vercel --prod     # publica en tu dominio .vercel.app
```

- El plan gratis acepta hasta 100 MB por publicación. Esta carpeta con los datos ronda los 60 MB: la voz no se sube (`.vercelignore`) y se descarga de Hugging Face.
- `vercel.json` ya trae los encabezados para que la voz use varios núcleos.
- Para actualizar las cartas: exportá de nuevo los datos, reemplazá `data/` y volvé a correr `vercel --prod`.

## Lectura con IA local (opcional, sin créditos)

Instalá Ollama (ollama.com) y un modelo: `ollama pull qwen2.5:7b`. La mesa lo detecta sola en tu computadora.
En la versión de Vercel solo funciona en tu propia máquina y, además, hay que permitir el dominio:
en Mac `launchctl setenv OLLAMA_ORIGINS "https://TU-PROYECTO.vercel.app"` y reiniciar Ollama
(en Windows, variable de entorno `OLLAMA_ORIGINS`). Sin Ollama, la mesa lee cada carta con su propio texto.

## Créditos

Voz «Daniela» (es_AR, CC BY-SA 4.0): Piper — rhasspy; entrenada por larcanio sobre OpenSLR 61.
