from ..models import PartsAndConsumble
from ..services.base_detail_view import BaseAnnouncementDetailView

class PartsAndConsumbleDetailView(BaseAnnouncementDetailView):
    model = PartsAndConsumble
    template_name = "car_parts/car_part_detail.html"
    pk_url_kwarg = 'pk'
    
