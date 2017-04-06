# Example app with docker and django

#Preguntas/Respuestas

P- Indica cómo se puede optimizar el rendimiento del servicio de listado de cursos de cocina.

R- Esto siempre será un problema con el que sobrecargaremos el servidor, podríamos montarlo por websockets para que nos actualice solo con las últimas novedades cuando estemos en el listado de cursos, o se podría limitar los cursos que se muestran


P- Dicen que las bases de datos relacionales no escalan bien,
se me ocurre montar el proyecto con Django y una noSQL, ¿qué me recomiendas?

R- La única que he usado hasta ahora ha sido Redis y MongoDB, y me ha ido muy bien, aúnque siempre he escuchado de Cassandra y ElasticSearch buenas impresiones también.


P- ¿Qué tipo de métricas y servicios nos pueden ayudar a comprobar que la API y el servidor funcionan correctamente?

R- Podríamos tener unos test en selenium que se ejecuten cada cierto tiempo y con ello tendremos asegurado que tanto nuestra API como nuestro servidor esté en funcionamiento


P- ¿Cómo sería tu entorno de desarrollo open source ideal?

R- Mi entorno de desarrollo ideal, es como estoy ahora mismo, Sublime Text 2 y iTerm, usando brew para los servicios y pip para las dependencias que pueda tener mi proyecto y virtualenv para usar un ambiente virtual para todas las dependencias del proyecto.