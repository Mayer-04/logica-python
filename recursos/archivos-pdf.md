# 📄 Herramientas para trabajar con archivos PDF en Python

Este es un resumen claro y accesible de librerías útiles en Python para **leer**, **extraer datos**, **editar** y **manipular documentos PDF**. Cada herramienta tiene sus puntos fuertes, y en muchos casos conviene combinarlas según el tipo de tarea que quieras automatizar o procesar.

> [!NOTE]
> ⭐️ Las cifras de estrellas provienen de GitHub al momento de escribir este artículo (agosto de 2025). Estos números pueden cambiar con el tiempo.

---

## 📌 ¿Cuándo usar cada herramienta?

- Si necesitas **extraer texto o tablas de forma muy precisa** → usa `pdfplumber`.
- Si tu objetivo es **manipular PDFs** **(unir, dividir, proteger, rotar…)** → usa `pypdf`.
- Si buscas una **solución rápida**, **completa** y con múltiples capacidades → usa `PyMuPDF`.

---

### ⚡ `PyMuPDF`

> [!NOTE]
> ⭐️ 7.700 estrellas en Github.

Una biblioteca de **alto rendimiento** para procesamiento completo de documentos PDF y otros formatos.

**Lo que puedes hacer con PyMuPDF:**

- Trabajar con PDF, XPS, EPUB, CBZ, FB2, entre otros formatos.
- Convertir cualquier documento soportado a PDF.
- Extraer texto con estructura (Markdown, HTML, JSON, XML…), imágenes y tablas.
- Leer texto por página completa, regiones específicas o según el orden natural de lectura.
- Insertar o eliminar imágenes, texto, anotaciones y formas vectoriales.
- Leer estructuras internas del PDF (objetos, catálogo, metadatos…).
- Soporte opcional para OCR, capas e información tipográfica

---

### 🐍 `pdfplumber`

> [!NOTE]
> ⭐️ 8.100 estrellas en Github.

Especializada en **extracción precisa de texto y tablas** desde documentos PDF generados digitalmente.

**Principales funcionalidades:**

- Extrae texto con coordenadas y metadatos tipográficos.
- Detecta y extrae tablas visualmente usando líneas y alineación de texto .
- Permite explorar visualmente páginas y depurar en Jupyter.
- Accede a objetos como caracteres, líneas, rectángulos, curvas o imágenes.
- Trabaja con regiones específicas de una página (crop, filter, etc.).
- Ideal para minería de datos en facturas, reportes, recibos, etc.

---

### 📘 `pypdf`

> [!NOTE]
> ⭐️ 9.300 estrellas en Github.

Librería ligera y 100 % Python para **manipular archivos PDF sin dependencias externas**.

**Qué puedes hacer con pypdf:**

- Unir, dividir, rotar y recortar páginas.
- Agregar marcas de agua, sellos o anotaciones sencillas.
- Leer y rellenar formularios (AcroForms).
- Proteger con contraseña o remover protección.
- Extraer texto, metadatos y archivos adjuntos.
- Cambiar opciones de visualización del documento.
- Muy fácil de instalar y usar.

---

## ✅ ¿Cuál es mejor para cada tarea?

| **Tarea**                                         | **PyMuPDF**                 | **pypdf**                    | **pdfplumber**                | **🏆 Mejor opción**      |
| ------------------------------------------------- | --------------------------- | ---------------------------- | ----------------------------- | ------------------------ |
| **Extraer texto (títulos, párrafos…)**            | ✅ Muy completo y eficiente | ⚠️ Limitado básico           | ✅ Muy preciso y estructurado | `PyMuPDF` o `pdfplumber` |
| **Extraer tablas**                                | ✅ Posible (más manual)     | ❌ No                        | ✅ Especialista en tablas     | `pdfplumber`             |
| **Extraer imágenes**                              | ✅ Alta calidad y flexible  | ⚠️ Limitado                  | ⚠️ Poco eficiente             | `PyMuPDF`                |
| **Convertir a Word, Markdown, JSON, XML**         | ✅ Muy versátil             | ❌ No                        | ⚠️ CSV / JSON limitado        | `PyMuPDF`                |
| **Editar contenido (texto, anotaciones…)**        | ✅ Avanzado                 | ⚠️ Básico (sin editar texto) | ❌ No                         | `PyMuPDF`                |
| **Eliminar elementos (texto, imágenes, dibujos)** | ✅ Soporta borrado          | ⚠️ Sólo páginas completas    | ❌ No                         | `PyMuPDF`                |
| **Agregar texto, imágenes o anotaciones**         | ✅ Muy flexible             | ✅ Básico                    | ❌ No                         | `PyMuPDF`                |
| **Unir múltiples PDFs**                           | ✅ Sí                       | ✅ Muy fácil y especializado | ❌ No                         | `pypdf`                  |
| **Encriptar / desencriptar PDFs**                 | ✅ Sí                       | ✅ Sí                        | ❌ No                         | `PyMuPDF` o `pypdf`      |

## Consejos prácticos

En muchos casos, la mejor solución es combinar varias librerías:

- Usa **pdfplumber** para extraer tablas o texto con estructura.
- Usa **pypdf** o **PyMuPDF** para unir documentos, editar o protegerlos una vez que tienes los datos extraídos.

Esto te permite aprovechar las fortalezas de cada herramienta según la fase del flujo de trabajo.

## 📚 Recursos Oficiales

- [pdfplumber en GitHub](https://github.com/jsvine/pdfplumber)
- [pypdf en GitHub](https://github.com/py-pdf/pypdf)
- [PyMuPDF en GitHub](https://github.com/pymupdf/PyMuPDF)
