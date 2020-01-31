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

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/Vidloader" ] ;
then
echo "[◉] A directory Vidloader was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/Vidloader"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/it5prasoon/vidloader.git /usr/share/doc/Vidloader;
 echo "#!/bin/bash 
 python /usr/share/doc/Vidloader/vidloader.py" '${1+"$@"}' > vidloader;
 chmod +x vidloader;
 sudo cp vidloader /usr/bin/;
 rm vidloader;


if [ -d "/usr/share/doc/Vidloader" ] ;
then
echo "";
echo "[✔]Tool istalled with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔] ✔✔✔ All is done!! You can execute tool by typing Vidloader  !   ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation failed![✘] ";
  exit
fi
