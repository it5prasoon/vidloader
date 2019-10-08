#!/bin/bash
clear
echo "

██╗████████╗███████╗        ██████╗ ██████╗  █████╗ ███████╗ ██████╗  ██████╗ ███╗   ██╗
██║╚══██╔══╝██╔════╝        ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔═══██╗██╔═══██╗████╗  ██║
██║   ██║   ███████╗        ██████╔╝██████╔╝███████║███████╗██║   ██║██║   ██║██╔██╗ ██║
██║   ██║   ╚════██║        ██╔═══╝ ██╔══██╗██╔══██║╚════██║██║   ██║██║   ██║██║╚██╗██║
██║   ██║   ███████║███████╗██║     ██║  ██║██║  ██║███████║╚██████╔╝╚██████╔╝██║ ╚████║
╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
                                                                                        
";

 INSTALL_DIR="/usr/share/doc/vidloader"

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ];
then
    echo "[◉] A directory VidLoader was found! Do you want to replace it? [Y/n]:" ;
    read decision
    if [ $decision == "y" ] ;
    then
      sudo rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
sudo apt-get install -y python-pip
sudo pip install --upgrade youtube_dl
sudo apt-get install -y libav-tools
git clone https://github.com/it5prasoon/vidloader.git $INSTALL_DIR;
echo "#!/bin/bash
python $INSTALL_DIR/vidloader.py" '${1+"$@"}' > vidloader;
chmod +x vidloader;
sudo cp vidloader /usr/bin/;


if [ -d "$INSTALL_DIR/vidloader" ];
then
    echo "";
    echo "[✔] All the tools are installed successfully!! [✔]";
    echo "";
    echo "[✔]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[✔]";
    echo "[✔] ✔✔✔  All is done!! Now you can Pirate Videos With VidLoader !  ✔✔✔ [✔]";
    echo "[✔]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[✔]";
    echo "";
else
    echo "[✘] Installation failed![✘] ";
    exit
fi
