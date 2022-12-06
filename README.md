# pytest-recordtop
用例执行过程中记录 top 命令中的值。
## 使用方法

```shell
pytest --top 5
```

表示记录前 5 个进程，如下：

```shell
top - 18:23:32 up 1 day,  8:34,  1 user,  load average: 0.43, 0.50, 0.49
Tasks: 412 total,   1 running, 410 sleeping,   0 stopped,   1 zombie
%Cpu(s):  0.6 us,  0.5 sy,  0.0 ni, 98.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  15932.3 total,    264.3 free,   8556.2 used,   7111.7 buff/cache
MiB Swap:  16384.0 total,  16368.5 free,     15.5 used.   6939.8 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                      
   1934 root      20   0 1922228 230344 131464 S   7.0   1.4  37:42.18 Xorg                         
   2348 mikigo    20   0 5425232 142520  73264 S   6.6   0.9  20:26.58 dde-session-dae              
   2409 mikigo    20   0 5906488 212824 135580 S   5.0   1.3  34:49.56 kwin_x11                     
  22142 mikigo    20   0 2453524 121048  93440 S   5.0   0.7   1:51.63 deepin-terminal              
   2624 mikigo    20   0 3565656 144924 101304 S   4.0   0.9  12:02.55 dde-dock                                      
```

每隔 3 秒会记录一次上面的信息，并追加写入到 `/tmp/logs/top_xxxxxxxxxx.log` 文件中。
