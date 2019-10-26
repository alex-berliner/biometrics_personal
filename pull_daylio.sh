SD_DB_DIR=/mnt/sdcard/databases

DAYLIO_DB_DIR=/data/data/net.daylio/databases
DAYLIO_DB_NAME=entries.db

WITHING_DB_DIR=/data/data/com.withings.wiscale2/databases
WITHINGS_DB_NAME=room-healthmate.db

# TODO: create alias for phone IP
ssh 192.168.5.104 -p 8022 "\
    mkdir -p $SD_DB_DIR;
    su -c \"\
        cp -r $DAYLIO_DB_DIR/$DAYLIO_DB_NAME*    $SD_DB_DIR;
        cp -r $WITHING_DB_DIR/$WITHINGS_DB_NAME* $SD_DB_DIR;
    \";"

mkdir -p daylio
scp -v -r -P 8022 192.168.5.104:$SD_DB_DIR/$DAYLIO_DB_NAME* daylio/

mkdir -p withings
scp -v -r -P 8022 192.168.5.104:$SD_DB_DIR/$WITHINGS_DB_NAME* withings/

ssh 192.168.5.104 -p 8022 "rm -rf $SD_DB_DIR"
