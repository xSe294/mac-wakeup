# Z00-Raspy-111-Testing
1. **Connectin to SSH**
    $ ssh pi@192.168.1.111
    ```
    pi@192.168.1.111's password: pi2049
    Linux raspberrypi 6.6.20+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.6.20-1+rpt1 (2024-03-07) aarch64
    ```
2. **Showing out NFS on Raspy**
    $ showmount -e 192.168.1.111
    ```
    Export list for 192.168.1.111:
    / *
    ```
2. **Mount NFS on Raspy**
    $ sudo mount 192.168.1.111:/ /home/xse/mnt-111
3.  **Unmounting the NFS**
    $ sudo umount 192.168.1.111:/ /home/xse/mnt-111
# Test: React APP autostart
1.  ## Download xdg-utils-packages on a Raspi with internet access
    1. **$ apt-cache depends xdg-utils**
        ```
        xdg-utils
            Recommends: libfile-mimeinfo-perl
            Recommends: libnet-dbus-perl
            Recommends: libx11-protocol-perl
            Recommends: x11-utils
                x11-utils:armhf
            Recommends: x11-xserver-utils
        ```
    1. **Download each one dependency**
        ```
        $ apt-get download libfile-basedir-perl
        $ apt-get download libfile-desktopentry-perl
        ```
        ```
        $ apt-get download libfile-mimeinfo-perl
        $ apt-get download libnet-dbus-perl
        $ apt-get download libx11-protocol-perl
        $ apt-get download x11-utils  ???
        $ apt-get download x11-utils:armhf
        $ apt-get download x11-xserver-utils

        ```

2.  ## Copy xdg-utils-packages into Raspi with NO internet access
    1. Files copyed:  
        ```
        $ pwd
        /home/pi/Autostart/xdg-utils-packages
        $ tree
        .
        ├── libfile-mimeinfo-perl_0.33-1_all.deb
        ├── libnet-dbus-perl_1.2.0-2_arm64.deb
        ├── libx11-protocol-perl_0.56-9_all.deb
        ├── x11-utils_7.7+5_arm64.deb
        ├── x11-utils_7.7+5_armhf.deb
        └── x11-xserver-utils_7.7+9+b1_arm64.deb

        1 directory, 6 files

        Directory: xdg-utils-packages
        libfile-mimeinfo-perl_0.33-1_all.deb
        libnet-dbus-perl_1.2.0-2_arm64.deb
        libx11-protocol-perl_0.56-9_all.deb
        x11-utils_7.7+5_arm64.deb
        x11-utils_7.7+5_armhf.deb
        x11-xserver-utils_7.7+9+b1_arm64.deb
       ```
3.  ## Install files
    1. Go to xdg-utils-packages directory:
        ```
        $ cd /home/pi/Autostart/xdg-utils-packages
        $ sudo dpkg -i *.deb
        ```
1.  # Run Paspberry Pi Graphical app on Startup
    ```
    https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/method-2-autostart
    ```
    - I am running a graphical app, so what I want is start X Window System.
    - So I need to wait for the X server to finish initializing before running the app. 
    - Raspbian is based on the LXDE desktop environment.
    - In a Raspbian, After the desktop environment starts (LXDE-pi, in this case) it **runs:** 
      - Whatever **commands** it finds in the profile's autostart script, which is located at **/home/pi/.config/lxsession/LXDE-pi/autostart**. 
      - **If no user autostart script** is found, Linux will **run** the global **/etc/xdg/lxsession/LXDE-pi/autostart** script instead.
    - **In addition** to running commands in autostart, Linux will also look for and **execute .desktop** scripts found in **/home/pi/.config/autostart**. 
    - The easiest way to execute GUI programs on boot is to create one of these .desktop scripts.
    1. Create a **ga.desktop** file
        `$ nano /home/pi/.config/autostart/ga.desktop`
        Add this code to ga.desktop
        ```
        [Desktop Entry]
        Type=Application
        Name=GasAnalyzer
        Exec=/home/pi/Autostart-0/autostart.sh
        ```
    2. Create **autostart.sh** file
        `nano /home/pi/Autostart-0/autostart.sh`
        Add this lines:
        ```
        #!/bin/bash
        #xdg-open http://localhost/analitica
        #xterm -hold -e '/home/pi/Autostart-0/start-app.sh'
        lxterm --command '/home/pi/Autostart-0/start-app.sh'
        ```
    3. $ Create **start-app.sh** file
        `mkdir -p /home/pi/Autostart-0`
        `nano /home/pi/Autostart-0/start-app.sh`
        Add this lines:
        ```
        #!/bin/bash
        chromium-browser \
        --disable \
        --disable-translate \
        --disable-infobars \
        --disable-suggestions-service \
        --disable-save-password-bubble \
        --disk-cache-dir=$CHROMIUM_TEMP/cache/ \
        --user-data-dir=$CHROMIUM_TEMP/user_data/ \
        --start-maximized \
        --kiosk "http:localhost/analitica"
        ```
2.  # Customize the Raspberry Pi Splash Screen
    1. **The path where the splash.png is in**
        ```
        /usr/share/plymonth/themes/pix/splash.png
        ```
