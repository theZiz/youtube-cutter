Youtube-Cutter
==============

Needs
-----
* Python3
* Ffmpeg (avconv)
* Tagmp3

Usage
-----
```youtube-cutter.sh youtube-download.m4a description.txt [shift] [end-deletion]```

The description.txt needs to have such a format:

```
01. 00:00:00 Song 1
02. 00:02:14 The second song
03. 00:04:56 Just another song
.
.
.
```

However, the hours, the leading zeros and the period after the title number are optional.

```shift``` shifts all time stamps if they are inaccurate.

With ```end-deletion``` the last seconds of a song can be ignored.
