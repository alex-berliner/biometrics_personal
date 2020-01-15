while getopts ":hd" opt; do
  case ${opt} in
    h )
      echo "Usage:"
      echo "-d: pull dbs from device"
      exit 0
      ;;
   d )
      # retrieve databases from phone via ssh
      echo "pulling dbs"
      ./scripts/pull_dbs.sh
     ;;
  esac
done
shift $((OPTIND -1))

# find databases in data_backings folder and convert to plaintext sql script file
python3 src/db_to_script.py

# convert my app databases into csv files containing different streams of biometric data
python3 src/db_script_to_csv.py
