#!/bin/bash
ffmpeg -r 60 -f image2 -s 1280x720  -i image%06d.jpg -vcodec libx264 -crf 25 -pix_fmt yuv420p snail_recon_`date +"%Y%m%d%H%M%S"`.mp4