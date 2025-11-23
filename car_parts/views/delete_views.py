from common.views.base_delete_view import BaseDeleteAnnouncementView
from django.urls import reverse_lazy


class PartsDeleteView(BaseDeleteAnnouncementView):
    app_name = "car_parts"
    template_name = "auto/delete_confirmation.html"
    success_url = reverse_lazy("auto:get_my_announcements")

