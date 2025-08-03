from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import calculate_fare

class FareCalculatorView(APIView):
    def post(self, request):
        journeys = request.data.get("journeys", [])
        total = 0
        detailed_fares = []
        for trip in journeys:
            from_zone = trip.get("from_zone")
            to_zone = trip.get("to_zone")
            fare = calculate_fare(from_zone, to_zone)
            total += fare
            detailed_fares.append({
                "from_zone": from_zone,
                "to_zone": to_zone,
                "fare": fare
            })
        return Response({
            "journeys": detailed_fares,
            "total_fare": total
        })
