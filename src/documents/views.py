from django.shortcuts import render
from documents.models import Quote, QuoteItem, PurchaseOrder, PurchaseOrderItem
from django.views import generic
from wkhtmltopdf.views import PDFTemplateResponse


class QuoteListView(generic.ListView):
    model = Quote


class QuotePDFView(generic.DetailView):
    model = Quote
    template_name = 'documents/quote_pdf.html'
    context = {'title': 'Hello World!'}

    def get(self, request, *args, **kwargs):
        self.context['quote'] = self.get_object()

        response = PDFTemplateResponse(request=request,
                                       template=self.template_name,
                                       filename="quoute.pdf",
                                       context=self.context,
                                       show_content_in_browser=True,
                                       #cmd_options={'margin-top': 50, }
                                       )
        return response
