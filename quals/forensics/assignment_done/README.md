# Assignment done!

## Challenge (??? points, ??? solves)

Whew! Assignment done!
Now I just have to put it in the USB flash drive and show it to Star.

The USB flash drive was connected right after the assignment was done.

1. Find the entire serial number of the device.
2. Find the disconnected time of the device.
   - (YYYY-MM-DD_hh:mm:ss) (UTC+9)

Flag format: CDDC2025{1_2}

## Summary

This is a Windows forensics challenge where the goal is to extract the serial number and disconnection timestamp of a USB device using Windows Event Logs. The trick lies in understanding which Event IDs contain USB connection/disconnection metadata, and extracting the right values.

Refer to this [website](https://www.senturean.com/posts/19_08_03_usb_storage_forensics_1/) for more information on USB storage forensics. Use FTK Imager to analyze the Windows Event Log files.
