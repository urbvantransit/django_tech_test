# coding: utf-8

class DefaultReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to the replica.
        """
        return 'default_replica'

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are always allowed because they are
        in the same cluster.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Same as allow relations.
        """
        return True