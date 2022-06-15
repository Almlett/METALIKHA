from django.db import models

class QuoteItem(models.Model):
    '''
    Item de cada Cotizacion
    '''
    description = models.TextField(help_text = 'Descripcion')
    quantity = models.FloatField(help_text = 'Cantidad')
    unit  = models.TextField(help_text = 'Unidad')
    unit_price = models.FloatField(help_text = 'Precio Unitario')
    
    def total(self):
        return self.quantity * self.unit_price

class Quote(models.Model):
    '''
    Modelo para cotizaciones
    '''
    TYPES = [
        ('MXN', 'Peso'),
        ('DLL', 'Dolar'),
    ]

    company = models.CharField(max_length=255, help_text='Empresa')
    contact = models.CharField(max_length=255, help_text='Contacto')
    date = models.CharField(max_length=255, help_text='Fecha')
    city = models.CharField(max_length=255, help_text='Ciudad')
    phonenumber = models.CharField(max_length=255, help_text='Telefono')
    address = models.CharField(max_length=255, help_text='Direccion')
    email = models.CharField(max_length=255, help_text='Correo')
    iva = models.CharField(max_length=255, help_text='IVA')
    payment_type = models.CharField(max_length=255, help_text='Tipo de pago')
    money_type = models.CharField(max_length=3,choices=TYPES,default='MXN', help_text = 'Moneda')
    commercial_terms = models.TextField(help_text = 'Condiciones Comerciales')
    items = models.ManyToManyField(QuoteItem, blank=True)

    def subtotal(self):
        subtotal = 0
        items = self.items
        for item in items:
            subtotal += item.total()
        return subtotal

    def total(self):
        return self.subtotal() * self.iva