from django.shortcuts import render
from django.forms.formsets import formset_factory
from django.contrib import messages

# Create your views here.
from testapp.apps.compare.forms import InputForm


def index(request):
    form_string_set = formset_factory(InputForm, extra=4)
    if request.method == 'POST':
        form = form_string_set(request.POST, prefix='String')
        data =[]
        if form.is_valid():
            for form_string in form:

                data.append(form_string.get_string())

            data = filter(None, data)
            numOfStrings = len(data)
            data.sort(key=len)
            max =[]
            for i in range(numOfStrings-1):
                leastStr = data.pop(0)
                maxSharedStr = ''

                while len(leastStr) > len(maxSharedStr):
                    robTestStr = leastStr
                    while len(robTestStr) > len(maxSharedStr):
                        numOfConcidence = 0
                        for compatStr in data:
                            if robTestStr in compatStr:
                                numOfConcidence += 1

                        if numOfConcidence >= 2 and len(robTestStr) > len(maxSharedStr):
                            maxSharedStr = robTestStr
                            max.append(robTestStr)
                        robTestStr = robTestStr[:-1]
                    leastStr = leastStr[1:]
            max.sort(key=len, reverse=True)
            if max:
                return render(request, 'compare/index.html', {'form': form, 'result':max[0]})
            else:
                messages.add_message(request, messages.ERROR, "No duble")
                return render(request, 'compare/index.html', {'form': form})
        else:
            messages.add_message(request, messages.ERROR, "Error.")
            return render(request, 'compare/index.html', {'form': form})
    else:
        form = form_string_set(prefix='String')
        return render(request, 'compare/index.html', {'form': form})

