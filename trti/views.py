from django.shortcuts import render,redirect

# Create your views here.

def home(request):
         return render(request,'trti/home.html',{})


def map(request):
         return render(request,'trti/new.html')

def gallery(request):
         return render(request,'trti/gallery.html',{})

def aboutus(request):
         return render(request,'trti/aboutus.html',{})

def villages(request):
            return render(request,'trti/trti_villages.html',{})

def whoswho(request):
            return render(request,'trti/stakeholders.html',{})

def umainstitutes(request):
            return render(request,'trti/umainstitutes.html',{})

def proposedschemes(request):
            return render(request,'trti/proposed_schemes.html',{})

def contactus(request):
            return render(request,'trti/contactus.html',{}) 


def background(request):
            return render(request,'trti/background.html',{})

def vision(request):
            return render(request,'trti/vision.html',{})

def coursesdetails(request):
            return render(request,'trti/coursesdetails.html',{}) 

def reports(request):
            return render(request,'trti/analysisreport.html',{}) 
            
            
def links(request):
            return render(request,'trti/links.html',{})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              