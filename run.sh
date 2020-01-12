while getopts ":h" opt; do
  case ${opt} in
    h )
      echo "Usage:"
      echo "    pip -h                      Display this help message."
      echo "    pip install <package>       Install <package>."
      exit 0
      ;;
   d )
      # retrieve databases from phone via ssh
      ./scripts/pull_dbs.sh
     ;;
  esac
done
shift $((OPTIND -1))

# find databases in data_backings folder and convert to plaintext sql script file
python3 src/db_to_script.py

# convert my app databases into csv files containing different streams of biometric data
python3 src/db_script_to_csv.py
