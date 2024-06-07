from pypresence import Presence
import time

client_id = '1248348135353356449'  # Baza is a BITCH
large_image_key = 'onlygran'  
large_image_text = 'Only Grannies'  
small_image_key = 'none'  
small_image_text = 'Level 100'  

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
