#!/bin/bash
# Run these commands:
# chmod +x palm-detect.sh
# sudo sed -i '/^exit 0/i /home/rmad/repos/scripts/palm-detect.sh &&' /etc/rc.local
sleep 20
synclient PalmDetect=1 && synclient PalmMinWidth=5
