class UrbvanRouter:
    """
      A router to control all database operations on models in the
      Urbvan application.
      db_write : Database for users auth.
      default : Database for modeles.
      """

    def db_for_read(self, model, **hints):
        """
        Attempts to read.
        """
        if model._meta.app_label == 'authtoken' or model._meta.app_label == 'auth' or model._meta.app_label == 'sessions':
            return 'db_write'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write.
        """
        if model._meta.app_label == 'authtoken' or model._meta.app_label == 'auth' or model._meta.app_label == 'sessions':
            return 'db_write'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'auth' or \
                obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'authtoken' or app_label == 'auth' or app_label == 'sessions':
            return db == 'db_write'
        return None
