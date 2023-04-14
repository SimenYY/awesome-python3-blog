import pymysql
# prevent "django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.3 or newer is required; you have 1.0.3."
pymysql.version_info = (1,4,13,"final", 0)
pymysql.install_as_MySQLdb()