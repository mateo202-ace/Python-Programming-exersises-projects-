import os
import logging
from azure.identity import ClientSecretCredential  # For authenticating using a service principal
from azure.mgmt.resource import SubscriptionClient  # For managing Azure subscriptions
from azure.mgmt.network import NetworkManagementClient
from google.cloud import compute_v1
from config import AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_SUBSCRIPTION_ID, GCP_CREDENTIALS_PATH  # Importing Azure credentials from config.py


# Function to get firewall info from Azure & get list of Subscription IDs in Azure
def get_azure_firewall_info():
    #Used for authentication to Azure
    credential = ClientSecretCredential(
        tenant_id = AZURE_TENANT_ID,
        client_id = AZURE_CLIENT_ID,
        client_secret = AZURE_CLIENT_SECRET
    )

    # Create a Subscription intance to interact with Azure Subs
    subscription_client = SubscriptionClient(credential)

    subscriptions = subscription_client.subscriptions.list()
    for subscription in subscriptions:
        print(f'Subscriptioin ID: {subscription.subscription_id}')

# Function for Checking IPs and Open Ports in Azure 
def check_public_ips_azure():
    try:

        credential = ClientSecretCredential(
            tenant_id = AZURE_TENANT_ID,
            client_id = AZURE_CLIENT_ID,
            client_secret = AZURE_CLIENT_SECRET
        )

        network_client = NetworkManagementClient(credential, AZURE_SUBSCRIPTION_ID)

        public_ips = network_client.public_ip_addresses.list_all() # Lists all public IPs in Subscription 

        for ip in public_ips:
         print(f'Public IP: {ip.ip_address}')

    except Exception as e:
        print(f'Error: {e}')


   
 # Function to get firewall info from GCP   
def get_gcp_firewall_info():
    firewall_client = compute_v1.FirewallsClient()
    project_id = 'premium-apex-453517-u3'

    # Get all firewall rules for the project & Iterate through the firewall rules for the GCP project
    firewall_rules = firewall_client.list(project=project_id)

    for item in firewall_rules:
        print(f'Firewall rule: {item.name}')

# Function to check for open ports in GCP
def check_open_ports_gcp():
    firewall_client = compute_v1.FirewallsClient()
    project_id = 'premium-apex-453517-u3'

    firewall_rules = firewall_client.list(project=project_id) # retrive all firewall rules accross all networks in the project

    for firewall in firewall_rules:
        if firewall.allowed:
            for rule in firewall.allowed:
                print(f'Open port: {rule.ports}')
                if any(port in ['22', '3389'] for port in rule.ports):
                    print(f'ALERT: Open port found: {rule.ports} (Potential security risk!)')


logging.basicConfig(filename='security_audit_log.txt', level=logging.INFO) # Sets up logging to a file

def log_info(message):
    logging.info(message) # Log info-level message to file
    print(message) # prints in console for immediate feeedback

def log_error(message):
    logging.error(message) # Log info-level message to file
    print(f'ERROR: {message}') # prints in console for immediate feeedback



# Main function to excecute to execute the entire auditing process
def main():
    print('Checking Azure Security Information.....')
    get_azure_firewall_info()

    print('\nChecking Azure Public IPs & Ports...... ')
    check_public_ips_azure()

    print('\nChecking GCP Security Information.....')
    get_gcp_firewall_info()

    print('\nChecking GCP for Open Ports......')
    check_open_ports_gcp()


# Check if this script is being run as the main module (not being imprted)
if __name__ == '__main__':
    main()