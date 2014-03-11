from pylons.i18n import N_

from r2.lib.permissions import PermissionSet


class ReporterPermissionSet(PermissionSet):
    info = {
        "manage": {
            "title": N_("manage reporters"),
            "description": N_("more or less, it's all the same"),
        },

        "settings": {
            "title": N_("settings"),
            "description": N_("change the title, description, and timezone"),
        },

        "edit": {
            "title": N_("edit"),
            "description": N_("strike or delete others' updates"),
        },

        "update": {
            "title": N_("update"),
            "description": N_("post updates"),
        },
    }

    def __contains__(self, permission):
        if self.is_superuser():
            return True
        return self.get(permission, False)


ReporterPermissionSet.SUPERUSER = ReporterPermissionSet.loads("+all")
ReporterPermissionSet.NONE = ReporterPermissionSet.loads("")
