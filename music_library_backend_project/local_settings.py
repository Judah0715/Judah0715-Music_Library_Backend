# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = 'django-insecure-x7-19*c8ayhoaoix=b)jo!2t@g=+!2^c8)k4tc^_0l+9j6b&be' 



# Database
# https://docs.djangoproject.com/en/4.0/ref.settings/#databases

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_backend',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}