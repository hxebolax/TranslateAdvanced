# Manual del Usuario: Traductor Avanzado para NVDA

<h2 id="indice">Índice</h2>

- [1 - Introducción](#introduccion)
  - [1.1 - Requisitos](#requisitos)
  - [1.2 - Limitaciones y advertencias](#limitaciones-y-advertencias)
  - [1.3 - Información del autor](#informacion-autor)
- [2 - Descripción y configuración](#descripcion-configuracion)
  - [2.1 - Descripción de servicios](#descripcion-servicios)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Translate](#microsoft-translate)
  - [2.2 - Configuración](#configuracion)
    - [Menú del complemento](#menu-del-complemento)
    - [Teclas rápidas del complemento](#teclas-rapidas-del-complemento)
- [3 - Solución de Problemas](#solucion-de-problemas)
  - [Problemas Comunes y Soluciones](#problemas-comunes-y-soluciones)
  - [Cómo Consultar el Log de NVDA](#como-consultar-el-log-de-nvda)
- [4 - Agradecimientos](#agradecimientos)
  - [Traductores](#traductores)
- [5 - Registro de Versiones](#registro-de-versiones)
  - [Versión 2024.06.06](#version-2024-06-06)
  - [Versión 2024.06.16](#version-2024-06-16)

<h2 id="introduccion">1 - Introducción</h2>

El **Traductor Avanzado para NVDA** es un complemento que permite traducir textos utilizando diversos servicios de traducción en línea, como Google Translate, DeepL, LibreTranslate y Microsoft Translator. Este complemento ofrece funcionalidades avanzadas como traducción simultánea, historial de traducciones, traducción de lo seleccionado, soporte para múltiples lenguajes y más.

[Volver al índice](#indice)

<h3 id="requisitos">1.1 - Requisitos</h3>

- NVDA (NonVisual Desktop Access) 2024.1 o superior
- Conexión a Internet

[Volver al índice](#indice)

<h3 id="limitaciones-y-advertencias">1.2 - Limitaciones y advertencias</h3>

El complemento envía información a Internet a cada servicio correspondiente para realizar la traducción simultánea. Es importante tener en cuenta que la información que se está traduciendo puede incluir datos confidenciales y sensibles. El uso del complemento es responsabilidad exclusiva del usuario, quien debe evaluar la naturaleza de la información que se envía. El desarrollador del complemento no asume ninguna responsabilidad por los datos enviados a los servicios que el complemento utiliza.

Como desarrollador, declino toda responsabilidad por cualquier eventualidad que pueda surgir del uso del complemento. La responsabilidad completa recae en el usuario.

Además, el complemento requiere una conexión a Internet para su funcionamiento. La velocidad de respuesta del complemento depende de varios factores, tales como:
- La calidad de nuestra conexión a Internet.
- El posible retraso (lag) de los servicios de traducción utilizados.
- Factores relacionados con la infraestructura de red del usuario.

Es recomendable que los usuarios sean conscientes de estos aspectos y realicen las pruebas necesarias para asegurar que el complemento cumple con sus expectativas y requisitos de seguridad.

[Volver al índice](#indice)

<h3 id="informacion-autor">1.3 - Información del autor</h3>

**Información Técnica y Medidas de Seguridad del Complemento para NVDA**

He trabajado arduamente para hacer el complemento lo más robusto posible, contemplando y manejando cualquier error potencial. Todos los errores son capturados y registrados en el log de NVDA, lo que facilita el seguimiento y la rápida resolución de inconvenientes.

**Problemas con Certificados de Windows**

Recientemente, he observado que los ordenadores recién instalados con Windows pueden presentar problemas con los certificados, lo cual puede ser frustrante. Por esta razón, he incorporado una comprobación al inicio del complemento. Si se detecta un fallo relacionado con los certificados, el complemento se encargará de regenerarlos automáticamente, asegurando un funcionamiento correcto tanto de Windows como del propio complemento.

**Medidas de Seguridad**

El complemento incluye varias medidas de seguridad:
- No se permite su ejecución en pantallas seguras.
- No se inicia si no se detecta una conexión a Internet.

En ocasiones, NVDA puede iniciarse más rápido que la conexión a la red Wi-Fi. En tales casos, será necesario reiniciar NVDA una vez establecida la conexión para poder utilizar el complemento correctamente.

**Gestión de Claves API**

El complemento genera un archivo JSON que almacena las claves API necesarias para aquellos servicios que las requieren. Este archivo, llamado `apis.json`, se aloja en la carpeta de usuario de Windows.

**Consideraciones sobre el Archivo de Claves**

Se ha decidido almacenar este archivo fuera del entorno del complemento para evitar que, al contener información sensible, pueda ser compartido inadvertidamente con una copia portátil de NVDA o en otras situaciones. Si el usuario decide dejar de utilizar el complemento, deberá eliminar manualmente este archivo.

Estas medidas aseguran una mejor gestión y seguridad del complemento, facilitando su uso y mantenimiento.

[Volver al índice](#indice)

<h2 id="descripcion-configuracion">2 - Descripción y configuración</h2>

<h3 id="descripcion-servicios">2.1 - Descripción de servicios</h3>

En su primera versión, el complemento ofrece 7 servicios de traducción:

<h4 id="google">Google</h4>

**4 Servicios de Google**

- **2 Servicios de raspado web:** Cada servicio realiza la misma función, pero de manera diferente, asegurando que siempre haya una alternativa disponible en caso de fallo de uno de ellos.
- **2 Servicios a través de API:** Estos servicios también son ilimitados y gratuitos, pero el abuso de los mismos puede resultar en un baneo temporal de la IP durante unas horas, después de las cuales el servicio se reestablecerá.
- Todos estos servicios de Google no requieren claves API y son ilimitados y gratuitos.

<h4 id="deepl">DeepL</h4>

**2 Servicios de DeepL**

- **API Free:** Esta opción requiere obtener una clave API Free desde la página de DeepL, la cual ofrece 500,000 caracteres al mes.
- **API Pro:** Esta opción también requiere una clave API obtenida desde la página web de DeepL. Su uso está condicionado al saldo y al plan contratado en la cuenta de DeepL del usuario.
- Las condiciones de uso de la API de DeepL se encuentran en su [página web](https://www.deepl.com/es/pro/change-plan#developer), y el complemento está limitado por dichas condiciones.

<h4 id="libretranslate">LibreTranslate</h4>

**1 Servicio de LibreTranslate**

- Este servicio mejora constantemente gracias a su aprendizaje neuronal continuo. Aunque actualmente no alcanza la calidad de Google, es perfectamente utilizable.
- Basado en la tecnología de Argos Translate.
- Para usar este servicio se requiere una clave API, la cual se puede obtener realizando una donación a la comunidad [NVDA.es](https://nvda.es/donaciones/).
  - Tras donar, se puede solicitar la clave API utilizando el formulario de la siguiente [página](https://nvda.es/contacto/), indicando en el asunto "solicitud de clave API" y proporcionando la referencia de PayPal, transferencia, etc.
- Además, es posible configurar otros servicios de LibreTranslate añadiendo la clave API y modificando la URL del servicio en la sección de configuración del complemento.

<h4 id="microsoft-translate">Microsoft Translate</h4>

**1 Servicio de Microsoft Translate**

- Este servicio tiene la limitación de que el uso continuo puede resultar en un baneo temporal de la IP durante unos minutos.
- Este baneo ocurre únicamente con un uso muy intensivo y en traducciones de textos largos.
- El servicio funciona muy bien, pero se recomienda no usarlo de manera continua para evitar interrupciones.

Estas opciones permiten a los usuarios elegir entre varios servicios de traducción, asegurando la disponibilidad y la flexibilidad del complemento según las necesidades y preferencias individuales.

Conforme el complemento reciba actualizaciones, pueden añadirse o eliminarse servicios. Se informará de los cambios en la sección de actualizaciones.

[Volver al índice](#indice)

<h3 id="configuracion">2.2 - Configuración</h3>

**Configuración del Complemento**

En esta sección, se detalla cómo configurar cada uno de los servicios disponibles en el complemento, incluyendo cómo agregar claves API, modificar URL de servicios y otros ajustes necesarios para personalizar el uso del complemento según las necesidades del usuario.

<h4 id="menu-del-complemento">Menú del complemento</h4>

En NVDA > Preferencias > Traductor Avanzado tenemos un menú que contiene lo siguiente:

- **Configuración de Traductor Avanzado**

  Si pulsamos esta opción se abrirá la ventana de configuración del complemento. Dicha ventana tiene 2 áreas:

  - **General**

    En esta pestaña se agregarán aquellas opciones de carácter general del complemento. Actualmente, solo tiene una casilla de verificación para activar o desactivar la caché del complemento.

    El complemento puede guardar una caché de aquellas traducciones para cada aplicación, lo que facilitará la traducción y será más rápido en futuras traducciones. Además, ahora crea caché para cada idioma, pudiendo haber más de una aplicación que tenga caché para distintos idiomas.

  - **Módulos de traducción**

    En esta pestaña podremos elegir el servicio que deseamos usar para traducir. En aquellos servicios que requieran de clave API, se mostrará también el gestor de claves API.

    Podemos tener más de una clave API para un mismo servicio; por ejemplo, en LibreTranslate podemos tener distintas claves y URLs para conectarnos. Podremos añadir, editar, eliminar y poner por defecto la clave API que deseamos para el servicio actual.

    El área de gestión de claves API cambia según el servicio que tengamos. Podemos poner un nombre identificativo a cada clave API para saber rápidamente a qué API nos referimos. Cuando tengamos más de una clave API para un servicio, el item que en la lista tenga un asterisco será el que esté por defecto. Esto se puede cambiar con el botón "Por defecto", pasando a ser la definida para dicho servicio la clave que tengamos enfocada en ese momento.

    Si el servicio de traducción que elijamos no requiere clave API, el gestor no se mostrará.

    Luego tenemos el botón "Aceptar" y "Cancelar". Todas las opciones tienen su tecla de atajo que nos informará NVDA.

- **Documentación del complemento**

  Si pulsamos "Documentación del complemento" se abrirá esta documentación.

- **Invítame a un café si te gusta mi trabajo**

  Si pulsamos esta opción, se abrirá la página de PayPal donde hay un enlace que dice "Enviar". Si pulsamos dicho enlace, nos pedirá que iniciemos sesión en nuestra cuenta y nos dejará en la página de donaciones.

  Solo diré que me he tomado muchos cafés haciendo este complemento.

[Volver al índice](#indice)

<h4 id="teclas-rapidas-del-complemento">Teclas rápidas del complemento</h4>

En NVDA > Preferencias > Gestos de entrada... > Traductor Avanzado tenemos las siguientes teclas que podremos configurar.

Las teclas por defecto vienen sin asignar para que sea el usuario quien elija su mejor distribución. Son las siguientes:

- **Abre la configuración del complemento**

  Este acceso nos abrirá rápidamente la configuración del complemento.

- **Activa o desactiva la caché de traducción**

  Este acceso activará o desactivará la caché sin necesidad de entrar a la configuración.

- **Activa o desactiva la traducción simultánea Online**

  Este acceso activa o desactiva la traducción. Es el acceso principal que nos empezará a traducir conforme nos movamos con las flechas de cursor. Si todo está correcto, oiremos la traducción; en caso de oír el texto original, tendremos que mirar el log de NVDA y ver qué ha sucedido.

- **Cambiar el módulo de traducción**

  Este acceso nos abrirá una ventana con todos los servicios de traducción disponibles. Podremos movernos con las flechas y seleccionar con "Intro". El servicio que seleccionemos será el que tengamos por defecto.

- **Cambiar idioma de destino**

  Este acceso nos abrirá una ventana con los idiomas de destino disponibles en el servicio que tengamos seleccionado. Cada servicio tiene unos idiomas y, por ejemplo, si estamos traduciendo un texto que está en ruso y queremos oírlo en inglés, en este diálogo tendremos que seleccionar inglés. Nos movemos por el diálogo con flechas de cursor y "Intro" para seleccionar el idioma que deseamos.

  Los nombres de los idiomas se obtienen en nuestro lenguaje desde NVDA, admitiendo aquellos que NVDA soporta. Por eso, en la lista pueden aparecer nombres de idiomas que están en inglés, ya que NVDA no los tiene traducidos. Se agrega al lado de cada nombre de idioma el código ISO del idioma.

- **Cambiar idioma de origen**

  Lo mismo que el anterior, pero este diálogo solo es válido para el traductor de Microsoft. El servicio de Microsoft no permite poner el idioma de origen como auto para que detecte qué idioma se le envía, por lo que tendremos que elegirlo nosotros.

  El resto de los servicios no podrá usar este diálogo ya que su opción por defecto de origen es detectar qué idioma se está enviando.

- **Copiar el último texto traducido al portapapeles**

  Este acceso nos copiará al portapapeles el último texto que haya sido traducido.

- **Eliminar la caché de traducción para la aplicación enfocada actualmente**

  Si pulsamos este acceso una vez, nos dará información; si lo pulsamos dos veces rápidamente, borrará la caché para la aplicación que en ese momento tenga el foco y nos informará del resultado.

- **Eliminar todas las traducciones en caché para todas las aplicaciones**

  Este acceso, pulsado una vez, nos dará información; pulsado dos veces rápidamente, borrará toda la caché del complemento ofreciendo también información.

- **Muestra el historial de traducción**

  Mostrará un diálogo con las últimas 500 traducciones en una lista. Podremos buscar y revisar en cuadros de solo lectura el texto origen y el texto traducido. Este diálogo nos permitirá buscar en todo el historial, copiar al portapapeles tanto el texto origen como el texto traducido o ambos.

  También permite alternar entre texto origen y texto traducido y trabajar con cualquiera de las dos maneras. Además, podremos borrar todo el historial para empezar desde cero.

  Advierto que el historial se borra cada vez que NVDA se reinicia.

- **Traduce el texto seleccionado**

  Esta acción traducirá el texto que tengamos seleccionado y enfocado. Si es un texto grande, nos abrirá un diálogo con el porcentaje de la traducción. Dicho diálogo puede ser cancelado, lo que también cancelará la traducción.

  Una vez la traducción se complete, el texto será mostrado en un diálogo para que podamos explorarlo.

  Esta opción usa el servicio de Google Translate y no puede ser cambiado dicho servicio, siendo elegido internamente ya que es el que mejor resultados da para textos largos.

[Volver al índice](#indice)

<h2 id="solucion-de-problemas">3 - Solución de Problemas</h2>

<h3 id="problemas-comunes-y-soluciones">Problemas Comunes y Soluciones</h3>

**Conexión a Internet**
- Verifique que su conexión a Internet esté activa y funcionando correctamente.
- Reinicie su enrutador o módem si es necesario.

**Errores de Certificados**
- Si experimenta errores de certificados, asegúrese de que la fecha y hora de su sistema estén correctas.
- Verifique que los certificados necesarios estén instalados y actualizados.

**Problemas de Rendimiento**
- Asegúrese de que su equipo cumple con los requisitos mínimos del sistema.
- Cierre otras aplicaciones que puedan estar consumiendo muchos recursos.

[Volver al índice](#indice)

<h3 id="como-consultar-el-log-de-nvda">Cómo Consultar el Log de NVDA</h3>

1. Abra NVDA.
2. Vaya a `NVDA > Herramientas > Ver registro`.
3. En la ventana del registro, busque cualquier error o mensaje relacionado con el Traductor Avanzado.

[Volver al índice](#indice)

<h2 id="agradecimientos">4 - Agradecimientos</h2>

Agradecer a todos los programadores de NVDA por su excelente trabajo.

Y no quiero dejar de decir que el principio de este complemento es el complemento de Yannick PLASSIARD (TRANSLATE), del cual e aprendido y e usado alguna función.

También a Alexy Sadovoy aka Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino, and other NVDA contributors también por el complemento (Instant Translate) del cual se obtuvo uno de los métodos para Google y fue modificado para implementarlo en Traductor Avanzado.

Este complemento es el trabajo de varios años sacando versiones no oficiales y el estudio de usar traducciones sin conexión.

El aprendizaje es el resultado de este complemento teniendo en claro que a futuro traerá novedades sorprendentes.

[Volver al índice](#indice)

<h3 id="traductores">Traductores</h3>

- **Portugués:** Ângelo Abrantes.
- **Turco:** Umut Korkmaz.
- **Ruso:** Valentin Kupriyanov.
- **Inglés:** Samuel Proulx.
- **Ucraniano:** Heorhii Halas y Volodymyr Pyrih.

[Volver al índice](#indice)

<h2 id="registro-de-versiones">5 - Registro de Versiones</h2>

En este apartado se añadira un registro de versiones, donde se iran poniendo las novedades de cada versión.

El manual esta basado en la primera versión por lo que no se actualizara sirviendo como base.

Las novedades se agregarán en esta sección.

[Volver al índice](#indice)

<h3 id="version-2024-06-06">Versión 2024.06.06</h3>

- Lanzamiento inicial del complemento.
- Soporte para 7 servicios de traducción.
- Funcionalidades básicas de traducción simultánea y gestión de claves API.

[Volver al índice](#indice)

<h3 id="version-2024-06-16">Versión 2024.06.16</h3>

- **Agregar el poder copiar al portapapeles lo traducido por selección en vez de mostrarlo en diálogo:**

Se ha añadido una opción para copiar automáticamente al portapapeles el texto traducido cuando se selecciona esta función, evitando la necesidad de mostrar un cuadro de diálogo adicional.

Dicha opción se añadió en el dialogo de configuración del complemento en General.

Si dicha opción se marca ya no mostrara cuando traduzcamos un texto seleccionado un dialogo si no que directamente lo copiara al portapapeles.

- **Traducir lo que haya en el portapapeles:**

Ahora es posible traducir directamente el contenido que se encuentra en el portapapeles, proporcionando una manera rápida y eficiente de traducir textos copiados.

Si no se traduce nada nos dirá que hay en el portapapeles o si no hay nada en el portapapeles nos notificara con un mensaje.

- **Traducir lo último verbalizado por el sintetizador:**

Se ha incorporado una funcionalidad que permite traducir la última frase o texto verbalizado por el sintetizador de voz, mejorando la accesibilidad y usabilidad del complemento.

Si no se puede traducir lo ultimo verbalizado nos dirá lo ultimo que se verbalizo en el idioma origen.

- **Mostrar traducciones en líneas braille:**

La nueva versión incluye soporte para mostrar las traducciones en dispositivos de línea braille, facilitando el acceso a las traducciones.

Solo funcionara en aquellos equipos que tengan configurada una línea braille.

Esta función esta en fase de pruebas.

- **Actualizador de idiomas del complemento:**

Se ha implementado un actualizador que permite mantener los idiomas del complemento siempre actualizados, asegurando la disponibilidad de los idiomas más recientes y precisos.

Ahora en el menú de NVDA > Preferencias > Traductor Avanzado

Tendremos un nuevo item llamado Actualizar idiomas del complemento (Sin actualizaciones).

Dicho item puede que nos informe si existen actualizaciones, por ejemplo:

Actualizar idiomas del complemento (3 actualizaciones disponibles)

Si lo pulsamos nos saldrá un dialogo con los nuevos idiomas, con las actualizaciones o con alguna de las dos si no hay en ambas.

Podremos instalar o omitir.

Si damos a instalar se descargarán los idiomas e instalarán y NVDA se reiniciará.

El item del menú se actualiza cada 30 minutos comprobando si hay actualizaciones o en cada reinicio.

El gasto de datos de esta comprobación es irrisorio por aquellos lugares que tengan problemas de datos es menos de 1kb lo que tiene que comprobar.

Este actualizador facilitara el poder compartir con los usuarios las actualizaciones de los idiomas para el complemento de manera rápida conforme van llegando y sin necesidad de sacar una nueva versión con los nuevos idiomas.

Cada nueva versión del complemento vendrá con todos los idiomas nuevos y actualizados que hayan llegado.

- **Error de lectura continua solucionado:**

Se ha corregido un problema que causaba errores en la lectura continua, mejorando la estabilidad y el rendimiento del complemento durante el uso prolongado.

- **Notas del autor:**

A todas las nuevas funciones como traducir el portapapeles, traducir lo ultimo verbalizado por el sintetizador o comprobar actualizaciones de idioma, se le pueden asignar gestos.

Recomiendo que si alguna opción no vamos a usarla no se le agregue gesto de entrada para poder tenerla en otros complementos. Agreguemos aquellas que nos puedan servir.

Conforme se vayan añadiendo utilidades se necesitarán más gestos y puede que una utilidad no sirva a uno y puede que a otro si por lo que asignemos solo los que vayamos a usar.

[Volver al índice](#indice)