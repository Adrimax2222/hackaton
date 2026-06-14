# Asteroid Belt Run

Juego educativo interactivo desarrollado para la **Hackathon Hack the Future 2026**, organizada por DEQ4Future, powered by Codelearn y con la colaboración del Ajuntament de Sabadell.

Proyecto realizado por **Adrià Navarro y Aleix Pascual.**

---

## La historia

Joel González, astronauta de la flota intergaláctica de Núrbor, se ha quedado atrapado en un cinturón de asteroides. Para escapar necesita tu ayuda: responde preguntas sobre la Tierra y guíalo a través de los 6 asteroides del cinturón. Pero ten cuidado — cada error destruye un propulsor, y si pierdes los tres, la nave queda inservible.

---

## Sobre la Hackathon

Este proyecto fue desarrollado el **13 de junio de 2026** durante la jornada intensiva **Hack the Future**, celebrada en el Centre Cívic de la Creu Alta - Cal Balsach, Sabadell.

El reto: diseñar y construir en un solo día un juego educativo funcional enfocado en **accesibilidad e inclusión**, incorporando herramientas que faciliten la comunicación a personas con necesidades diversas.

**Organiza:** DEQ4Future  
**Powered by:** Codelearn  
**Col·labora:** Ajuntament de Sabadell  

---

## Características del juego

- Narrativa espacial con introducción cinematográfica de texto en movimiento
- Tablero con 6 asteroides desbloqueables en orden
- Quiz de 6 preguntas sobre ciencia y astronomía
- Sistema de 3 vidas representado con la nave de Joel (nave.png → nave2 → nave1 → nave0)
- Pantalla de game over y pantalla de victoria personalizada
- Música ambiental en bucle

### Accesibilidad incluida

- **Leer en Voz Alta** — narración de todos los textos en audio sincronizada con la animación visual. El texto nunca desaparece antes de que termine el audio
- **Filtro de daltonismo** — ajuste de color para personas con dificultades en la percepción del color
- **Control de música** — activar o desactivar la música de ambiente
- Todas las preferencias se guardan entre pantallas mediante localStorage

---

## Tecnologías usadas

- HTML5
- CSS3
- JavaScript (vanilla, sin librerías externas)

Sin frameworks. Sin dependencias. Código básico y accesible.

> El proyecto incluye un archivo `app.py` de Flask creado durante el desarrollo inicial, pero el juego final funciona completamente en el navegador mediante Live Server, sin necesidad de servidor Python.

---

## Estructura del proyecto

```
HACKATON/
  static/
    media/
      lectura/
        game_over.mp3
        inicio.mp3
        intro_1.mp3
        intro_2.mp3
        jugar.mp3
        llegaste.mp3
        motor.mp3
        normas.mp3
        pregunta_1.mp3
        pregunta_2.mp3
        pregunta_3.mp3
        pregunta_4.mp3
        pregunta_5.mp3
        pregunta_6.mp3
      ambiente.mp3
      click.mp3
      fondo.png
      gameover.png
      intro.png
      llegaste.png
      nave.png
      nave0.png
      nave1.png
      nave2.png
      tablero.png
    intro.css
    style.css
    tablero.css
  templates/
    intro.html        ← introducción animada
    juego.html        ← menú principal y accesibilidad
    tablero.html      ← tablero de juego y quizzes
  app.py
```

---

## Cómo ejecutar

1. Abre `templates/juego.html` con **Live Server** en VS Code
2. Configura tus opciones de accesibilidad en el menú
3. Pulsa **Empezar Misión** y ayuda a Joel a escapar

No se necesita servidor ni instalación adicional.

---

## Licencia

Este proyecto se publica bajo la licencia **MIT**, tal como establecen las bases de la Hackathon Hack the Future 2026.

Puedes usar, copiar, modificar y compartir este proyecto libremente, siempre que se mencione a los creadores originales.

---

*Desarrollado con HTML, CSS y JavaScript durante la Hackathon Hack the Future 2026 — Sabadell.*
