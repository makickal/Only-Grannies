from pypresence import Presence
import time

client_id = '1248348135353356449'  # Replace with your application's client ID
large_image_key = 'onlygran'  # Replace with the exact key of your uploaded large image
large_image_text = 'Only Grannies'  # Text displayed when hovering over the large image
small_image_key = 'none'  # Replace with the exact key of your uploaded small image
small_image_text = 'Level 100'  # Text displayed when hovering over the small image

RPC = Presence(client_id)
RPC.connect()

# Set up the presence information
RPC.update(
    state="In Session",
    details="Getting Freak On",
    start=1507665886,
    end=3507665886,
    large_image=large_image_key,
    large_text=large_image_text,
    small_image=small_image_key,
    small_text=small_image_text,
    party_id="ae488379-351d-4a4f-ad32-2b9b01c91657",
    party_size=[1, 5],
    join="MTI4NzM0OjFpMmhuZToxMjMxMjM="
)

# Keep the script running to maintain the presence
while True:
    time.sleep(15)
