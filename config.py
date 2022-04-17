import os
API_ID ="16432997" int(os.getenv("API_ID"))
API_HASH ="0840e001fad4699da3d7d87e2a4066aa" os.getenv("API_HASH")
BOT_TOKEN ="5396516569:AAFSHbNMhAQv25K4fffVCz-LfPP_vZEaD-U" os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
