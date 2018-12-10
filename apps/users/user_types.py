# coding: utf8
from django.utils.translation import gettext as _

# User Types - Conf
USER_TYPES = {
    "supervisor": 1,
    "driver": 2,
    "passenger": 3,
}

USER_TYPES_DESCRIPTION = {
    "supervisor": _("Supervisor"),
    "driver": _("Driver"),
    "passenger": _("Passenger")
}

# User Types - Utils
def get_user_type_choices():
	user_types_choices = []
	for ut in USER_TYPES:
		user_types_choices.append(
			(USER_TYPES[ut], USER_TYPES_DESCRIPTION[ut])
		)
	return user_types_choices
