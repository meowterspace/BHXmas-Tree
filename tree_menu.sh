clear

TREE="    _\/_\n     /\\n     /\\n    /  \\n    /~~\o\n   /o   \\n  /~~*~~~\\n o/    o \\n /~~~~~~~~\~\n/__*_______\\n     ||\n   \====/\n    \__/"

while [ 1 ]
do
OPTION=$(
whiptail --title "Tree Menu" --menu 'Merry Christmas Developer! Select options:' 25 104 16 \
"Cycle patterns" "Cycle through the scripts in /scripts." \
"Pull Repo" "Pull down latest repo changes." \
"Tree config" "Change tree settings" \
"Tree docs" "View tree pattern documentation" \
"Kill Scripts" "Turn off all running light scripts" \
"Terminal" "Break into RPi shell." \
"Shut Down" "Turn off the raspberry pi." 3>&2 2>&1 1>&3
)

case $OPTION in
	"Cycle patterns")
		python3 lights.py &>/dev/null &
		disown
	;;
	"Pull Repo")
	;;
	"Tree config")
	;;
	"Tree docs")
		whiptail --title "Tree docs" --msgbox "Coming soon...." 8 45
	;;
	"Kill Scripts")
		python3 tree_off.py &>/dev/null &
	;;
	"Terminal")
		whiptail --passwordbox "Please enter admin password to break menu" 8 78 --title "Terminal" 3>&1 1>&2 2>&3
		exit
	;;
	"Shut down")
		whiptail --yesno "Are you sure you want to shut down?" 8 45 --title "Shut Down" 3>&1 1>&2 2>&3
		exit
	;;
esac
done
exit
