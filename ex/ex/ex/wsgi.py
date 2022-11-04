# wsgi_win.py

from django.core.wsgi import get_wsgi_application
import site
import sys
import os
# activate_this = 'C:/Users/aaa57/newEnv/Scripts/activate_this.py'

# exec(open(activate_this).read(), dict(__file__=activate_this))


# 가상환경의 패키지 추가
site.addsitedir('C:/conda/envs/django-1/Lib/site-packages')

# PYTHONPATH에 application directory 추가
path = os.path.abspath(__file__+'/../..')
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ex.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ex.settings")

application = get_wsgi_application()
