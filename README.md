# GCP-Logging-to-Google-Chat

## Google Log to Google Chat Integration

This guide provides step-by-step instructions on how to route Google Cloud logs to a Google Chat room using Google Cloud Functions, Pub/Sub, and Webhooks.

## Prerequisites

- Google Cloud Platform account
- Google Chat room
- Google Cloud SDK installed

## Steps

### 1. Google Chat: Create a New Room

![Google Chat: Create a New Room](https://imgur.com/KdPnTEs.png)

### 2. Select Space Setting

![Select Space Setting](https://imgur.com/ithRBdA.png)

### 3. Click on Apps & Integrations, then Add Webhook

![Apps & Integrations: Add Webhook](https://imgur.com/xWTNEFf.png)

### 4. Create Webhook Name

![Create Webhook Name](https://imgur.com/DbjpOxQ.png)

### 5. Copy Webhook URL

![Copy Webhook URL](https://imgur.com/ISoTHfc.png)

### 6. Pub/Sub: Create Topic

![Pub/Sub: Create Topic](https://imgur.com/OiMYIrI.png)

### 7. Pub/Sub: Create Topic ID

![Pub/Sub: Create Topic ID](https://imgur.com/eTnD5xF.png)

### 8. Pub/Sub Dashboard: Verify the Created Topic ID

![Pub/Sub Dashboard: Verify Topic ID](https://imgur.com/mYEDhtQ.png)

### 9. Create Log Router

![Create Log Router](https://imgur.com/dvUCITw.png)

### 10. Create Sink

![Create Sink](https://imgur.com/POfGPmD.png)

### 11. Set Sink Name and Description

![Set Sink Name and Description](https://imgur.com/EvFmisb.png)

### 12. Select Sink Service: Cloud Pub/Sub Topic and Select the Created Topic

![Select Sink Service and Topic](https://imgur.com/nEeCTUQ.png)

### 13. Set Sink Filter

![Set Sink Filter](https://imgur.com/T5lzak4.png)

### 14. Create Cloud Function

![Create Cloud Function](https://imgur.com/II2kww2.png)

### 15. Set First Gen, Function Name: `function-1`, Region: `asia-east1`, Trigger: Cloud Pub/Sub, Topic: Select the Created Topic

![Set Cloud Function Details](https://imgur.com/2nz3zYt.png)

### 16. Delete Default Code

Remove the default files.

### 17. Add `main.py` and `requirements.txt`

Replace the contents of Google Cloud Function's `main.py` with the `main.py` from the GitHub repository. Similarly, replace the `requirements.txt` with the one from the GitHub repository.

![Delete Default Code](https://imgur.com/CNzKQO4.png)

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

```

### 19. View Cloud Function Logs

Send a test log. (https://imgur.com/F65F1aJ.png)

### 20. View Google Chat Message

![View Google Chat Message](https://imgur.com/NQWIYKP.png)

## Conclusion

Following these steps, you can successfully route Google Cloud logs to a Google Chat room for monitoring and alerting purposes. This setup leverages Google Cloud Functions, Pub/Sub, and Webhooks to achieve real-time log monitoring.


