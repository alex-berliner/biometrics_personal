SD_DB_DIR=/mnt/sdcard/databases

DAYLIO_DB_DIR=/data/data/net.daylio/databases
DAYLIO_DB_NAME=entries.db

WITHING_DB_DIR=/data/data/com.withings.wiscale2/databases
WITHINGS_DB_NAME=room-healthmate.db

LOCAL_DB_DIR=data_backings

# copy app data to sdcard
# TODO: create alias for phone IP
# TODO: figure out how to log in as root; ssh root@<IP> logs in as user
ssh 192.168.5.104 -p 8022 "\
    mkdir -p $SD_DB_DIR;
    su -c \"\
        cp -r $DAYLIO_DB_DIR/$DAYLIO_DB_NAME*    $SD_DB_DIR;
        cp -r $WITHING_DB_DIR/* $SD_DB_DIR;
    \";"

# copy app data from sd card to local storage
mkdir -p $LOCAL_DB_DIR

mkdir -p $LOCAL_DB_DIR/daylio
scp -v -r -P 8022 192.168.5.104:$SD_DB_DIR/$DAYLIO_DB_NAME* $LOCAL_DB_DIR/daylio/

mkdir -p $LOCAL_DB_DIR/withings
scp -v -r -P 8022 192.168.5.104:$SD_DB_DIR/* $LOCAL_DB_DIR/withings/

# remove app data from sd card
ssh 192.168.5.104 -p 8022 "rm -rf $SD_DB_DIR"
