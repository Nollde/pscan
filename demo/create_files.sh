for param0 in a b c
do
    for param1 in 1 2 3
    do
        tp="param0_${param0}/param1_${param1}"
        mkdir -p $tp
        echo "${param0} ${param1}" >> "${tp}/file.txt"
    done
done
