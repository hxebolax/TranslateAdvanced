* Corregido la devolución de idiomas en configuración.

• 
Ahora siempre devolverá idiomas de código ISO 639-1 en la función obtenerLenguaje del manager de configuración.

* Solucionado Issue #13

• 
Importación del módulo html: Se ha añadido import html para utilizar la función html.unescape(), la cual desescapa todas las entidades HTML, incluidas las numéricas como &#39;.
• 
Eliminación de código innecesario: Se han eliminado los métodos _load_html_entities y unescape, ya que ahora se utiliza html.unescape() en los módulos de Google web.
