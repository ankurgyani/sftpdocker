import paramiko
import datetime as datetime
import time
today=time.strftime('%Y%m%d')
ssh_client=paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="localhost", username="foo",password="pass", port=2222)
sftp_client=ssh_client.open_sftp()
# sftp_client.chdir("/home/foo/upload/customer_event_ids.json")
sftp_client.mkdir("/upload/upload"+str(today))
#sftp_client.get("/upload/customer_event_ids.json","paramiko_download.json")
sftp_client.put("customer_event_ids.json","/upload/ankur/customer_event_ids.json")  ##TO-D0: figure out how to upload in the newly created dir now
sftp_client.close()
ssh_client.close()
