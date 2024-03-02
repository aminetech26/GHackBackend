import os
from django.http import JsonResponse
from django.views import View
from simplegmail import Gmail
import facebook
from dotenv import load_dotenv

load_dotenv()

class FacebookMessagesView(View):
    def get(self, request, *args, **kwargs):
        try:
            access_token = os.getenv('FB_ACCESS_TOKEN')
            page_id = os.getenv('PAGE_ID')

            if not access_token or not page_id:
                return JsonResponse({'success': False, 'error': 'Missing Facebook access token or page ID'})

            graph = facebook.GraphAPI(access_token)
            conversations = graph.get_object(f'{page_id}/conversations', fields='id,messages')

            messages_per_conversation = []

            for conversation in conversations['data']:
                conversation_id = conversation['id']
                messages_response = graph.get_object(f'{conversation_id}/messages', fields='id,created_time,message')

                messages_data = messages_response.get('data', [])
                formatted_messages = []

                for message in messages_data:
                    message_id = message['id']
                    single_message = graph.get_object(f'/{message_id}', fields='id,created_time,message')
                    print(single_message)

                    formatted_messages.append({
                        'id': single_message.get('id'),
                        'created_time': single_message.get('created_time'),
                        'message': single_message.get('message')
                    })


                messages_per_conversation.append({'conversation_id': conversation_id, 'messages': formatted_messages})

            return JsonResponse({'success': True, 'messages': messages_per_conversation})

        except facebook.GraphAPIError as e:
            return JsonResponse({'success': False, 'error': str(e)})


class GmailMessagesView(View):
    def get(self, request, *args, **kwargs):
        try:
            gmail = Gmail()
            messages = gmail.get_unread_inbox()
            data = []
            for message in messages:
                message_data = {
                    "to": message.recipient,
                    "from": message.sender,
                    "subject": message.subject,
                    "date": message.date,
                    "preview": message.snippet,
                    "body": message.plain or '',
                    "attachments": [attm.filename for attm in message.attachments],
                }
                data.append(message_data)
                # for message in messages:
                #     message.mark_as_read()
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


    
