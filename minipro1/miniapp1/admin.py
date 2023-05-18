from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from miniapp1.models import student
from miniapp1.models import HonorsSub
from miniapp1.models import BTSubject
from miniapp1.models import BTStudentRegistrations
from miniapp1.models import HonorsRegistration
from miniapp1.models import BTmarks
from miniapp1.models import HonorsMarks


# Register your models here.
admin.site.register(student,ImportExportModelAdmin)
admin.site.register(HonorsSub,ImportExportModelAdmin)
admin.site.register(BTSubject,ImportExportModelAdmin)
admin.site.register(BTStudentRegistrations,ImportExportModelAdmin)
admin.site.register(HonorsRegistration,ImportExportModelAdmin)
admin.site.register(BTmarks,ImportExportModelAdmin)
admin.site.register(HonorsMarks,ImportExportModelAdmin)


