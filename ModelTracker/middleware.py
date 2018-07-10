from ModelTracker.Tracker import ModelTracker
class ModelTrackerMiddleware(object):
    def process_request(self, request):
        ModelTracker.thread.request = request



