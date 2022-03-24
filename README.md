<!-- 
    DOCUMENTACIÓN
    # Web app Tienda Lissa


    1.0 ## Definicion del problema
        Contextualizar o interpretar el problema de manera que permita desarrollar su solución.

        1.1 ### Description:
            Aplicación web para administrar las ventas en general de una tienda, tendrá algunas características para tener mayor control como por ejemplo, registro de deudas de clientes, las compras que la tienda hace a su proveedor, todo mediante registros. A continuación, se muestra un listado de las características que tendrá dicha app.

        1.2 ### Features:
            - Tener un home para mostrar todas las herramientas
            - Registrar ventas
                 - Nombre
                 - Descripcion
                 - Cantidad 
                 - Precio por prenda
                 - No pagado: checkbox
            - Al visualizar las ventas
                 - Fecha al inicio
                 - Nombre
                 - Descripcion
                 - Cantidad
                 - Precio por prenda
                 - Total
                 - No pagado: si se activo antes el checkbox
            - Registrar compras

        1.3 ### Avanced features:
             - Tener un buscador que me recopile las ventas por nombre o fecha
             - Resumen diario, semanal y mensual
             - Gráficos para cada uno de los resumenes


    2.0 ## Análisis del problema
        Consiste en analizar las herramientas, métodos, costes, estructura, etc. y utilizar lo más adecuado para la elaboración de la solución.

            2.1 ### Herramientas:
                2.1.1 - Backend
                         - Docker
                         - PostgressSQL DataBase
                         - Python with Django + RestFramework
                2.1.2 -Frontend
                         - Js, Html, Css
                         - Boostrap (Aprender)
                2.1.3 - Opcionales
                         - Boostrap
                         - RestFramework

            2.2 ### Patrones:
                      - MVT que ofrece el framework Django de python


    3.0 ## Diseño del algoritmo
        Dibujar el camino que resuelva el problema de la forma más optima posible
        - Tiene que ser definido, preciso y finito

        ### Algoritmo:
            - Sección 1:
                 - Crear formulario de registro ventas
                 - validar los datos y guardarlos en una DB
                 - Crear parte del home para imprimir los registros de ventas
            --------------------------------------------------------------------
            - Sección 2:
                 - Crear template que muestre las ventas registradas que no están pagadas, permitir seleccionarlas y pagarlas mediante checkboxes
                     - Al seleccionar al menos un registro no pago, que aparezca un botón que valide la acción
                 - Buscador de ventas por nombre, día(nn/nn/nnnn), o mes(Septiembre)
            - Sección 3:
                 - Crear resúmenes con sus gráficos
            - Sección 4
                 - Crear formulario de registro de compras
                 - Guardarlos e imprimirlos en home, debajo de las ventas


    4.0 ## Etapa de desarrollo
            
            4.1 ### Etapa 1:
                4.1.1- Backend:
                        a) - Armar el modelo en django
                             - Fecha al inicio (Dinamic)
                             - Nombre
                             - Descripción
                             - Cantidad
                             - Precio por prenda
                             - Total (Dinamic)
                             - No pagado: si se activo antes el checkbox
                        b) - Validar los datos y guardarlos en la DB
                4.1.2- Frontend:
                         a) - Button de añadir más bloques de registro
                         b) - Button para eliminar bloques de registro si es que hay más de uno
                         c) - Enumerar los bloques de registro
                         d) - Button de guardar registros
                         e) - Checkbox de producto no pagado (fiado)
                         f) - Validar los datos y enviarlos al servidor

            4.2 ### Etapa 2:
                4.2.1- Backend:
                         a) - Leer los registros de ventas de la DB
                         b) - Filtrar los resultados que estén pagados
                              y mostrarlos en el template index (sólo los primeros 10)
                         c) - Filtrar los resultados que no estén pagados
                              y mostrarlos en el template saldos (sólo los primeros 10)
                4.2.2- Frontend:
                         a) - Crear el index e imprimir los registros leidos
                         c) - Crear template de saldos (fiados) e imprimir
                              los registros de productos no pagos leidos
                         b) - Button ver más registros, para que aparezcan 10 más
                              así evitamos sobrecargar la app (en index y saldos)
                         c) - Crear buscador de registros de ventas por:
                                - Nombre
                                - Fecha dd/mm/yyyy
                                - Mes: Ene, Feb, Mar, Abr, May,
                                       Jun, Jul, Ago, Sep, Oct,
                                       Nov, Dic.

            4.3 ### Etapa 3:
                4.3.1- Backend:
                         a) - Resumenes con los datos obtenidos (revisar)
                                - Diario, semanal, mensual
                4.3.2- Frontend:
                         a) En el index insertar:
                                - Mostrar los resúmenes y generar los gráficos
                                    - Diario: Gráfico de torta
                                    - Semanal: Gráfico de barras
                                    - Mensual: Gráfico de barras
                         c) - Añadir al resumen
                                - Ingresado:
                                    - Dentro del gráfico de torta en el caso de diario
                                    - En el gráfico de barras, ingrsar los datos arriba en h2
                                - Porcentaje obtenido $+0,4 (27%)
                                - Total ventas: 22 | Saldos: 14

-->

# Web app tienda lissa

Aplicación web para controlar ventas y deudas de clientes

## Características
    - Registro de ventas
    - Buscador de registros
    - Resumenes diarios, semanales y mensuales
    - Registro de compras realizadas al proveedor

## Version 1.1
## License ...