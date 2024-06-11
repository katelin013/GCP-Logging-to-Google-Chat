import base64
import json
import requests

def helloPubSub(event, context):

    webhook_url = "https://chat.googleapis.com/v1/spaces/AAAAmCUFVwo/messages?key=AIzaSyDdI0hCZtE6v"

    try:
        print(f"Received event: {event}")
        
        pubsub_message = base64.b64decode(event['data']).decode('utf-8')
        print(f"PubSub Message: {pubsub_message}")

        try:
            log_entry = json.loads(pubsub_message)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return

        print(f"Decoded Pub/Sub message: {log_entry}")

        # 提取新的字段
        severity = log_entry.get('severity', 'N/A')
        cluster_name = log_entry.get('resource', {}).get('labels', {}).get('cluster_name', 'N/A')
        container_name = log_entry.get('resource', {}).get('labels', {}).get('container_name', 'N/A')
        json_payload = log_entry.get('jsonPayload', {})

        print(f"severity: {severity}")
        print(f"cluster_name: {cluster_name}")
        print(f"container_name: {container_name}")
        print(f"json_payload: {json_payload}")

        # 更新條件檢查邏輯
        is_error_flag = json_payload.get('isErrorFlag') == '1'
        is_error_or_info_severity = severity in ['ERROR', 'INFO']
        contains_error = 'error' in json_payload.get('log', '').lower()

        if not is_error_flag and not is_error_or_info_severity and not contains_error:
            print("Log message does not meet the filter criteria, skipping...")
            return

        payload_info = {
            "categoryName": json_payload.get('categoryName', 'N/A'),
            "exception": json_payload.get('exception', 'N/A'),
            "message": json_payload.get('message', 'N/A'),
            "threadId": json_payload.get('threadId', 'N/A'),
            "timestamp": json_payload.get('timestamp', 'N/A'),
            "traceId": json_payload.get('traceId', 'N/A')
        }

        try:
            message_json = json.dumps(json.loads(payload_info['message']), indent=2)
        except (json.JSONDecodeError, TypeError):
            message_json = payload_info['message']

        payload_info['message'] = message_json

        formatted_message = (
            f"Log Entry:\n"
            f"Severity: {severity}\n"
            f"Cluster Name: {cluster_name}\n"
            f"Container Name: {container_name}\n"
            f"Category Name: {payload_info['categoryName']}\n"
            f"Exception: {payload_info['exception']}\n"
            f"Message: {payload_info['message']}\n"
            f"Thread ID: {payload_info['threadId']}\n"
            f"Timestamp: {payload_info['timestamp']}\n"
            f"Trace ID: {payload_info['traceId']}\n"
        )

    except Exception as e:
        print(f"Error while parsing log entry: {e}")
        formatted_message = f"Original message: {pubsub_message}"
        error_message = {
            "text": f"Error while parsing log entry: {e}"
        }
        requests.post(webhook_url, json=error_message)
        return

    try:
        message_content = formatted_message

        max_length = 2000
        if len(message_content) > max_length:
            message_content = message_content[:max_length] + "... (message truncated)"

        message = {
            "text": message_content
        }

        print(f"Sending message to Google Chat: {message}")

        response = requests.post(webhook_url, json=message)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        if response.status_code != 200:
            raise Exception(f"Request to Google Chat returned an error {response.status_code}, the response is:\n{response.text}")

        print("Message sent to Google Chat successfully.")
    except Exception as e:
        error_message = {
            "text": f"Error while sending message to Google Chat: {e}"
        }
        print(f"Error while sending message: {e}")
        requests.post(webhook_url, json=error_message)
        raise
