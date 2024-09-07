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
  - [Versión 2024.06.23](#version-2024-06-23)
  - [Versión 2024.09.07](#version-2024-09-07)

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
- **Francés:** Rémy Ruiz.

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

<h3 id="version-2024-06-23">Versión 2024.06.23</h3>

* Agregado nuevo modulo Traductor DeepL (Free)

Este nuevo modulo no necesita de clave API y es utilizado para la traducción simultanea 

* Corrección de errores

[Volver al índice](#indice)

<h3 id="version-2024-09-07">Versión 2024.09.07</h3>
#### Interfaz de Traducción

La **Interfaz de Traducción** es el componente principal del complemento **Traductor Avanzado** para NVDA. Esta interfaz permite al usuario traducir texto entre distintos idiomas de manera eficiente, mostrando el texto original y el traducido, y brindando varias opciones de personalización.

Para invocarlo tendremos que asignar una combinación de teclas en gestos de entrada o desde el menú virtual (explicado más abajo).

##### Funcionalidades principales:

1. **Entrada de texto origen**: Permite al usuario escribir o pegar el texto que desea traducir. Se puede acceder rápidamente con la combinación de teclas `Alt+1`.
   
2. **Texto destino (resultado)**: El área donde se muestra el texto traducido. Este campo es de solo lectura y se puede enfocar con `Alt+2`.

3. **Selección de idioma origen**: Permite seleccionar el idioma del texto origen. El idioma por defecto es la opción "Auto Detectar", que permite al sistema detectar automáticamente el idioma del texto. Se accede con `Alt+3`.

4. **Selección de idioma destino**: Permite seleccionar el idioma al cual se quiere traducir el texto. Se puede enfocar con `Alt+4`.

5. **Contador de caracteres**: Muestra el número de caracteres en el campo de texto de origen. Es útil para conocer la cantidad de texto que será traducido. Se accede con `Alt+5`.

6. **Botones de acción**:
   - **Traducir**: Inicia la traducción del texto ingresado.
   - **Escuchar**: Obtiene el audio de la traducción y permite reproducirlo a través de un reproductor integrado (ver sección más abajo).
   - **Intercambiar**: Intercambia el idioma de origen con el de destino, útil si deseas revertir los idiomas de traducción.
   - **Limpiar**: Limpia tanto el campo de texto de origen como el de destino.
   - **Pegar al foco**: Pega el texto traducido en la ventana o campo de texto activo detrás de la interfaz. También se puede activar con `F3`.
   - **Cerrar**: Cierra la ventana de traducción.

##### Atajos de teclado:

- `Alt+1`: Enfocar el cuadro de texto de origen.
- `Alt+2`: Enfocar el cuadro de texto de destino.
- `Alt+3`: Seleccionar el idioma de origen.
- `Alt+4`: Seleccionar el idioma de destino.
- `Alt+5`: Enfocar el contador de caracteres.
- `F3`: Pegar el texto traducido en la ventana activa.
- `Esc`: Cerrar el diálogo de traducción.

##### Comportamiento en caso de errores:

- Si no hay conexión a Internet, el sistema mostrará un mensaje informando de la falta de conexión.
- Si el cuadro de texto de origen está vacío, el usuario recibirá una advertencia solicitando ingresar texto antes de realizar la traducción.
- Si el idioma de origen y el de destino son iguales, se mostrará una advertencia indicando que no es necesario traducir el texto al mismo idioma.

##### Funciones adicionales:

- **Auto-detección de idioma**: Si se selecciona "Auto Detectar" en el idioma de origen, el complemento intentará identificar automáticamente el idioma del texto a traducir.
- **Intercambio de idiomas**: Esta función es útil cuando se desea traducir de regreso un texto al idioma original.

#### Reproductor de Audio

Cuando el usuario utiliza la opción **Escuchar** tras realizar una traducción, el complemento convierte el texto traducido en un archivo de audio y lo reproduce a través de un reproductor integrado. Este reproductor incluye controles básicos y avanzados para gestionar la reproducción de audio.

##### Funcionalidades del reproductor:

1. **Botones de control**:
   - **Atrasar (F1)**: Retrocede la reproducción de acuerdo con el tiempo seleccionado. El usuario puede configurar este tiempo.
   - **Reproducir/Pausar (F2)**: Inicia o pausa la reproducción del archivo de audio.
   - **Adelantar (F3)**: Adelanta la reproducción de acuerdo con el tiempo configurado por el usuario.
   - **Detener (F4)**: Detiene la reproducción por completo.

2. **Volumen y velocidad**:
   - **Volumen (F5/F6)**: Ajusta el volumen de reproducción utilizando un control deslizante.
   - **Velocidad (F7/F8)**: Cambia la velocidad de reproducción, con opciones desde 0.50x hasta 2.0x la velocidad normal.

3. **Texto asociado**: Muestra el texto traducido en un cuadro de solo lectura, permitiendo al usuario visualizar lo que está siendo reproducido.

4. **Guardar**: Permite guardar el archivo de audio generado en formato WAV en el sistema del usuario.

5. **Cerrar**: Cierra el reproductor y libera los recursos asociados.

##### Atajos de teclado:

- `F1`: Atrasar la reproducción.
- `F2`: Reproducir o pausar el audio.
- `F3`: Adelantar la reproducción.
- `F4`: Detener la reproducción.
- `F5/F6`: Ajustar el volumen.
- `F7/F8`: Cambiar la velocidad de reproducción.
- `F9`: Información del tiempo de la reproducción.
- `Shift+F10/Aplicaciones`: En los botones atrasar y adelantar desplegará un menú contextual para elegir el tiempo correspondiente.

##### Funciones adicionales:

- **Guardar audio**: Los usuarios pueden optar por guardar el archivo de audio en su dispositivo en formato WAV para su posterior uso.
- **Menú de opciones avanzadas**: El reproductor permite elegir el tiempo exacto para atrasar o adelantar la reproducción mediante un menú contextual (accedido con la tecla `Shift+F10`) o tecla aplicaciones.

#### Menú virtual

Se a agregado un menú virtual el cual contiene todas las opciones que el complemento tiene.

Podremos invocar desde el menú virtual todas las opciones que podemos asignar en gestos de entrada, de esta manera desde el menú virtual el complemento puede ser usado totalmente sin necesidad de tener más teclas asignadas al complemento.

Esto ya queda a gusto del usuario.

Para poder invocar el menú virtual tendremos que asignarle una tecla en gestos de entrada.

El uso del menú virtual es sencillo, una vez invocado tendremos que pulsar la tecla correspondiente para la acción que deseemos ejecutar.

Una vez pulsada se ejecutara y siempre se nos informara de lo realizado, si pulsamos una tecla que no esta asignada el menú virtual se cerrara y también podemos cerrarlo con escape.

##### Atajos de Teclado del Menú Virtual

El menú virtual del Traductor Avanzado te permite acceder rápidamente a las funciones más útiles del complemento. A continuación, te presentamos los atajos que puedes usar para realizar varias acciones:

- **`P`**: **Abrir configuración**  
  Abre la configuración del Traductor Avanzado donde puedes ajustar los idiomas y servicios de traducción.

- **`U`**: **Buscar actualizaciones de idioma**  
  Busca y descarga las actualizaciones disponibles para los idiomas del complemento.

- **`O`**: **Cambiar idioma de origen**  
  Cambia el idioma del texto que deseas traducir (idioma de origen).

- **`D`**: **Cambiar idioma de destino**  
  Cambia el idioma al que deseas traducir el texto (idioma de destino).

- **`C`**: **Cambiar servicio de traducción**  
  Permite cambiar entre los servicios de traducción disponibles, como Google, DeepL, Microsoft, entre otros.

- **`A`**: **Eliminar toda la caché de traducción**  
  Borra todas las traducciones almacenadas en caché.

- **`X`**: **Eliminar caché de traducción de la aplicación actual**  
  Borra las traducciones en caché solo para la aplicación que tienes abierta.

- **`G`**: **Activar/Desactivar caché de traducción**  
  Activa o desactiva la función de caché que guarda temporalmente las traducciones.

- **`L`**: **Copiar última traducción al portapapeles**  
  Copia la última traducción realizada al portapapeles para que puedas pegarla donde la necesites.

- **`B`**: **Traducir el texto del portapapeles**  
  Traduce el contenido actual del portapapeles.

- **`V`**: **Traducir el último texto verbalizado**  
  Traduce el último texto que NVDA haya leído en voz alta.

- **`T`**: **Activar/Desactivar traducción en tiempo real**  
  Activa o desactiva la traducción automática mientras navegas por textos.

- **`S`**: **Traducir el texto seleccionado**  
  Traduce el texto que has seleccionado en la aplicación.

- **`Z`**: **Traducir texto del objeto del navegador**  
  Traduce el texto de un objeto específico dentro del navegador, como un botón o un cuadro de texto.

- **`W`**: **Abrir interfaz de traducción**  
  Abre la ventana gráfica donde puedes introducir manualmente el texto que deseas traducir.

- **`I`**: **Detectar idioma seleccionado**  
  Detecta automáticamente el idioma del texto seleccionado.

- **`J`**: **Activar/Desactivar intercambio automático de idiomas**  
  Activa o desactiva el intercambio automático si el idioma de origen detectado coincide con el idioma de destino.

- **`K`**: **Intercambiar idiomas principal y alternativo**  
  Intercambia el idioma principal con el idioma alternativo en la configuración del traductor.

- **`H`**: **Mostrar historial de traducción**  
  Muestra un historial de las traducciones recientes realizadas.

- **`F1`**: **Mostrar lista de comandos**  
  Muestra un diálogo con la lista de comandos de una sola tecla para el Traductor Avanzado.

#### Detección de idioma

Esta opción permite detectar automáticamente el idioma del texto que hayas seleccionado en cualquier aplicación. Para usar esta función:
1. Selecciona el texto del cual deseas conocer el idioma.
2. Utiliza el atajo de teclado configurado en los gestos de entrada (o el menú virtual) para activar la detección de idioma.
3. El sistema detectará y te informará del idioma en el que está escrito el texto seleccionado.
Esta función es útil cuando no estás seguro del idioma de un texto y necesitas saberlo antes de traducirlo o realizar alguna otra acción.

#### Intercambio Automático de Idiomas en Traductor Avanzado NVDA

  1. Activa el intercambio automático presionando el atajo de teclado correspondiente o accediendo desde el menú virtual.
  2. Si el texto que seleccionas está en el mismo idioma que el idioma de destino, el sistema cambiará automáticamente el idioma de destino al idioma alternativo para evitar traducciones innecesarias.
  3. Puedes desactivar esta opción en cualquier momento utilizando el mismo atajo.

##### Configuración de Idiomas en el Complemento

- Puedes configurar los **idiomas de destino** y **idiomas alternativos** accediendo a **Configuración del complemento** en el apartado de **General**. Desde ahí puedes seleccionar los idiomas que se usarán para el intercambio automático.

Esta función es útil para evitar confusiones al traducir textos en los que el idioma de origen es igual al de destino, cambiando automáticamente a un idioma alternativo configurado.

#### Ayuda en Diálogos del Complemento

Se ha agregado la funcionalidad para mostrar ayuda contextual en los diálogos del complemento. Al presionar la combinación de teclas `Ctrl+H`, se mostrará una pequeña descripción de la función del widget que está actualmente enfocado.

En cualquier parte de los diálogos del complemento, si necesitas información sobre la función de un botón, cuadro de texto, deslizador u otro control, simplemente puedes pulsar `Ctrl+H`. Esto mostrará una breve descripción del widget enfocado, proporcionando una guía rápida sobre su uso.

#### Traduce texto del objeto del navegador

Esta funcionalidad permite traducir el texto de un objeto específico dentro del navegador o cualquier otra aplicación que NVDA esté utilizando. Se puede activar a través del menú virtual o mediante una combinación de teclas asignada en los gestos de entrada del complemento.

1. Coloca el cursor sobre el objeto que deseas traducir (puede ser un botón, un cuadro de texto, etc.).
2. Activa la funcionalidad presionando la combinación de teclas asignada o a través del menú virtual.
3. El complemento traducirá el texto contenido en ese objeto y lo mostrará o verbalizará, dependiendo de la configuración.

- Traduce cualquier texto contenido en el objeto seleccionado dentro de una página web, aplicación o cualquier otra interfaz donde NVDA interactúe.
- Útil para traducir pequeños fragmentos de texto que no son parte del cuerpo principal de una página o aplicación, como menús, botones, o etiquetas.
- Si el objeto no contiene texto o es inaccesible, el complemento mostrará un mensaje informando que no hay texto para traducir.

- Puedes acceder a esta funcionalidad tanto desde el menú virtual del complemento como configurando una tecla de acceso rápido en los "Gestos de entrada" de NVDA.

#### Modulo de OpenAI

Se a agregado un nuevo modulo para traducir con OpenAI con el modelo chatGPT-4º-mini que es el más barato y rápido.

Este modulo esta en pruebas teniendo algunas veces un poco de lag, pero mejorara en futuras versiones.

Este modulo necesita que se asigne una clave API en configuración / módulos.

OpenAI es de pago por lo que es función del usuario comprobar su gasto.

En el siguiente enlace se puede mirar el gasto que llevamos:

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Mejora en el modulo de Microsoft

El modulo del traductor de Microsoft a sido escrito desde cero y mejorado la rapidez, estabilidad y el poder tener más tiempo de traducción hasta que bloqueen por uso y tengamos que esperar unos minutos para volver a traducir.

Ahora en las pruebas realizadas y traduciendo simultáneamente bastante texto más de un uso normal no e sufrido ninguna restricción.

Por lo que de momento funciona y se a mejorado respecto al modulo anterior.

#### Otros

* Solucionado problema con la verbalización de algunos mensajes.
* Cambiada forma de comprobar si hay internet.
*Corrección de errores
* Agregado oficialmente idioma francés.

[Volver al índice](#indice)
