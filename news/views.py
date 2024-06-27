from django.shortcuts import render
from .models import News, Category,Contact, PublishChoice
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def homeindex(request):
    lates_post=News.objects.filter(state=PublishChoice.success).order_by('-created_date')[:3]
    lates_older=News.objects.filter(state=PublishChoice.success)[:8]
    lates_business=News.objects.filter(category__name='Business',state=PublishChoice.success).order_by('-created_date')
    categories=Category.objects.all()

    context={
        'lates_post':lates_post,
        'lates_older':lates_older,
        'lates_business':lates_business,
        'categories':categories
        

    }
    return render(request=request, template_name='news/index.html',context=context)


def contact(request):
    if request.method=='POST':
        data=request.POST
        form=ContactForm(data=data)
        if form.is_valid():
            form.save()
            name=form.data['name']
            email=form.data['email']
            message=form.data['message']

            Contact.objects.create(
                name=name,
                email=email,
                message=message,
            )
          
            context={
                'message':'Malumotlarinigiz yuborildi'
            }
            return render(request=request, template_name='pages/contact.html', context=context)
        else:
            context={
                'form':form,
                   }
            return render(request=request, template_name='pages/contact.html', context=context)
    else:

        form = ContactForm()
        context={
            'form':form
        }
        return render(request=request, template_name='pages/contact.html', context=context)
            
            


    return render(request=request, template_name='pages/contact.html')

def not_404_found(request):
    return render(request=request, template_name='pages/404.html')

def make():
    return 'to me'