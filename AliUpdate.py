import sys
from aligo import Aligo

upload_file,refresh_token=sys.argv[1],sys.argv[2]

ali=Aligo(refresh_token=refresh_token)

ali.upload_folder(upload_file)
