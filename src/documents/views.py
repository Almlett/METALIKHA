from django.shortcuts import render
from documents.forms import QuoteForm


def quote_new(request):
    if request.method == "quote":
        form = QuoteForm(request.quote)
        if form.is_valid():
            quote.save()
            return redirect('quote_detail', pk=quote.pk)
    else:
        form = QuoteForm()
    return render(request, 'quote_edit.html', {'form': form})