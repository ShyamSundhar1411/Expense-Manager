SECRET_KEY = '_gsl0f5yct#yaj=h3-b#vr%o@$3h9t3rf!6!puqp3_f^+zyz5&'
SITE_ID = 1
#SocialAccountProviders
SOCIALACCOUNT_PROVIDERS = {
    'google':{
        'APP':{
            'client_id':'325531148519-fdqce5j0rk78ijha3irsqj961mdut7em.apps.googleusercontent.com',
            'secret': 'wX7X0WN1-v_S8Pr8tDnOt5kN'
        },
        'SCOPE':{
            'profile',
            'email',
        },
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'github':{
        'APP':{
            'client_id': '6f3b7a0fd8193deae27f',
            'secret': 'b6e66dd708956e59ee5ef9206b552645d7d9c028'
        },
        'SCOPE':{
            'user',
            'repo',
        }
    }
}
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
]
#Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '325531148519-fdqce5j0rk78ijha3irsqj961mdut7em.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'wX7X0WN1-v_S8Pr8tDnOt5kN'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'profile',
    'email',
]
#GitHub
SOCIAL_AUTH_GITHUB_KEY = '6f3b7a0fd8193deae27f'
SOCIAL_AUTH_GITHUB_SECRET =  'b6e66dd708956e59ee5ef9206b552645d7d9c028'
SOCIAL_AUTH_GITHUB_SCOPE = [
    'user',
    'repo',
]
#Email Backends
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USER_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'clashwithchiefrpjyt@gmail.com'
EMAIL_HOST_PASSWORD = 'pjtioxzccqphhddc'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'CodeBusters Team <noreply@expensemanager.com>'
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
CELERY_RESULT_BACKEND = 'django-cache'
CELERY_CACHE_BACKEND = 'default'

# django setting.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'Cached_Table',
    }
}
