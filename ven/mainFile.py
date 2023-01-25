from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)
for x in range(100):
    message = client.messages.create(

        body="This is a message",
        from_=keys.twilio_number,
        to=keys.target_number
    )

