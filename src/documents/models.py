from distutils import extension
from django.db import models

TYPES = [
    ('MXN', 'Peso'),
    ('DLL', 'Dolar'),
]


class Quote(models.Model):
    '''
    Modelo para cotizaciones
    '''

    company = models.CharField(max_length=255, help_text='Empresa')
    contact = models.CharField(max_length=255, help_text='Contacto')
    date = models.DateField(help_text='Fecha')
    city = models.CharField(max_length=255, help_text='Ciudad')
    phonenumber = models.BigIntegerField(help_text='Telefono')
    address = models.CharField(max_length=255, help_text='Direccion')
    email = models.EmailField(help_text='Email')
    iva = models.IntegerField(help_text='IVA')
    payment_type = models.CharField(max_length=255, help_text='Tipo de pago')
    money_type = models.CharField(
        max_length=3, choices=TYPES, default='MXN', help_text='Moneda')
    commercial_terms = models.TextField(help_text='Condiciones Comerciales')

    def items(self):
        return QuoteItem.objects.filter(quote=self)

    def subtotal(self):
        subtotal = 0
        items = self.items()
        for item in items:
            subtotal += item.total()
        return round(float(subtotal), 2)

    def total(self):
        return round(float(self.subtotal() * (1+(self.iva/100))), 2)

    def only_iva(self):
        return round(self.total()-self.subtotal(), 2)


class QuoteItem(models.Model):
    '''
    Item de cada Cotizacion
    '''
    description = models.TextField(help_text='Descripcion')
    quantity = models.FloatField(help_text='Cantidad')
    unit = models.TextField(help_text='Unidad')
    unit_price = models.FloatField(help_text='Precio Unitario')
    quote = models.ForeignKey('Quote', on_delete=models.CASCADE)

    def total(self):
        try:
            total = self.quantity * self.unit_price
        except Exception:
            total = 0
        return round(float(total), 2)


class PurchaseOrder(models.Model):
    """

    """
    payment_type = models.CharField(max_length=255, help_text='Tipo de pago')
    cfdi = models.CharField(max_length=255, help_text='CFDI')
    construction_site = models.CharField(max_length=255, help_text='Obra')
    contact = models.CharField(max_length=255, help_text='Contacto')
    provider = models.CharField(max_length=255, help_text='Proveedor')
    address = models.CharField(max_length=255, help_text='Direccion')
    city = models.CharField(max_length=255, help_text='Ciudad')
    state = models.CharField(max_length=255, help_text='Estado')
    email = models.EmailField(help_text='Email')
    date = models.DateField(help_text='Fecha')
    rfc = models.CharField(max_length=255, help_text='RFC')
    extension = models.IntegerField(help_text='Extension')
    cp = models.IntegerField(help_text='CP')
    phone = models.IntegerField(help_text='Telefono')

    def subtotal(self):
        subtotal = 0
        items = PurchaseOrderItem.objects.filter(purchase_order=self)
        for item in items:
            subtotal += item.total()
        return round(float(subtotal), 2)

    def total(self):
        return round(float(self.subtotal() * self.iva), 2)


class PurchaseOrderItem(models.Model):
    '''
    Item de cada Orden de Compra
    '''
    description = models.TextField(help_text='Descripcion')
    quantity = models.FloatField(help_text='Cantidad')
    unit = models.TextField(help_text='Unidad')
    unit_price = models.FloatField(help_text='Precio Unitario')
    purchase_order = models.ForeignKey(
        'PurchaseOrder', on_delete=models.CASCADE)

    def total(self):
        try:
            total = self.quantity * self.unit_price
        except Exception:
            total = 0
        return round(float(total), 2)
