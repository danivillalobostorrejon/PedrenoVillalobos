# Practica 1 de Tipologia y Ciclo de Vida de los Datos

### Descripción

Para poder hacer uso de este script es necesario tener instalados los requierements, anexados en este repositorio

**Para ejecutar el código**

Debemos estar en la carpeta y ejecutar la siguiente línea de código:

* Para el primer run:

```
scrapy crawl eci -o test.csv  
```

* Si queremos hacer un *append* de los datos debemos realizar:

```
scrapy crawl eci -o test.csv -t headless
```