import requests

def meraki_get(resource):
    api_path = "https://api.meraki.com/api/v0"
    headers = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
    }
    get_resp = requests.get(f"{api_path}/{resource}", headers=headers)
    get_resp.raise_for_status()
    return get_resp.json()

def main ():
    orgs = meraki_get("organizations")
    print("Organization discovered:")

    devnet_id = 0
    for org in orgs:
        print(f"ID: {org['id']:<6} Name:{org['name']}")
        if "devnet" in org["name"].lower():
            devnet_id = org["id"]
    if devnet_id:
        networks = meraki_get(f"organizations/{devnet_id}/networks")
        print(f"\nNetworks seen for DevNet org ID {devnet_id}:")

        devnet_network = ""
        for network in networks:
            print(f"NETWORK ID: {network['id']} Name: {network['name']}")
            if "devnet" in network["name"].lower():
                devnet_network = network["id"]
        if  devnet_network:
            devices = meraki_get(f"networks/{devnet_network}/devices")
            print(f"\nDevices seen on the DevNet network{devnet_network}:")
            for devices in devices:
                print(f"Model: {device['model']:,8} IP: {device['lanIp']}")


if __name__ == "__main__":
    main()