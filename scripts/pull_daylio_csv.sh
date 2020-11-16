SD_DB_DIR=/mnt/sdcard/databases

DAYLIO_DB_DIR=/data/data/net.daylio/databases
DAYLIO_DB_NAME=entries.db

WITHING_DB_DIR=/data/data/com.withings.wiscale2/databases
WITHINGS_DB_NAME=room-healthmate.db

LOCAL_DB_DIR=data_backings

CLIENT_IP=192.168.5.101
CLIENT_PORT=8022
# copy app data to sdcard
# TODO: figure out how to log in as root; ssh root@<IP> logs in as user
ssh $CLIENT_IP -p $CLIENT_PORT "\
    mkdir -p $SD_DB_DIR;
    su -c \"\
        cp -r $DAYLIO_DB_DIR/$DAYLIO_DB_NAME*    $SD_DB_DIR;
        cp -r $WITHING_DB_DIR/* $SD_DB_DIR;
    \";"

# copy app data from sd card to local storage
mkdir -p $LOCAL_DB_DIR

mkdir -p $LOCAL_DB_DIR/daylio
scp -v -r -P $CLIENT_PORT $CLIENT_IP:$SD_DB_DIR/$DAYLIO_DB_NAME* $LOCAL_DB_DIR/daylio/

mkdir -p $LOCAL_DB_DIR/withings
scp -v -r -P $CLIENT_PORT $CLIENT_IP:$SD_DB_DIR/* $LOCAL_DB_DIR/withings/

# remove app data from sd card
ssh $CLIENT_IP -p $CLIENT_PORT "rm -rf $SD_DB_DIR"
