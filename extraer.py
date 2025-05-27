import requests
from bs4 import BeautifulSoup

# URL del artículo
url = "https://www.infobae.com/politica/2025/05/27/aumentaron-a-34-las-muertes-por-el-fentanilo-contaminado-elaborado-por-el-laboratorio-hlb-pharma/"

# Hacer la solicitud
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# Parsear el HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extraer el título
titulo = soup.find("h1")
titulo = titulo.get_text(strip=True) if titulo else "Título no disponible"

# Extraer el autor
autor_meta = soup.find("meta", attrs={"name": "author"})
autor = autor_meta["content"].strip() if autor_meta else "Autor no disponible"

# Extraer la fecha
fecha_meta = soup.find("meta", attrs={"property": "article:published_time"})
fecha = fecha_meta["content"][:10] if fecha_meta else "Fecha no disponible"

# Extraer el contenido del artículo (párrafos dentro del <article>)
contenido = ""
article = soup.find("article")
if article:
    for p in article.find_all("p"):
        texto = p.get_text(strip=True)
        if texto:
            contenido += texto + "\n"
else:
    contenido = "Contenido no disponible"

# Mostrar resultados
print(f"Título: {titulo}")
print(f"Autor: {autor}")
print(f"Fecha de publicación: {fecha}")
print(f"\nContenido:\n{contenido}")
