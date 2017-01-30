#!/bin/bash +x
########################################################################
# run tests
# author: Valeriy Solovyov
#########################################################################
SOURCE="${BASH_SOURCE[0]}"
RDIR="$( dirname "$SOURCE" )"
echo "Running tests..."
cd "${RDIR}"
find "${RDIR}" -name "test_*.py" -type f -print0| while read -d $'\0' file_of_test
do
#for file_of_test in `ls|grep "^test_"|grep -v pyc`;do
    if [ -e "$file_of_test" ];then
        echo -n "$file_of_test"
        python $file_of_test &>/dev/null;
        if [ $? -ne 0 ];then
            echo "[FAILED]";
            exit 1
        else
            echo "[OK]";
        fi
	echo ""
    fi
done
cd "${OLDPWD}" || true
exit 0
