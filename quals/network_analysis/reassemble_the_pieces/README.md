# Reassemble The Pieces

## Challenge (??? points, ??? solves)

BH-2000 relayed important information through a streaming service, but I wasn't able to view the content.
Let's try to uncover it by examining the captured network packet file.

Flag format: CDDC2025{   }

## Summary

- Read the part about the RTSP protocol in the pcap file
- Notice that the RDP packets (dynamic type 96) are in H264 format
- Use "Decode as" to force Wireshark to decode the packets as H264
- Use this [tool](https://github.com/volvet/h264extractor/tree/master) to extract the H264 stream
- Use ffmpeg to convert the H264 stream to a mp4 file
- The flag is shown in the video
