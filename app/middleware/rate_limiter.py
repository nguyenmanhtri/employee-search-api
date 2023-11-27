import time
import logging

from collections import defaultdict
from django.http import JsonResponse
from django.conf import settings

request_counters = defaultdict(int)
request_timestamps = defaultdict(float)
logger = logging.getLogger(__name__)


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get("REMOTE_ADDR")
        current_time = time.time()

        # Reset count if time window has passed
        if (
            current_time - request_timestamps[client_ip]
            > settings.RATE_LIMIT_CONFIGS["TIME_WINDOW"]
        ):
            request_counters[client_ip] = 1
            request_timestamps[client_ip] = current_time
        else:
            request_counters[client_ip] += 1

        if request_counters[client_ip] > settings.RATE_LIMIT_CONFIGS["REQUEST_COUNT"]:
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        response = self.get_response(request)
        return response
