import argparse
import re
import subprocess
from copy import deepcopy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", help="New name for the current workspace.")
    args = parser.parse_args()

    # command = "gsettings get org.gnome.desktop.wm.preferences num-workspaces".split()
    # num_desktops = int(subprocess.check_output(command))

    command = "xdotool get_desktop".split()
    current_workspace_index = int(subprocess.check_output(command))

    command = "gsettings get org.gnome.desktop.wm.preferences workspace-names".split()
    current_workspace_names = re.findall(
        r"\'([^']*)\'",
        str(subprocess.check_output(command)),
    )
    new_workspace_names = deepcopy(current_workspace_names)
    new_workspace_names[current_workspace_index] = args.workspace
    command = "gsettings set org.gnome.desktop.wm.preferences workspace-names".split()
    command.append(str(new_workspace_names))
    subprocess.run(command)


if __name__ == "__main__":
    main()
