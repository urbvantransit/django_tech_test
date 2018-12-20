class UrbvanRouter:
    """
      A router to control all database operations on models in the
      Urbvan application.
      """
    def db_for_read(self, model, **hints):
        """
        Attempts to read Urbvan models go to db_read.
        """
        if model._meta.app_label == 'urbvan':
            return 'db_read'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to db_write.
        """
        if model._meta.app_label == 'urbvan':
            return 'db_write'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'urbvan' or \
                obj2._meta.app_label == 'urbvan':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'db_write'
        database.
        """
        if app_label == 'urbvan':
            return db == 'db_write'
        return None
