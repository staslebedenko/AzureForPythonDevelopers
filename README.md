# Azure for Python developers
Workshop repository for AtomSpace and IT2School community.

You can do this workshop(lab) by yourself, 
just use detailed steps below and get free Azure account https://azure.microsoft.com/en-us/free/.

Goal is to create simple Django application and deploy it via Git to Azure Web App.
You will have a hands on with Azure web interface and Azure CLI via bash.

Intial version of workshop is oriented towards Windows OS.
Requirenment is a Windows, VS Code, Git, Python 3.7
You can use git command line or SourceTree for repository init and commits to master.
Dont forget to add .gitignore file for python in your master branch. 

STEP 1. Application scaffold
STEP 2. Application configuration change.
	Azure infrastructure setup with Azure CLI.
	Deployment of the application.

STEP 1.
-------------


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
	
-------------	
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
		from django.urls import path

        urlpatterns = [
          #path('admin/', admin.site.urls),
          path("", include("WebApp.urls")),
        ]
	
5. Start your application to verify changes
	
	    python manage.py runserver 5050


STEP 2.
-------------
Initialize git repository for your folder and add .gitignore for python (you can use ignore file from my repo)
IMPORTANT! Root folder is the folder with manage.py file. 

	git init
	git add
	git add .gitignore
	git commit	

Then We need to slightly update our repo  with following code.

1. Add requirements.txt with following text
We need white noise for static files handling.

		Django==2.2.1
		whitenoise==4.1.2
		
2. Update file AzurePythonBootcampWeb/settings.py by
	Replacing
	
		ALLOWED_HOSTS = []
	With 
	
		ALLOWED_HOSTS = [os.environ['WEBSITE_SITE_NAME'] + '.azurewebsites.net', '127.0.0.1'] if 'WEBSITE_SITE_NAME' in os.environ else []

	Replacing 
	
		    'django.middleware.security.SecurityMiddleware',
		    
	With
	
		    'django.middleware.security.SecurityMiddleware',
    			'whitenoise.middleware.WhiteNoiseMiddleware',
			
	Adding at the end of file

		STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
	
		STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

-------------
Lets move to the Azure part

1. Lets start with Azure CLI script execution.
Open Azure portal and select bash console.

		export groupName="atomspace-azureforpython-webapps"
		export primaryLocation="northeurope"
		export deploymentUser="AtomAzureForPythonLogin" 
		export deploymentPass=""
		export servicePlanName="AzurePythonBootcamp"
		export appName="AtomAzurePythonWeb2019"

		az group create --name $groupName --location $primaryLocation

		az webapp deployment user set --user-name $deploymentUser --password $deploymentPass

		az appservice plan create --name $servicePlanName --resource-group $groupName --sku B1 --is-linux

		az webapp create --resource-group $groupName --plan $servicePlanName --name $appName --runtime "PYTHON|3.7" --deployment-local-git


2. Well Done. Now save output parameter deploymentLocalGitUrl from bash somewhere

		"deploymentLocalGitUrl": "https://AtomAzureForPythonLogin@atomazurepythonweb2019.scm.azurewebsites.net/AtomAzurePythonWeb2019.git",

3. Now create empty local git repo and copy your project there, make sure that requirements.txt is in master root.

4. Run following command and provide password from the first step

		git remote add azure https://AtomAzureForPythonLogin@atomazurepythonweb2019.scm.azurewebsites.net/AtomAzurePythonWeb2019.git

5. Lets push our application to Azure

		git pull
		git push azure master

Observe output results, yes there is a docker container

6. Lets add simple logging for your application. Application insights we add later on.

		export groupName="atomspace-azureforpython-webapps"
		export appName = "AtomAzurePythonWeb2019"
		az webapp log config --name #appName --resource-group $grounName --docker-container-logging filesystem

7. To read logs in bash console, execute command

		az webapp log tail --name $appName --resource-group $groupName

8. To read application logs manually

		Visit url https://atom-azure-python-web2019.scm.azurewebsites.net/api/logs/docker to read logs

9. Dont forget to delete your subscription

		export grounName="atomspace-azureforpython-webapps"
		az group delete --name $groupName


