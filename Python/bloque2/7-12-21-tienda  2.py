t=0
iva=1.16
while(t>=0):
  
  t=t+1

  cajeronombre=input('Buenas Tardes,       Bienvenid@ a la tienda RANA CALVA lo estará atendiendo:')
  print('Buenas tardes mi nombre es',cajeronombre,'será un gusto atenderl@ en su compra el día de hoy')

  articulo=int(input('El chocolate cuesta:'))

  articulo2=int(input('La mochila cuesta:'))

  articulo3=int(input('Las papas cuestan:'))
 
  articulo4=int(input('La caja de cubrebocas cuestan:'))

  articulo5=int(input('El libro cuesta:'))

  print('El subtotal a pagar es',articulo+articulo2+articulo3+articulo4+articulo5)
  subtotal=articulo+articulo2+articulo3+articulo4+articulo5

  print('y su total con iva será de',subtotal*iva)
  Total=subtotal*iva
  
  print('~~~~~~~~~~~~~~~~~~~~~~~~')

  print('|TICKET DE COMPRA.      |')
  print('|Tienda RANA CALVA.     |')
  print('|Chocolate=',articulo,'.         |')
  print('|Mochila=',articulo2,'.           |')
  print('|Papas=',articulo3,'.             |')
  print('|Caja de cubrebocas=',articulo4,'.|')
  print('|Libro=',articulo5,'.             |')
  print('|Numero de articulos=5. |')
  print('|Subtotal=',subtotal,'.         |')
  print('|Total=', Total,'.          |')
  print('~~~~~~~~~~~~~~~~~~~~')
