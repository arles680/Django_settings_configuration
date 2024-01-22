import os
import subprocess

select_os = input('Enter your operating system (macos or windows): ')

def create_virtualenv(env_path):
    subprocess.run(['python3', '-m', 'venv', env_path])
    print(f'Virtual environment created at {env_path}.')

def activate_venv(env_path):
    activate_path = os.path.join(env_path, 'bin', 'activate')
    subprocess.run([activate_path], shell=True)

def upgrade_pip(env_path):
    subprocess.run([os.path.join(env_path, 'bin', 'python3'), '-m', 'pip', 'install', '--upgrade', 'pip'])
    print('Pip upgraded.')

def install_packages(env_path):
    subprocess.run([os.path.join(env_path, 'bin', 'pip'), 'install', 'django', 'pillow'])
    print('Packages installed.')

def create_django_project(env_path, project_name, app_name):
    subprocess.run([os.path.join(env_path, 'bin', 'django-admin'), 'startproject', project_name])
    os.chdir(project_name)
    subprocess.run([os.path.join(env_path, 'bin', 'python3'), 'manage.py', 'startapp', app_name])
    print(f'Django project "{project_name}" created with app "{app_name}".')

def modify_settings(base_path, project_name, app_name):
    settings_path = os.path.join(base_path, project_name, project_name, 'settings.py')
    with open(settings_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith('INSTALLED_APPS = ['):
            lines.insert(i + 1, f"    '{app_name}',\n")
            break
    lines.append('\n')
    lines.append("MEDIA_URL='/media/'\n")
    lines.append("STATIC_ROOT=BASE_DIR/'static'\n")
    lines.append("MEDIA_ROOT=BASE_DIR/'media'\n")
    with open(settings_path, 'w') as f:
        f.writelines(lines)
    print(f'Updated settings.py with {app_name}.apps.{app_name.capitalize()}Config, STATIC_ROOT, MEDIA_URL, and MEDIA_ROOT.')

def modify_project_urls(base_path, project_name, app_name):
    urls_path = os.path.join(base_path, project_name, project_name, 'urls.py')

    with open(urls_path, 'w') as f:
        f.write("from django.contrib import admin\n")
        f.write("from django.urls import path, include\n")
        f.write("from django.conf import settings\n")
        f.write("from django.conf.urls.static import static\n\n")

        f.write("urlpatterns = [\n")
        f.write("    path('admin/', admin.site.urls),\n")
        f.write(f"    path('', include('{app_name}.urls')),\n")
        f.write("]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n")
    print('Updated urls.py with new URL patterns.')

def create_main_urls(base_path, app_name):
    main_folder = os.path.join(base_path, app_name)
    urls_path = os.path.join(main_folder, 'urls.py')
    views_path = os.path.join(main_folder, 'views.py')

    with open(urls_path, 'w') as f:
        f.write("from django.urls import path\n")
        f.write(f"from . import views\n\n")
        f.write("urlpatterns = [\n")
        f.write("    path('', views.index)\n")
        f.write("]\n")
    print(f'Created main/urls.py for the "{app_name}" app.')

    with open(views_path, 'w') as f:
        f.write("from django.shortcuts import render\n\n")
        f.write("def index(request):\n")
        f.write("    return render(request, 'index.html')\n")
    print(f'Created main/views.py for the "{app_name}" app.')

def MacOS(env_path):
    base_path = os.getcwd()
    project_name = input('Enter project name: ')
    app_name = input('Enter application name: ')

    env_path = os.path.join(base_path, 'venv')
    project_path = os.path.join(base_path, project_name)

    create_virtualenv(env_path)
    activate_venv(env_path)
    upgrade_pip(env_path)
    install_packages(env_path)
    create_django_project(env_path, project_name, app_name)
    modify_settings(base_path, project_name, app_name)
    modify_project_urls(base_path, project_name, app_name)
    create_main_urls(project_path, app_name)
    

if __name__ == '__main__':
    if select_os == "macos":
        MacOS(None)




def create_virtualenv(env_path):
    subprocess.run(['python', '-m', 'venv', env_path])
    print(f'Virtual environment created at {env_path}.')

def activate_venv(env_path):
    activate_path = os.path.join(env_path, 'Scripts', 'activate.bat')
    subprocess.run([activate_path], shell=True)

def upgrade_pip(env_path):
    subprocess.run([os.path.join(env_path, 'Scripts', 'python'), '-m', 'pip', 'install', '--upgrade', 'pip'])
    print('Pip upgraded.')

def install_packages(env_path):
    subprocess.run([os.path.join(env_path, 'Scripts', 'pip'), 'install', 'django', 'pillow'])
    print('Packages installed.')

def create_django_project(env_path, project_name, app_name):
    subprocess.run([os.path.join(env_path, 'Scripts', 'django-admin'), 'startproject', project_name])
    os.chdir(project_name)  # Change working directory to the project
    subprocess.run([os.path.join(env_path, 'Scripts', 'python'), 'manage.py', 'startapp', app_name])
    print(f'Django project "{project_name}" created with app "{app_name}".')


def modify_settings(base_path, project_name, app_name):
    settings_path = os.path.join(base_path, project_name, project_name, 'settings.py')
    with open(settings_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith('INSTALLED_APPS = ['):
            lines.insert(i + 1, f"    '{app_name}',\n")
            break
    lines.append('\n')
    lines.append("MEDIA_URL='/media/'\n")
    lines.append("STATIC_ROOT=BASE_DIR/'static'\n")
    lines.append("MEDIA_ROOT=BASE_DIR/'media'\n")
    with open(settings_path, 'w') as f:
        f.writelines(lines)
    print(f'Updated settings.py with {app_name}.apps.{app_name.capitalize()}Config, STATIC_ROOT, MEDIA_URL, and MEDIA_ROOT.')

def modify_project_urls(base_path, project_name, app_name):
    urls_path = os.path.join(base_path, project_name, project_name, 'urls.py')

    with open(urls_path, 'w') as f:
        f.write("from django.contrib import admin\n")
        f.write("from django.urls import path, include\n")
        f.write("from django.conf import settings\n")
        f.write("from django.conf.urls.static import static\n\n")

        f.write("urlpatterns = [\n")
        f.write("    path('admin/', admin.site.urls),\n")
        f.write(f"    path('', include('{app_name}.urls')),\n")
        f.write("]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n")
    print('Updated urls.py with new URL patterns.')

def create_main_urls(base_path, app_name):
    main_folder = os.path.join(base_path, app_name)
    urls_path = os.path.join(main_folder, 'urls.py')
    views_path = os.path.join(main_folder, 'views.py')

    with open(urls_path, 'w') as f:
        f.write("from django.urls import path\n")
        f.write(f"from . import views\n\n")
        f.write("urlpatterns = [\n")
        f.write("    path('', views.index)\n")
        f.write("]\n")
    print(f'Created main/urls.py for the "{app_name}" app.')

    with open(views_path, 'w') as f:
        f.write("from django.shortcuts import render\n\n")
        f.write("def index(request):\n")
        f.write("    return render(request, 'index.html')\n")
    print(f'Created main/views.py for the "{app_name}" app.')

def Windows(env_path):
    base_path = os.getcwd()
    project_name = input('Enter project name: ')
    app_name = input('Enter application name: ')

    env_path = os.path.join(base_path, 'venv')
    project_path = os.path.join(base_path, project_name)

    create_virtualenv(env_path)
    activate_venv(env_path)
    upgrade_pip(env_path)
    install_packages(env_path)
    create_django_project(env_path, project_name, app_name)
    modify_settings(base_path, project_name, app_name)
    modify_project_urls(base_path, project_name, app_name)
    create_main_urls(project_path, app_name)

if __name__ == '__main__':
    if select_os == "windows":
        Windows(None)


