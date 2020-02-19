from ModelTracker.Tracker import ModelTracker
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    # Works perfectly for everyone using MIDDLEWARE_CLASSES
    MiddlewareMixin = object

class ModelTrackerMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ModelTracker.thread.request = request
        response = self.get_response(request)
        return response

    def process_request(self, request):
        ModelTracker.thread.request = request



