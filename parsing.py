import json
import os
import paramiko
import datetime as datetime
import time
def get_data_from_json(curr_dir_path, name1, name2):
    """
    reads input from json file
    """
    events_path = os.path.join(curr_dir_path, name1)
    insights_path = os.path.join(curr_dir_path, name2)

    with open(events_path) as f1:
        events_today = json.load(f1)

    with open(insights_path) as f2:
        our_insights = json.load(f2)

    return events_today, our_insights

def mine_customer_ids(customer, events_today, our_insights):
    customer_insights_today = []
    for i in range(len(events_today)):
        for insight in our_insights:
            if insight in events_today[i] and events_today[i][1] == customer:
                dictionary = {}                                              
                dictionary["id"] = events_today[i][0]
                dictionary["insight"] = our_insights[insight]
                customer_insights_today.append(dictionary)
    
    return customer_insights_today

def write_to_output(customer_insights_today):
    """
    create json file with customer's event id's 
    """
    with open('customer_event_ids.json', 'w') as outfile:
        json.dump(customer_insights_today, outfile)

def main():
    curr_dir_path = os.path.abspath(os.path.dirname(__file__))
    events_today, our_insights = get_data_from_json(curr_dir_path, 'events_today.json', 'our_insights.json')
    customer = "Williams-Williams"
    customer_insights_today = mine_customer_ids(customer, events_today, our_insights)
    write_to_output(customer_insights_today)
    today=time.strftime('%Y%m%d')
    ssh_client=paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="localhost", username="foo",password="pass", port=2222)
    sftp_client=ssh_client.open_sftp()
    sftp_client.mkdir("/upload/upload"+str(today))
    sftp_client.put("customer_event_ids.json","/upload/upload"+str(today)+"/customer_event_ids.json")
    sftp_client.close()
    ssh_client.close()

if __name__=="__main__":
    main()
