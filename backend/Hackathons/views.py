# path: hackathons/views.py
import datetime

from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny

from Users.models import Users
from Hackathons.models import HackathonDetails

from commons.mandatory_checks import mandatory_param_check
from commons.common_response import basic_response_dict


class HackathonViews(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        created_by = data.get('created_by')
        title = data.get('title')
        description = data.get('description')
        background_image = data.get('background_image')
        hackathon_image = data.get('hackathon_image')
        submission_type = data.get('submission_type')
        reward_prize = data.get('reward_prize')

        param_check = mandatory_param_check([title, submission_type, reward_prize])

        if param_check:
            response = basic_response_dict("Mandatory params are not provided", "Empty params", None, 404)
            return Response(response, status=status.HTTP_200_OK)

        # try:
        #     created_by = Users.objects.get(id=created_by)
        # except Exception as e:
        #     response = basic_response_dict("Failed to get user!", str(e), request.data)
        #     return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            hackathon_obj = HackathonDetails.objects.create(
                title=title,
                description=description,
                background_image=background_image,
                hackathon_image=hackathon_image,
                submission_type=submission_type,
                reward_prize=reward_prize
                start_datetime=datetime.datetime.now()
            )
            hackathon_obj.save()
        except Exception as e:
            response = basic_response_dict("Hackathon creation failed", str(e), request.data, 400)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        response = basic_response_dict("Hackathon created successfully", None, [], 200)
        return Response(response, status=status.HTTP_200_OK)

    
    # def get(self, request):
    #     data = request.GET
    #     hackathon_id = data.get('hackathon_id')
    #     
    #     if hackathon_id:
    #         result = HackathonDetails.objects.get(id=hackathon_id)
    #         
    #         response = basic_response_dict("Hackathon Data", None, result, 200)
    #         return Response(response, status=status.HTTP_200_OK)

    def get(self):
        hackathons = HackathonDetails.objects.all()

        result = []
        for hackathon in hackathons:
            result.append({
                "title": hackathon.title,
                "description": hackathon.description,
                "background_image": hackathon.background_image,
                "hackathon_image": hackathon.hackathon_image,
                "submission_type": hackathon.submission_type,
                "reward_prize": hackathon.reward_prize,
                "start_date_time": hackathon.start_datetime,
                "end_date_time": hackathon.end_datetime
            })
        
        response = basic_response_dict("Hackathon Data", None, result, 200)
        return Response(response, status=status.HTTP_200_OK)
