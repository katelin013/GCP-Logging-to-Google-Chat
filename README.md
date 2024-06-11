# GCP-Logging-to-Google-Chat

## Google Log to Google Chat Integration

This guide provides step-by-step instructions on how to route Google Cloud logs to a Google Chat room using Google Cloud Functions, Pub/Sub, and Webhooks.

## Prerequisites

- Google Cloud Platform account
- Google Chat room
- Google Cloud SDK installed

## Steps

### 1. Google Chat: Create a New Room

![Google Chat: Create a New Room](https://imgur.com/KdPnTEs)

### 2. Select Space Setting

![Select Space Setting](https://imgur.com/ithRBdA)

### 3. Click on Apps & Integrations, then Add Webhook

![Apps & Integrations: Add Webhook](https://imgur.com/xWTNEFf)

### 4. Create Webhook Name

![Create Webhook Name](https://imgur.com/DbjpOxQ)

### 5. Copy Webhook URL

![Copy Webhook URL](https://imgur.com/ISoTHfc)

### 6. Pub/Sub: Create Topic

![Pub/Sub: Create Topic](https://imgur.com/OiMYIrI)

### 7. Pub/Sub: Create Topic ID

![Pub/Sub: Create Topic ID](https://imgur.com/eTnD5xF)

### 8. Pub/Sub Dashboard: Verify the Created Topic ID

![Pub/Sub Dashboard: Verify Topic ID](https://imgur.com/mYEDhtQ)

### 9. Create Log Router

![Create Log Router](https://imgur.com/dvUCITw)

### 10. Create Sink

![Create Sink](https://imgur.com/POfGPmD)

### 11. Set Sink Name and Description

![Set Sink Name and Description](https://imgur.com/EvFmisb)

### 12. Select Sink Service: Cloud Pub/Sub Topic and Select the Created Topic

![Select Sink Service and Topic](https://imgur.com/nEeCTUQ)

### 13. Set Sink Filter

![Set Sink Filter](https://imgur.com/T5lzak4)

### 14. Create Cloud Function

![Create Cloud Function](https://imgur.com/II2kww2)

### 15. Set First Gen, Function Name: `function-1`, Region: `asia-east1`, Trigger: Cloud Pub/Sub, Topic: Select the Created Topic

![Set Cloud Function Details](https://imgur.com/2nz3zYt)

### 16. Delete Default Code

Remove the default files.

### 17. Add `main.py` and `requirements.txt`

Replace the contents of Google Cloud Function's `main.py` with the `main.py` from the GitHub repository. Similarly, replace the `requirements.txt` with the one from the GitHub repository.

![Delete Default Code](https://imgur.com/CNzKQO4)

### 18. Test Log with PowerShell Command

Use the following command to test the log:

```powershell
gcloud pubsub topics publish TestTopic --message '{
  "severity": "ERROR",
  "resource": {
    "labels": {
      "project_id": "test-project",      
      "location": "asia-east1-a"
    }
  },
  "jsonPayload": {
    "timestamp": "2024-06-11 02:55:04.543",    
    "message": "Response is null, start to retry",
    "exception": null,
    "threadId": 32,
    "log": "Response is null, start to retry",
    "isErrorFlag": "1"
  }
}' --project=$PROJECT_ID

```powershell

### 18. 19. View Cloud Function Logs

Send a test log. (https://imgur.com/F65F1aJ)

### 19. View Google Chat Message

![View Google Chat Message](https://imgur.com/NQWIYKP)

## Conclusion

Following these steps, you can successfully route Google Cloud logs to a Google Chat room for monitoring and alerting purposes. This setup leverages Google Cloud Functions, Pub/Sub, and Webhooks to achieve real-time log monitoring.


