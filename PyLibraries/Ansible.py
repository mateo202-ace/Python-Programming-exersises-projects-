import ansible_runner

def run_ansible_playbook(playbook_path, inventory_path, extra_vars=None):
    """
    Run an Ansible playbook using ansible-runner.

    :param playbook_path: Path to the Ansible playbook file.
    :param inventory_path: Path to the inventory file.
    :param extra_vars: Dictionary of extra variables to pass to the playbook.
    :return: Status and output of the playbook execution.
    """
    result = ansible_runner.run(
        playbook=playbook_path,
        inventory=inventory_path,
        extravars=extra_vars
    )
    return result.status, result.stdout.read()

if __name__ == "__main__":
    # Example: Automating server patching
    playbook_path = "/path/to/patching_playbook.yml"
    inventory_path = "/path/to/inventory.ini"
    extra_vars = {
        "patching_window": "02:00-04:00",
        "reboot_required": True
    }

    status, output = run_ansible_playbook(playbook_path, inventory_path, extra_vars)

    print(f"Playbook execution status: {status}")
    print("Playbook output:")
    print(output)