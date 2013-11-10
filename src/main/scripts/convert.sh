for file in `ls -1|grep MTS`
do
  NEW_NAME=`stat -c %y ${file} |cut -f1 -d" "`.avi
  if [ NEW_NAME = ]
  echo ${NEW_NAME}
  PREVIOUS_NAME=${NEW_NAME}
done
