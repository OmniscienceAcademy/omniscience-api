# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete`
#       set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create,
#       modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SwipeResults(models.Model):
    id_swipe_session = models.CharField(
        "id_swipe_session", max_length=50, primary_key=True
    )
    query = models.CharField("query", max_length=200)
    pub_date = models.DateTimeField("date published")
    serialized_results = models.TextField("serialized_results")

    # Liste de positive [{id:, score:} ]

    # Liste de negative
    # Liste de candidte
    # Historique des swipe
    # Rajouter undo à swipe
    # date d'ajout de l'article dans la bdd

    # Liste de resultats triés ?
