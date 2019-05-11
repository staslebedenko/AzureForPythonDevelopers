# AzureForPythonDevelopers
Workshop repository for AtomSpace and IT2School community.

Intial version of workshop is oriented towards Windows OS.
Requirenment is a Windows, VS Code, Git, Python 3.7

Lets start with installation of components.
We will work with Python virtual environments.

1. Install virtualenv and virtualenvwrapper
Virtualenv and virtualenvwrapper provide a dedicated environment for each Django project you create.
While not mandatory, this is considered a best practice and will save you time in the future when
you’re ready to deploy your project.

    pip install virtualenvwrapper-win

2. Then create a virtual environment for your project:

        mkvirtualenv AzurePythonBootcamp

3. Now you should switch your environment byt restarting VS Code
Running terminal with Ctrl+Shift+P  and selecting newly created Virual Environment (you can switch it in bottom status bar too)
Then close and open terminal again, it should be pointed towards your virtual environment

4. Install Django in your local environment
	
	    python -m pip install django	
	
5. Create your project
	
	    django-admin startproject AzurePythonBootcampWeb
		    
6. Change directory to your project folder

	    cd AzurePythonBootcampWeb
	
7. Run development server and visit page http://127.0.0.1:5050/

	    python manage.py runserver 5050
	
	
Lets proceed with application itself

1. First we will create empty template
	
	    python manage.py startapp WebApp	
	
2. As second step we will modify contents of hello/views.py with code below:
	
	    from django.http import HttpResponse

	    # Create your views here.
	    def home(request):
		      return HttpResponse("Your first published app in Azure!")
	
3. Then we will create a file, WebApp/urls.py and add routing configuratio code below. 

	    from django.urls import path
	    from WebApp import views

	    urlpatterns = [
		    path("", views.home, name="home"),
	     ]
	
4. Last step is to modify file AzurePythonBootcampWeb/urls.py with code below

        from django.urls import include

        urlpatterns = [
          #path('admin/', admin.site.urls),
          path("", include("WebApp.urls")),
        ]
	
5. Start your application to verify changes
	
	    python manage.py runserver 5050


